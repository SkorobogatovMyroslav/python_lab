letters = digits = spaces = vowel_count = 0

for char in text.lower():
    if char.isalpha():
        letters += 1
    if char.isdigit():
        digits += 1
    if char == " ":
        spaces += 1
    if char in vowels:
        vowel_count += 1

words = len(text.split())

print(f"Символів: {total_chars}")
print(f"Літер: {letters}")
print(f"Цифр: {digits}")
print(f"Пробілів: {spaces}")
print(f"Голосних: {vowel_count}")
print(f"Слів: {words}")

===========================================================

full_name = input("Введіть ПІБ (прізвище ім'я по батькові): ")
parts = full_name.split()

if len(parts) == 3:
    surname = parts[0].capitalize()
    name_initial = parts[1][0].upper() + "."
    patronymic_initial = parts[2][0].upper() + "."
    print(f"{surname} {name_initial}{patronymic_initial}")
else:
    print("Помилка: потрібно ввести рівно три частини.")

==========================================================================

text1 = input("Перший рядок: ")
text2 = input("Другий рядок: ")

a = text1.lower().replace(" ", "")
b = text2.lower().replace(" ", "")

print(f"Нормалізований перший рядок:  '{a}'")
print(f"Нормалізований другий рядок:  '{b}'")

if sorted(a) == sorted(b):
    print("Рядки є анаграмами.")
else:
    print("Рядки не є анаграмами.")

================================================================

sentence = input("Введіть речення: ")
words = sentence.split()

if not words:
    print("Речення порожнє.")
else:
    max_len = max(len(w) for w in words)
    min_len = min(len(w) for w in words)

    longest_words = [w for w in words if len(w) == max_len]
    shortest_words = [w for w in words if len(w) == min_len]
    unique_words = {w.lower() for w in words}

    print("Найдовші:", ", ".join(longest_words))
    print("Найкоротші:", ", ".join(shortest_words))
    print("Унікальних слів:", len(unique_words))

    old_word = input("Слово для заміни: ")
    new_word = input("Нове слово: ")

    replaced = " ".join(new_word if w.lower() == old_word.lower() else w for w in words)
    print("Після заміни:", replaced)

================================
