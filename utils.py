"""
utils.py - Утилиты для расчётов
"""

def calculate_bmi(weight, height):
    """Расчёт ИМТ"""
    height_m = height / 100
    return round(weight / (height_m * height_m), 1)

def get_bmi_category(bmi):
    """Категория ИМТ"""
    if bmi < 18.5:
        return "Недостаточный вес 🟡"
    elif 18.5 <= bmi < 25:
        return "Нормальный вес ✅"
    elif 25 <= bmi < 30:
        return "Избыточный вес 🟠"
    else:
        return "Ожирение 🔴"

def calculate_ideal_weight(height, gender, body_type):
    """Идеальный вес с учётом пола и телосложения"""
    if height <= 165:
        base = height - 100
    elif 166 <= height <= 175:
        base = height - 105
    else:
        base = height - 110
    
    if body_type == "астеник":
        base *= 0.9
    elif body_type == "гиперстеник":
        base *= 1.1
    
    return round(base, 1)

def calculate_bmr(weight, height, age, gender):
    """Базовый метаболизм (формула Миффлина-Сан Жеора)"""
    if gender == "мужчина":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return round(bmr)

def calculate_daily_calories(bmr, activity):
    """Суточная потребность в калориях"""
    activity_factors = {
        "1.4": 1.4, "1.6": 1.6, "1.9": 1.9, "2.2": 2.2, "2.5": 2.5
    }
    factor = activity_factors.get(str(activity), 1.6)
    return round(bmr * factor)

def calculate_water_norm(ideal_weight, activity):
    """Норма воды на идеальный вес"""
    base = ideal_weight * 30
    if activity >= 2.2:
        base += 500
    elif activity >= 1.9:
        base += 250
    return round(base)

def validate_height(height_text):
    """Валидация роста"""
    try:
        height = int(height_text)
        if 100 <= height <= 250:
            return height, None
        else:
            return None, "Рост должен быть от 100 до 250 см"
    except ValueError:
        return None, "Пожалуйста, введите число (например: 165)"

def validate_weight(weight_text):
    """Валидация веса"""
    try:
        weight = float(weight_text.replace(',', '.'))
        if 30 <= weight <= 300:
            return weight, None
        else:
            return None, "Вес должен быть от 30 до 300 кг"
    except ValueError:
        return None, "Пожалуйста, введите число (например: 65.5)"