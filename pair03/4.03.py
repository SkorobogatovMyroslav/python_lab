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