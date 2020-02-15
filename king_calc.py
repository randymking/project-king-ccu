



#randy king
#final exam review
#fall 2016

#This program calculates sales tax and total cost based on difference between what the customer pays and what the user is selling for. Customer
#pay price is based on a computer generated number between 15 and 45. The program displays product name,
#selling price, pay price, tax calculated, and total cost.

total_tax = 0
total_cost = 0
COST = 10
UNDER_TAX = .02
OVER_TAX = .03
sale_price = 0
pay_price = 0
sub_total_for_tax = 0
start = 'yes'
product_name = 0
while start == 'yes' or 'Yes':

    import random
    def main():
     # Initialize list of numbers.
        number_list = [0, 0, 0, 0, 0, 0, 0]

    # Assign random numbers to list.
        for i in range(7):
          number_list[i] = random.randint(15, 45)




    product_name =input( "Please enter the name the item to sell: ")
    sale_price = int(input("Please enter a sale price between 20 and 40 dollars: "))
    pay_price = random.randint(15,45)



    if pay_price > sale_price:
         sub_total_for_tax = pay_price - sale_price
         total_tax = sub_total_for_tax * OVER_TAX

    elif pay_price < sale_price:
         sub_total_for_tax = sale_price - pay_price
         total_tax = sub_total_for_tax * UNDER_TAX

    total_cost = total_tax + COST
    print("The item for sale is a "+str(product_name))
    print("The item is selling for:$" + str(sale_price))
    print("The customer paid $"+str(pay_price)+" for the item.")
    print("Total sales tax for the item is:$"+str(total_tax))
    print("Total cost for the item with sales tax is:$" + str(total_cost))

    start = input("If you want to continue, enter yes")


