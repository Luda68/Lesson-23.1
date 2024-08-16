
import os.path
def custom_write(file_name, strings):
    strings_positions = dict()
    with open(file_name, 'w', encoding = "utf-8") as file:
        for index, string in enumerate(strings):
#            print(index, string)
            strings_positions[(index + 1, file.tell())] = string
            file.write(string + '\n')
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)