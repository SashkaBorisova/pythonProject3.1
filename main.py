flag = True
while flag:
    str = input("Введите строку ")  # запрос пользователя на ввод строки
    a = str.split()
    if len(a) == 0:
        print("Вы ввели только пробелы")
    else:
        flag = False
word_length = input("Введите длину слова ")  # запрос пользователя на ввод длины
words_of_length = []  # создаём пустой список, в который будут добавляться слова заданной длины
if not word_length.isdigit():  # проверка на числовое значение
    print(
        "Введена некорректная длина слова. Введите целое число")  # в случае ошибки, программа выводит сообщение и просит ввести число снова
    word_length = input("Введите длину слова ")
if not str:
    print("Вы не ввели строку. Попробуйте снова.")
word_length = int(word_length)
w = str.split()
count = 0
for word in w:
    cleaned_word = ''.join(c for c in word if c.isalnum())
    if len(cleaned_word) == word_length:
        count += 1
        words_of_length.append(cleaned_word)
print(f"Количество слов длины {word_length}: {count}")
print(words_of_length)

# Вложенный цикл для сортировки с использованием ASCII кодов
for i in range(len(words_of_length)):
    for j in range(i + 1, len(words_of_length)):
        if (ord(words_of_length[i][0]), words_of_length[i]) > (ord(words_of_length[j][0]), words_of_length[j]):
            words_of_length[i], words_of_length[j] = words_of_length[j], words_of_length[i]

print(words_of_length)
# Ввести строку, подсчитать количество слов заданной длины.
# Доп:вывести все слова заданной длины, отсортированные по возрастанию ( ascii code).
