class TestCase:
    def __init__(self):
        # В начале шагов нет — создаём пустой словарь
        self.steps = {}
        # Ожидаемого результата пока нет
        self.result = None

    def set_step(self, step_number, step_text):
        # Добавляем шаг в словарь по номеру шага
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        # Удаляем шаг по его номеру
        if step_number in self.steps:
            del self.steps[step_number]

    def set_result(self, result):
        # Устанавливаем ожидаемый результат
        self.result = result

    def get_test_case(self):
        # Выводим шаги и результат
        print("Шаги:", self.steps)
        print("Ожидаемый результат:", self.result)


# Создаём объект теста
test = TestCase()

# Добавляем шаги
test.set_step(1, 'Открыть сайт')
test.set_step(2, 'Перейти в раздел Товары')
test.set_step(3, 'Выбрать первый товар')
test.set_step(4, 'Нажать кнопку "Купить"')

# Удалим один шаг, например шаг 3
test.delete_step(3)

# Установим ожидаемый результат
test.set_result('Товар окажется в корзине')

# Выведем весь тест-кейс
test.get_test_case()