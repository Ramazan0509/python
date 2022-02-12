__author__ = 'Magomedov Ramazan'
# Задача-2: Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
time_in_sec = int(input("Введите время в секундах: "))
hours = time_in_sec // 3600
residue = time_in_sec % 3600
minutes = residue // 60
sec = residue % 60
print(f"Сейчас время: {hours}:{minutes}:{sec} ")
