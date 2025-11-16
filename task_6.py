# Словарь с уровнями критичности
types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

# Словарь с тикетами по критичности
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

# Функция для удаления дублей
def remove_duplicates(ticket_dict):
    unique_tickets = set()
    result = {}

    for level, ticket_list in ticket_dict.items():
        # Создаём новый список только с уникальными тикетами
        new_list = []
        for ticket in ticket_list:
            if ticket not in unique_tickets:
                new_list.append(ticket)
                unique_tickets.add(ticket)
        result[level] = new_list
    return result

# Функция связывает уровни критичности с тикетами
def link_tickets(types_dict, tickets_dict):
    unique_tickets = remove_duplicates(tickets_dict)
    result = {}

    for level, name in types_dict.items():
        result[name] = unique_tickets.get(level, [])
    return result

# Вызываем функцию и печатаем итоговый словарь
final_dict = link_tickets(types, tickets)
print(final_dict)