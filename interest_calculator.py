# collect the necessary input: principle, interest, years
# use the formula to work out the program

def interest_calculator(principles, interest, years):
    monthly_interest_rate = interest / 1200
    tenure = years * 12
    monthly_interest_payment = principles * monthly_interest_rate / \
        (1 - (1 + monthly_interest_rate) ** (-tenure))

    print("your Tenure is : ", tenure)
    print("your monthly interest payment is : ", monthly_interest_payment)
    print("")
    print("")


principle = float(input("Enter the principle amount : "))
annual_interest = float(input("Enter the annual interest : "))
years = int(input("Enter the duration in years : "))

interest_calculator(principle, annual_interest, years)
