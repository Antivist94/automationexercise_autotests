from datetime import datetime, timedelta


def calculate_date(start_date: str, days_offset: int) -> str:
    # Проверяем, является ли начальная дата "сегодня"
    if start_date.lower() == "сегодня":
        start_date = datetime.now()
    else:
        raise ValueError("Поддерживается только параметр 'сегодня' для начальной даты")

    # Добавляем указанное количество дней
    new_date = start_date + timedelta(days = days_offset)

    # Форматируем дату в нужный формат
    formatted_date = new_date.strftime("%d/%m/%Y")

    return formatted_date


# Пример использования
if __name__ == "__main__":
    days = int(input("Введите количество дней для прибавления: "))
    result_date = calculate_date("сегодня", days)
    print(f"Дата через {days} дней: {result_date}")