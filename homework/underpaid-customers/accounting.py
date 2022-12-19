# To Do
# Read through accounting.py and understand what it does. x

#create a global variable for the price of the melons X
    #MELON_PRICE = 1.00


# Create a function that takes in a text file of customer orders and parses it to produce similar output.
    #name the function something that makes sense - def customer-melon-payment(payment-information-filename): x
    #open the customer-orders file open()
        #save to a variable -- call it melon-payment-data
        #melon-payment-data = open(payment-information-filename) x
    #for in loop through the payment-information-filename to access each line
        #for line in melon-payment-data:

            #DATA INFORMATION
            #trim the lines and parse through on the | and save to a descriptive variable, call it "order" X
                #order = line.rstrip().split("|")
            
            #CUSTOMER INFORMATION
            #access customer full names (found at index 1) and create a variable to hold their name. x
                #Split on the space btwn first and last (split will create a new list with the first and last name as separate indexes)
                    #customer_name = order[1]
            
            #create a variable for the first name of customer x
                #first_name = customer_name.split(" ")[0]
            
            #TRANSACTION INFORMATION
            #access the 3rd index to get the amount paid and create a variable to hold that information. x
                #change the type into an integer
                    #customer_amount_paid = int(order[3])
            
            #access the 2nd index to get the quantity of melons bought and create a variable to hold that information x
                #change the type into an integer
                    #how_many_melons = int(order[2])

            #EXPECTED AMOUNT PAID
            #create a variable to hold the quantity of melons multiplied by the cost of the melon and call it the expected price x
                #expected_price_paid = how_many_melons * MELON_PRICE
            
            #PAYMENT FEEDBACK
            #print the payment information including how much the customer actually paid and how much was expected. x
                #use an f string
                #trim the decimals to 2 places using :.2f
                    #print(f"{customer_name} paid ${customer_amount_paid}, expected amount was" f"{expected_price_paid:.2f}")
            
            
            #create some logic for what to print in case the customer over paid or if they underpaid x
                #if expected_price_paid < customer_amount_paid:
                    #print(f"{first_name} paid too much for their melons! They will need a refund.") --> could go on to say how much of a refund
                #elif expected_price_paid > customer_amount_paid:
                    #print(f"{first_name} paid too little for their melons! They will need to be hunted down for the amount they owe use.)


            #close the file x
                #melon-payment-data.close()

        #call the function to actually use it customer-melon-payment()

MELON_PRICE = 1.00

def customer_melon_payment(payment-information-filename):
    melon_payment_data = open(payment-information-filename)

    for line in melon_payment_data:
        #parse the data to access each line and clean it
        order = line.rstrip().split("|")
        #customer information
        customer_name = order[1]
        first_name = customer_name.split(" ")[0]
        #transaction information
        customer_amount_paid = int(order[3])
        how_many_melons = int(order[2])
        #expected amount paid 
        expected_price_paid = how_many_melons * MELON_PRICE
        #payment feedback
        print(f"{customer_name} paid ${customer_amount_paid}, expected amount was" f"{expected_price_paid:.2f}")
        #who paid too much and who paid too little feedback

        if expected_price_paid < customer_amount_paid:
            print(f"{first_name} paid too much for their melons! They will need a refund.")
       
        elif expected_price_paid > customer_amount_paid:
            print(f"{first_name} paid too little for their melons! They will need to be hunted down for the amount they owe use.")

    melon_payment_data.close()


customer_melon_payment()









# Add comments explaining what your code does.

# Read over our solution and compare it to your own.


#cost of a melon
melon_cost = 1.00

#transation informatio including customer name, number of melons purchased and dollars paid
customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

customer1_expected = customer1_melons * melon_cost
#create a variable that holds how much it was expected that customer 1 would pay
    #which is how many melons multiplied by how uch the melons cost
if customer1_expected != customer1_paid:
#if the expected amound is not equal to what the customer actually paid print out "customer name paid how much they paid but expected payment was ___"
    print(f"{customer1_name} paid ${customer1_paid:.2f},",
    #the expected payment was ___ rounded to 2 decimal points
          f"expected ${customer1_expected:.2f}"
          )
#
customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print(f"{customer2_name} paid ${customer2_paid:.2f},",
          f"expected ${customer2_expected:.2f}"
          )

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print(f"{customer3_name} paid ${customer3_paid:.2f},",
          f"expected ${customer3_expected:.2f}"
          )

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print(f"{customer4_name} paid ${customer4_paid:.2f},",
          f"expected ${customer4_expected:.2f}"
          )

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print(f"{customer5_name} paid ${customer5_paid:.2f},",
          f"expected ${customer5_expected:.2f}"
          )

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print(f"{customer6_name} paid ${customer6_paid:.2f},",
          f"expected ${customer6_expected:.2f}"
          )
