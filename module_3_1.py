calls = 0 # Глобальная переменная, чтобы посчитать вызов функций

def count_calls():
    global calls # обпращение к глобальной переменной
    calls += 1

def string_info(string):
    count_calls()  # фиксируем вызов функции
    length = len(string) # длина строки
    upper = string.upper() # Перевод в верхний регистр
    lower = string.lower() # Перевод в нижний регистр
    return (length, upper, lower)

def is_contains(string, list_to_search):
    count_calls()  # # фиксируем вызов функции
    return string.lower() in (item.lower() for item in list_to_search) # Сравниваем строку с элементами списка без учёта регистра

# Примеры вызовов функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))    # False


print(calls) # число вызова всех функций

