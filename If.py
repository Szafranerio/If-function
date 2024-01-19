brands = ['apple', 'bmw', 'lg', 'sony', 'audi']

for brand in brands:
    if brand == 'sony': 
        print(brand.upper())  #If there is 'sony' in the list it will be printed with capital letters only, rest of list only first letter is big
    else:
        print(brand.title())
#Apple
#Bmw
#Lg
#SONY
        
# == means equal != not equal 
        
pizza_toppings = 'tomato'
if pizza_toppings != 'potato':
    print('Please add potatos')
#Please add potatos
    
age = 17 

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
#You cannot vote. User is under 18 and he cannot vote.
    
age = 19

if age < 5:
    print("Ticket cost 10 euro")
elif age < 18:
    print("Ticket cost 15 euro")
else:
    print("Tickect cost 100 euro")
#Tickect cost 100 euro
    
age = 56

if age < 5:
    print("Ticket cost 10 euro")
elif age < 18:
    print("Ticket cost 15 euro")
elif age < 60:
    print("Ticket cost 5 euro")
else:
    print("Tickect cost 100 euro")
# Ticket cost 5 euro
    
#In some cases there are no need to use else, command elif can take over 
    
age = 62

if age < 5:
    print("Ticket cost 10 euro")
elif age < 18:
    print("Ticket cost 15 euro")
elif age < 60:
    print("Ticket cost 5 euro")
elif age > 61:
    print("Tickect cost 1 euro")
#Tickect cost 1 euro
    
toppings = ['ham', 'tomato', 'pasta']
for topping in toppings:
    if topping == 'pasta':
        print('There is no pasta')
    else:
        print(f'Added {topping}.')
print('\nYour dish is ready ')
#Added ham.
#Added tomato.
#There is no pasta

#Your dish is ready 

users = ['admin', 'tom', 'eric', 'paul']
for user in users:
    if user == 'admin':
        print(f'\nHello {user.title()}, do you wnat to see the monthly report')
    else:
        print(f'Hello {user.title()}')

#Hello Admin, do you wnat to see the monthly report
#Hello Tom
#Hello Eric
#Hello Paul
