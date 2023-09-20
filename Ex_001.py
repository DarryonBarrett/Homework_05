def count_vowels(word):
    vowels = "АОУЫЭЯЁЮИЕаоуыэяёюие"
    return sum(1 for char in word if char in vowels)

poem = input("Введите стихотворение Винни-Пуха: ")
phrases = [phrase.split("-") for phrase in poem.split()]
rhythms = [sum(map(count_vowels, phrase)) for phrase in phrases]
if all(rhythm == rhythms[0] for rhythm in rhythms):
    print("Парам пам-пам")
else:
    print("Пам парам")