import sys

# Некоторые функции sys
print('Версия Python:', sys.version)
print('ОС:', sys.platform)
print('Путь к файлам:', sys.path)

print()

# Вывод в консоль
# 1
print('Hello', 'world!')
# 2
sys.stdout.write('Hello world!\n')

# Ввод из консоли
# 1
a = input('[input] Enter \'a\': ')
print("a = ", a)
# 2
print('[stdin] Enter \'b\': ', end='', flush=True)
b = sys.stdin.readline()
print("b = ", b)


# Сохранение оригинальных потоков ввода/вывода
original_stdout = sys.stdout
original_stdin = sys.stdin

# Вывод в файл
out_file = open('stdout_test.txt', 'w', encoding='utf-8')
sys.stdout = out_file

print('This line goes to file \'stdout_test.txt\'')
print('Apple', 'Apricot', 'Banana', 'Kiwi', sep='\n')

sys.stdout = original_stdout
out_file.close()

# Ввод из файла
in_file = open('stdout_test.txt', 'r', encoding='utf-8')
sys.stdin = in_file

print('File \'stdout_test.txt\' contains:')
i = 0
for line in sys.stdin:
    i += 1
    print(i, line.strip())

sys.stdin = original_stdin
in_file.close()

# Поток ошибок
original_stderr = sys.stderr

with open('stderr_test.txt', 'w', encoding='utf-8') as err_file:
    sys.stderr = err_file

    sys.stderr.write('Error 1\n')
    sys.stderr.write('Error 2')

    sys.stderr = original_stderr