name = input('Cual es tu nombre? ')
sales = float(input('Cuanto has vendido este mes? '))

commissions = round(sales * .13, 2)

print(f"Bien {name}, tus comisiones son: {commissions}")