def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, "w", encoding='utf-8')
    for string_index in range(len(strings)):
        strings_positions[(string_index+1, file.tell())] = strings[string_index]
        file.write(strings[string_index] + "\n")
    file.close()
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