def digit_root(num):
    # Первый раз: складываем цифры
    num_str = str(num)
    sum_digits = 0
    for digit in num_str:
        sum_digits += int(digit)

    # Проверка: если сумма всё ещё больше 9, снова складываем
    if sum_digits > 9:
        num_str = str(sum_digits)
        sum_digits = 0
        for digit in num_str:
            sum_digits += int(digit)

        # Ещё одна проверка
        if sum_digits > 9:
            num_str = str(sum_digits)
            sum_digits = 0
            for digit in num_str:
                sum_digits += int(digit)

    return sum_digits

# Примеры
print(digit_root(4851))     # 9
print(digit_root(97569))    # 9
print(digit_root(889987))   # 4