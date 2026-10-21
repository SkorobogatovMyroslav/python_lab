text = input("Введіть довільний текст: ")

vowels = "аеєиіїоуюяaeiouy"
total_chars = len(text)
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