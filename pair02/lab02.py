n = int(input("N = "))
total = 0
count = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        total += i
        count += 1

print(f"Кількість: {count}")
print(f"Сума: {total}")

if count > 0:
    print(f"Середнє: {total / count:.2f}")
else:
    print("Чисел, кратних 3 або 5, немає.")
  
=================================================================

n = int(input("N = "))
temp = n
count = 0
total = 0
max_digit = -1
min_digit = 10

if temp == 0:
    count = 1
    total = 0
    max_digit = 0
    min_digit = 0
else:
    while temp > 0:
        digit = temp % 10
        count += 1
        total += digit
        
        if digit > max_digit:
            max_digit = digit
        if digit < min_digit:
            min_digit = digit
            
        temp //= 10

print(f"Кількість цифр: {count}")
print(f"Сума цифр: {total}")
print(f"Найбільша цифра: {max_digit}")
print(f"Найменша цифра: {min_digit}")

=================================================================

n = int(input("N = "))
result = []

for i in range(1, n + 1):
    temp = i
    is_valid = True
    
    while temp > 0:
        digit = temp % 10
        if digit != 0 and i % digit != 0:
            is_valid = False
            break
        temp //= 10
        
    if is_valid:
        result.append(i)

print(" ".join(map(str, result)))

==============================================================================

width = int(input("width = "))
height = int(input("height = "))
border = input("контур = ")
inside = input("всередині = ")

if width < 3 or height < 3:
    print("Помилка: мінімальний розмір рамки — 3 × 3.")
else:
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                print(border, end="")
            else:
                print(inside, end="")
        print()
