# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
def user_info(name, surname, year_of_birth, city, user_email, user_tel):
    print(
        f'Имя: {name}, Фамилия: {surname}, Год рождения: {year_of_birth}, Город проживания: {city}, Email: {user_email}'
        f', Телефон: {user_tel}')


user_info(name=input('Имя: '), surname=input('Фамилия: '),
          year_of_birth=input('Год рождения: '), user_email=input('Email: '),
          city=input('Город проживания: '), user_tel=input('Телефон: '))
