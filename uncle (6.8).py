s = """Мой дядя самых честных правил, Когда не в шутку
занемог, Он уважать себя заставил И лучше выдумать не
мог"""

"""Удалить из стихотворения все слова,
начинающиеся на букву м.
Результат вывести на экран в виде строки."""

"""words  = s.split()
new_words = [word for word in words if not word.startswith('м')]
print(' '.join(new_words))"""


words = s.split()
new_words = []
for word in words:
    if not word.startswith('м'):
        new_words.append(word)
print(' '.join(new_words))

    