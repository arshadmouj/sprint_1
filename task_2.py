class Tester:
    def __init__(self, name):
        self.name = name  # сохраняем имя
        self.deadline = True  # изначально дедлайн включен

    def work_hard(self, deadline=True):  # сюда можно передать новый дедлайн
        self.deadline = deadline  # сохраняем значение в атрибут
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

# создаём двух тестеров и проверяем
tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'

tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'