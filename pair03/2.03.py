full_name = input("Введіть ПІБ (прізвище ім'я по батькові): ")
parts = full_name.split()

if len(parts) == 3:
    surname = parts[0].capitalize()
    name_initial = parts[1][0].upper() + "."
    patronymic_initial = parts[2][0].upper() + "."
    print(f"{surname} {name_initial}{patronymic_initial}")
else:
    print("Помилка: потрібно ввести рівно три частини.")