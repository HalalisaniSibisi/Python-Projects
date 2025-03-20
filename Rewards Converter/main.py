print('Welcome to the Credit Card Rewards Converter!')
    
def rewards_converter():
    
    
    airline_per_miles = 0.1
    while True:
        try:
        
            customer_input = input('Please enter a cash value to convert to airline miles:R  ')

            if customer_input.lower() == 'exit':
                print('Thank you for using the Credit Card Rewards Converter. Goodbye!')
                break


            customer_input = float(customer_input)
            cashValue = customer_input * airline_per_miles
        
            print(f'Converting your money in R{customer_input} is worth {cashValue:.2f} in miles')

        except ValueError:
            print('Invalid input! Please enter a numerical value or type "exit" to quit.')

rewards_converter()



