# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
str_count = 0
word_amt = 0
str_info = {}
with open('./mydata1/стихи.txt', 'r', encoding='windows-1251') as my_file:
    while True:
        text = my_file.readline()
        if not text:
            break
        else:
            str_count += 1
            print(text, end='')
            str_info[str_count] = len(text.split())
            word_amt += str_info[str_count]
print(f'\n\nвсего {str_count} строк в тексте\n')
for n_str, word_count in str_info.items():
    print(f'{"во" if n_str == 2 else "в"} {n_str}й строке {word_count} '
          f'{"слово" if word_count == 1 else "слова" if 1 < word_count < 5 else "слов"}')
print(f'\nвсего {word_amt} слов в тексте')
