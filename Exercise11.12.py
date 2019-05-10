#11
# zero_to_hundred = range(101)
# for num in zero_to_hundred:
#     if num % 3 == 0 and num % 5 == 0:
#         print('BitMaker')
#     if num % 3 == 0:
#         print('Bit')
#     if num % 5 == 0:
#         print('Maker')
#     else:
#         print(num)
#12

def pizzamaker ():
    customer_order = int(input('How many pizzas do you want?'))
    quantity = range(1, customer_order + 1)

    for pizza in quantity:
        print(f"How many toppings for pizza{pizza}?")
        topping_number = int(input())
        print(f"You have ordered a pizza with {topping_number} toppings")

pizzamaker()
