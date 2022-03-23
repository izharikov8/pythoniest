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

print('Anything')



