import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "343748829"))

GOOGLE_DRIVE_FOLDER_ID = "1zA9vOuVhqyBUHyMoefCcXtLEd1qHnJx7"
SERVICE_ACCOUNT_FILE = "service_account.json"

DB_PATH = "database.db"
EXPORT_PATH = "exports"
PDF_GUIDE_PATH = "13_opor.pdf"
PRODUCTS_EXCEL_PATH = "Список продуктов.xlsx"

os.makedirs(EXPORT_PATH, exist_ok=True)

CHANNEL_LINK = "https://t.me/neidealniy_nutriciolog"
GROUP_LINK = "https://t.me/+guNv9c0RxTY5YjRi"
PERSONAL_LINK = "https://t.me/Ekaterina_andreeva13"   # Google Drive
SERVICE_ACCOUNT_FILE = "service_account.json"
GOOGLE_DRIVE_FOLDER_ID = "1zA9vOuVhqyBUHyMoefCcXtLEd1qHnJx7"
