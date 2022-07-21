from random import choice

async def replaceFruit(div_id, fruit):
  
  pyscript.write(div_id, fruit)
  print('✅ success, dom manipulated! 💪')
  # playsound('ding.mp3')
  console.log('✅ success, dom manipulated! 💪')
  
def replaceAllFruits():
  for fruit in document.querySelectorAll('.fruit'):
    pyscript.write(fruit.id, choice('🍓 🫐 🍊 🍑 🍌 🥝'.split()))

def on_click_change_fruit_1(event):
  pyscript.write('fruit-1', choice('🍓 🫐 🍊 🍑 🍌 🥝'.split()))

def on_click_change_fruit_2(event):
  pyscript.write('fruit-2', choice('🍓 🫐 🍊 🍑 🍌 🥝'.split()))

def on_click_change_fruit_3(event):
  pyscript.write('fruit-3', choice('🍓 🫐 🍊 🍑 🍌 🥝'.split()))

# from random import choice

# async def things():
#   for i in range(3):
#     print('hi')
#     await replaceFruit(f'fruit-{i+1}', choice('🍓 🫐 🍊 🍑 🍌 🥝'.split()))

## things()