import random
import string
import sys
import time

# Функция возвращает послейдний байт от текущего значения наносекунд
def generate_random_byte_from_nanoseconds():
    random.seed()
#     Устанавливаем точность времени до наносекунд
    cur_time_str = str('%.9f' % time.time())
#     Берем значение дробной части текущего времени
    nanoseconds = int(cur_time_str.split('.')[1])
#     Берем последний байт наносекунд
    byte = nanoseconds.to_bytes(4, byteorder='big')[3]
#     Для случайного результата наносекунд устанавливаем случайное ожидание
    time.sleep(random.randint(0, 255)*1e-9)
    return byte

# Функция возвращает сгенерированный пароль заданной длины
def generate_rand_pass(length):
    password = ''
    count = 0
    while count != length:
        byte = chr(generate_random_byte_from_nanoseconds())
#         Проверяем, соотв. ли полученный байт нужному нам символу
        if byte in string.ascii_letters or byte in string.digits:
            password += byte
            count += 1
    print(password)


def main():
#     Задаем длинну пароля в консоли
    if len(sys.argv) == 1:
        generate_rand_pass(sys.argv[1])
    else:
        sys.exit('You need to specify the password size as first argument')


if __name__ == "__main__":
    main()
