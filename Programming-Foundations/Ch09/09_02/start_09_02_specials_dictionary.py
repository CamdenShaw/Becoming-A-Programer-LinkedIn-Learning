""" I'll Have the Special! """
from datetime import date

specials = {'Sunday'    : 'spinach', 
            'Monday'    : 'mushroom', 
            'Tuesday'   : 'pepperoni', 
            'Wednesday' : 'veggie',
            'Thursday'  : 'bbq chicken',
            'Friday'    : 'sausage',
            'Saturday'  : 'Hawaiian'}

def order(day):
    pizza = specials[day]
    print('Order the {} pizza.'.format(pizza))

print(order('Saturday'))

#Experiments
# making the program less reliant on user input
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
today = weekday[date.today().weekday()]
print(order(today))

def order(day = today):
    pizza = specials[day]
    print('Order the {} pizza'.format(pizza))
