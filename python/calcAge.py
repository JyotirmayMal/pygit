#calculate your current age
import datetime

current_datetime = datetime.datetime.now()
current_year = current_datetime.year

birth_year = input("Enter your birth year : ")
age =  current_year - int(birth_year)
print(age)