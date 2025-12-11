text = input('Matn kiriting:')
word = input('Qaysi so\'z bilan boshlanishini tekshirish:')

if text.startswith(word):
    print('True')
else:
    print('False')