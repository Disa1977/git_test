rate_as_str = input('Оцените работу оператора от 1 до 5:')
rate = int(rate_as_str)

if(rate< 1 ):
    rate = 1

if(rate > 5):
    rate = 5

feedback = ''

if rate == 1:
    feedback = input('Почему:')
elif rate == 2:
    feedback = input('Раскажи:')
elif rate == 3:
    feedback = input('Поясни:')
elif rate == 4:
    feedback = input('За базар:')
else:
    feedback = input('И...:')

print(feedback)