Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # PY-46 Zharikov Ivan
# Task 3

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'еда',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'курс по гитхаб',
    'как стать программистом'
    ]

data = {}

for search in queries:
  words = search.split()
  words_qty = len(words)
  if words_qty in data.keys():
    data[words_qty] += 1
  else:
    data.update({words_qty: 1})

for key, value in data.items():
  percentage = ((value / len(queries) * 100))
  print(f'Поисковых запросов состоящих из {key} слова: {percentage}%')
print()

print("Напечатай комит")

