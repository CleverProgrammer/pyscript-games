# from datetime import datetime
from playsound import playsound

# now = datetime.now()
# now.strftime("%m/%d/%Y, %H:%M:%S")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([number * 2 for number in numbers])
# print([number for number in numbers if number % 2 != 0])

def replaceFruit(div_id, item):
  
  pyscript.write(div_id, item)
  print('✅ success, dom manipulated! 💪')
  playsound('ding.mp3')
  console.log('✅ success, dom manipulated! 💪')

# replaceAllFruits(['fruit-1', 'fruit-2', 'fruit-3'], ['🍓', '🍌', '🍊'])
def replaceAllFruits(div_ids, fruits):
  for id, fruit in zip(div_ids, fruits):
    print(f'div id: {id} fruit: {fruit}')
  # pyscript.write()

def show_fruit(*args, **kwargs):
  print('hi')
  print('-----------')
  print(dir(args))
  print(args[0])
  print('-----------')
  pyscript.write('fruit-1', '🍓')
  playsound('ding.mp3')

# from random import choice

# async def things():
#   for i in range(3):
#     print('hi')
#     await replaceFruit(f'fruit-{i+1}', choice('🍓 🫐 🍊 🍑 🍌 🥝'.split()))

## things()