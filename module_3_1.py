calls = 0

def count_calls():
    global calls
    calls+=1 # Изменяем значение переменной

def string_info(string):
    count_calls()
    # Возвращаем кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    # Возвращаем True, если строка находится в этом списке, False - если отсутствует. Регистром строки при
    # проверке пренебречь: UrbaN ~ URBAN
    return string.upper() in [s.upper() for s in list_to_search]

print("Вывод на консоль:")
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)