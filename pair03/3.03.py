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