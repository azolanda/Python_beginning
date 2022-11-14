# Напишите программу, удаляющую из текста все слова, содержащие "абв".

from colorama import init, Fore

init(autoreset=True)

text = 'абв зеленый абвход три хр тр трабвбр пр учитьабв'

print(Fore.BLUE + f'Исходный текст:\n--> {text}')

final_text = ' '.join(
    list(filter(lambda x: not 'абв' in x, list(text.split()))))

print(Fore.GREEN +
      f'Текст после удаления слов, содержащих "абв":\n--> {final_text}')
