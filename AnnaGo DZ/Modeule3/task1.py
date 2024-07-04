#Функція, яка розраховує кількість днів між заданою датою і поточною датою. Дата має вводитися в форматі "YYYY.MM.DD".

from datetime import datetime

def get_date_str():
            return input("Enter a date: ")


# get user str date
user_date_str = get_date_str()

def get_days_from_today(user_date_str):
    # get current date
    current_date= datetime.now().date()
    #  convert user str date to datetime
    user_date = datetime.strptime(user_date_str, "%Y.%m.%d").date()
    # return delta between current date and user date
    return (current_date - user_date)

print(get_days_from_today(user_date_str).days)





#Private Notes: #lection time on video "delta" - 00:16:00 and 00:21:20; AND homework 2:38:00