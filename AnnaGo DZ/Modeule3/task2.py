#  Щоб виграти головний приз лотереї, 
# необхідний збіг кількох номерів на 
# лотерейному квитку з числами, що 
# випали випадковим чином і в певному 
# діапазоні під час чергового тиражу. 
# Наприклад, необхідно вгадати шість 
# чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.
import random


def get_numbers_ticket(min, max, quantity):
    from random import randint
   
    numbers = set()
    for i in range(quantity):
        numbers.add(randint(min, max))
        if max >= 1000:
                print("Please enter a number less than 1000")
        elif min > max:
                print("Error: min > max")
        elif len(numbers) == quantity:
                print("Error: quantity is more than range")
        elif min == max:
                print("Error: min = max") 
        
    return numbers

lottery_numbers = get_numbers_ticket(1, 1002, 8)
print("Ваші лотерейні числа:", lottery_numbers)
