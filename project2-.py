 
customer_code = input("Enter customer code (R, C, or I): ").upper() #Prompts the user for the customer's code
while customer_code != 'R' and customer_code != 'I' and customer_code != 'C':
    print('Invalid input, please enter R, C, or I: ')
    customer_code = input("Enter customer code (R, C, or I): ").upper() #Prompts the user for the customer's code
beginning_reading = int(input("Enter beginning reading (between 0 and 999999999): "))
ending_reading = int(input("Enter ending reading (between 0 and 999999999): ")) 

while beginning_reading < 0 or beginning_reading > 999999999:
    print('out of range. ')
    beginning_reading = int(input("Enter beginning reading (between 0 and 999999999): "))
    ending_reading = int(input("Enter ending reading (between 0 and 999999999): ")) 
gallons_used = (ending_reading - beginning_reading) / 10.0
#Checks if the meter readings are valid
#Calculates the gallons of water used
        
#Calculates the amount to be billed
if customer_code == 'R':
    amount_billed = 5.00 + 0.0005 * gallons_used
if customer_code == 'C':
    if gallons_used <= 4000000:
                amount_billed = 1000.00
    else:
        amount_billed = 1000.00 + 0.00025 * (gallons_used - 4000000)
if customer_code == 'I':
    if gallons_used <= 4000000:
        amount_billed = 1000.00
    if gallons_used <= 10000000:
        amount_billed = 2000.00
    else:
        amount_billed = 2000.00 + 0.00025 * (gallons_used - 10000000)
        
print(f"Customer Code: {customer_code}")
print(f"Beginning Meter Reading: {beginning_reading}")
print(f"Ending Meter Reading: {ending_reading}")
print(f"Gallons Used: {gallons_used:.2f}")
print(f"Amount Billed: ${amount_billed:.2f}")#This shows the summary
