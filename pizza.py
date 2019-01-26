from datetime import datetime as dt


class Pizza:

    def get_price(self):
        return self.price

    def get_ingred(self):
        return self.ingred

    def extra_ing(self):
        return self.extra

    def get_size(self):
        return self.size

    def __str__(self):
        ingr = str(self.get_ingred()).replace('[', '').replace(']', '').replace('\'', '')
        ext = str(self.extra_ing()).replace('[', '').replace(']', '').replace('\'', '')
        return '\n\nYour Pizza:\nSize:' + str(self.get_size()) + '\nIngredients: ' + ingr + '\nExtra ingredients: ' + ext\
               + ('\nTotal Price = %.2f$' % self.get_price())


class MondayPizza(Pizza):
    pizza_of_the_day = 'Today\'s pizza is Hawaiian pizza. Ingredients:' \
                       '\nTomato Souse, Parmezan, Pineapples, Chicken, Corn, Mozarella.'
    ingred = ['Tomato Souse', 'Parmezan', 'Pineapples', 'Chicken', 'Corn', 'Mozarella']
    extra = []
    price = 15.25
    size = ''


class TuesdayPizza(Pizza):
    pizza_of_the_day = 'Today\'s pizza is Vegetable pizza.Ingredients:' \
                       '\nBase, Tomato Souse, Parmezan, Olives, Mushrooms, Pepper, Corn, Mozarella.'

    ingred = ['Tomato Souse', 'Parmezan', 'Olives', 'Mushrooms', 'Pepper', 'Corn', 'Mozarella']
    extra = []
    price = 7.00
    size = ''


class WednesdayPizza(Pizza):
    pizza_of_the_day = 'Today\'s pizza is 4 cheese pizza.Ingredients:' \
                       '\nTomato Souse, Parmezan, Mozarella, Dor Blue, Rockfor, Feta.'

    ingred = ['Tomato Souse', 'Parmezan', 'Mozarella', 'Dor Blue', 'Rockfor', 'Feta']
    extra = []
    price = 25.00
    size = ''


class ThursdayPizza(Pizza):
    pizza_of_the_day = 'Today\'s pizza is Fodja pizza.Ingredients:' \
                       '\nTomato Souse, Parmezan, Beckon, Olives, Mushrooms, Chicken, Pepper'

    ingred = ['Tomato Souse', 'Parmezan', 'Beckon', 'Olives', 'Mushrooms', 'Chicken', 'Pepper']
    extra = []
    price = 20.50
    size = ''


class FridayPizza(Pizza):
    pizza_of_the_day = 'Today\'s pizza is meat pizza. Ingredients:' \
                       '\nBase, Tomato Souse, Parmezan, Beckon, Chiken, Salami, Hunting Sausages'

    ingred = ['Tomato Souse', 'Parmezan', 'Beckon', 'Chicken', 'Salami', 'Hunting Sausages']
    extra = []
    cost = 21.75
    size = ''


class SaturdayPizza(Pizza):
    pizza_of_the_day = 'Today\'s pizza is BBQ pizza. Ingredients:' \
                       '\nBase, Tomato Souse, Parmezan, Beckon, Pepper, Rockfor, Corn, Hunting Sausages'

    ingred = ['Tomato Souse', 'Parmezan', 'Beckon', 'Pepper', 'Rockfor', 'Corn', 'Hunting Sausages']
    extra = []
    price = 19.25
    size = ''


class SundayPizza(Pizza):
    pizza_of_the_day = 'Today\'s pizza is americana pizza. Ingredients:' \
                       '\nBase, Tomato Souse, Parmezan, Beckon, Pepper, Rockfor, Corn, Chicken.'
    ingred = ['Tomato Souse', 'Parmezan', 'Beckon', 'Pepper', 'Rockfor', 'Corn', 'Chicken']
    extra = []
    price = 15.50
    size = ''


class Decorator(Pizza):
    def __init__(self, extra_comp):
        self.component = extra_comp

    def get_ingred(self):
        return self.component.get_ingred()

    def extra_ing(self):
        return self.component.extra_ing() + Pizza.extra_ing(self)

    def get_price(self):
        return self.component.get_price() + Pizza.get_price(self)

    def get_size(self):
        return self.component.get_size()


class TomatoSouse(Decorator):
    price = 2
    extra = ['Tomato Souse']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Parmezan(Decorator):
    price = 4
    extra = ['Parmezan']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Pineapples(Decorator):
    price = 5
    extra = ['Pineapples']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Beckon(Decorator):
    price = 5.50
    extra = ['Beckon']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Olives(Decorator):
    price = 4.25
    extra = ['Olives']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Chicken(Decorator):
    price = 3.75
    extra = ['Chicken']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Mushrooms(Decorator):
    price = 2.75
    extra = ['Mushrooms']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class HuntingSausages(Decorator):
    price = 5
    extra = ['Hunting Sausages']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Pepper(Decorator):
    price = 2.75
    extra = ['Pepper']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Corn(Decorator):
    price = 2.75
    extra = ['Corn']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Salami(Decorator):
    price = 6
    extra = ['Salami']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Mozarella(Decorator):
    price = 5.75
    extra = ['Mozarella']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class DorBlue(Decorator):
    price = 10
    extra = ['DorBlue']

    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class DecoratorSize(Pizza):

    def __init__(self, size, pizza):
        self.size = size
        self.pizza = pizza

    def get_price(self):
        return self.price + self.pizza.get_price()

    def get_size(self):
        return self.pizza.get_size() + self.size

    def get_ingred(self):
        return self.pizza.get_ingred()

    def extra_ing(self):
        return self.pizza.extra_ing()


class Small(DecoratorSize):
    price = 10

    def __init__(self, pizza):
        size = 'Small'
        DecoratorSize.__init__(self, size, pizza)


class Medium(DecoratorSize):
    price = 20

    def __init__(self, pizza):
        size = 'Medium'
        DecoratorSize.__init__(self, size, pizza)


class Large(DecoratorSize):
    price = 30

    def __init__(self, pizza):
        size = 'Large'
        DecoratorSize.__init__(self, size, pizza)


def creatting_pizza(Pizza_of_day):
    print(Pizza_of_day.pizza_of_the_day)
    print('\n\nDo you want to add something?')
    if input('Enter eny key to add one more ingredient, or enter to go next.') == '':
        Pizza_of_day.extra = ['None']
        return Pizza_of_day
    print('\nAdditional ingredients:'
          '\nTomato Souse, Parmezan, Pineapples, Beckon, Olives, Mushrooms, Hunting Sausages, Chicken, Pepper, '
          'Salami, Corn, Mozarella, DorBlue.\n')

    while True:
        while True:
            try:
                key = input('Additional ingredient: ').title()
                if key not in ('Tomato Souse, Parmezan, Pineapples, Beckon, Olives, Mushrooms, Hunting Sausages, '
                               'Chicken, Pepper, Salami, Corn, Mozarella, Dorblue').split(', '):
                    raise Warning('There is no such ingredient. Maybe error in name of ingredient.')
                break
            except Warning:
                print('There is no such ingredient. Maybe error in name of ingredient. Try again. \n')

        dict = {'Tomato Souse': TomatoSouse(Pizza_of_day), 'Parmezan': Parmezan(Pizza_of_day),
                'Pineapples': Pineapples(Pizza_of_day), 'Beckon': Beckon(Pizza_of_day), 'Olives': Olives(Pizza_of_day),
                'Mushrooms': Mushrooms(Pizza_of_day), 'Hunting Sausages': HuntingSausages(Pizza_of_day),
                'Chicken': Chicken(Pizza_of_day), 'Pepper': Pepper(Pizza_of_day), 'Salami': Salami(Pizza_of_day),
                'Corn': Corn(Pizza_of_day), 'Mozarella': Mozarella(Pizza_of_day), 'Dorblue': DorBlue(Pizza_of_day)}
        Pizza_of_day = dict[key]

        if input('\nSomething else? Enter eny key to add one more ingredient, or enter to go next.') == '':
            return Pizza_of_day


def choosing_pizza_of_the_day():
    day = dt.weekday(dt.today())
    days_pizza = {0: MondayPizza(), 1: TuesdayPizza(), 2: WednesdayPizza(), 3: ThursdayPizza(), 4: FridayPizza(),
                  5: SaturdayPizza(), 6: SundayPizza()}
    return days_pizza[day]


def choosing_size(pizza):
    while True:
        try:
            inp = input('\n\nSize of pizza?\n-Small - 25cm\n-Medium - 30cm\n-Large - 35cm\n').title()
            if inp not in ['Small', 'Medium', 'Large']:
                raise ValueError
            break
        except ValueError:
            print('Incorrect value. Retry entering')

    decor = {'Small': Small(pizza), 'Medium': Medium(pizza), 'Large': Large(pizza)}
    return decor[inp]


def main():
    some_pizza = creatting_pizza(choosing_pizza_of_the_day())
    print(choosing_size(some_pizza))


if __name__ == '__main__':
    main()
