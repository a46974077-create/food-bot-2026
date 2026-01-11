"""
google_drive.py - Интеграция с Google Drive
"""

import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

from config import SERVICE_ACCOUNT_FILE, GOOGLE_DRIVE_FOLDER_ID

class GoogleDriveService:
    def __init__(self):
        self.service = None
        self.authenticate()
    
    def authenticate(self):
        """Аутентификация через сервисный аккаунт"""
        try:
            creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE,
                scopes=['https://www.googleapis.com/auth/drive.file']
            )
            self.service = build('drive', 'v3', credentials=creds)
            print("✅ Google Drive аутентификация успешна")
        except Exception as e:
            print(f"❌ Ошибка аутентификации Google Drive: {e}")
            self.service = None
    
    def upload_file(self, file_path, file_name):
        """Загрузка файла в Google Drive"""
        if not self.service:
            return None
        
        try:
            file_metadata = {
                'name': file_name,
                'parents': [GOOGLE_DRIVE_FOLDER_ID]
            }
            
            media = MediaFileUpload(
                file_path,
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            
            file = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id, webViewLink'
            ).execute()
            
            print(f"✅ Файл загружен: {file.get('webViewLink')}")
            return file.get('webViewLink')
            
        except HttpError as error:
            print(f'❌ Ошибка загрузки файла: {error}')
            return None
    
    def list_files(self):
        """Список файлов в папке"""
        if not self.service:
            return []
        
        try:
            results = self.service.files().list(
                q=f"'{GOOGLE_DRIVE_FOLDER_ID}' in parents",
                pageSize=10,
                fields="files(id, name, createdTime)"
            ).execute()
            
            return results.get('files', [])
            
        except HttpError as error:
            print(f'❌ Ошибка получения списка файлов: {error}')
            return []

drive_service = GoogleDriveService()