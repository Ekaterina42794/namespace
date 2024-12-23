'''Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новую функцию test_function
Создайте внутри test_function другую функцию - inner_function,
Эта функция должна печатать значение "Я в области видимости функции test_function"
Вызовите функцию inner_function внутри функции test_function
Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы'''
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
print(inner_function()) #name 'inner_function' is not defined.\имя 'inner_function' не определено.
inner_function() #name 'inner_function' is not defined.\имя 'inner_function' не определено.
test_function()

