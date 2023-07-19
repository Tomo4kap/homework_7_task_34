import re

# Ввод стихотворения
poem = input("Введите стихотворение: ")

# Разбить стихотворение на фразы
phrases = poem.split()

# Первая фраза
prev_num_vowels = len(re.findall(r"[aeiouAEIOU]", phrases[0]))

# Проверить ритм для каждой фразы
for phrase in phrases[1:]:
    num_vowels = len(re.findall(r"[aeiouAEIOU]", phrase))
    if num_vowels != prev_num_vowels:
        print("Пам парам")
        break
    prev_num_vowels = num_vowels
else:
    print("Парам пам-пам")

