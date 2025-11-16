# Исходная строка с временными значениями
time_data = '1h 45m,360s,25m,30m 120s,2h 60s'

# Разбиваем строку по запятой
time_chunks = time_data.split(',')

# Общая сумма минут
total_minutes = 0

# Обрабатываем каждый кусочек
for chunk in time_chunks:
    parts = chunk.split()  # разбиваем, если есть пробелы, например: '1h 45m'
    
    for part in parts:
        if 'h' in part:
            hours = int(part.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in part:
            minutes = int(part.replace('m', ''))
            total_minutes += minutes
        elif 's' in part:
            seconds = int(part.replace('s', ''))
            total_minutes += seconds // 60  # переводим в минуты

# Выводим результат
print(total_minutes)