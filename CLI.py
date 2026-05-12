from forex_python.converter import CurrencyRates

c = CurrencyRates()

print("========================================================================================================================")
print("             WELCOME TO CLI BASED CURRENCY CONVERSION                               ")
print("========================================================================================================================")
print("Please see our currency code list to know about country names and codes")
print()

flag = True
while flag:
    print("Enter Source Currency Country Code : ")
    source = input()
    print("Enter Destination Currency Country Code : ")
    dest = input()
    print("Enter Amount to Convert : ")
    amount = input()
    status = 0
    try:
        amount = float(amount)
    except Exception:
        status = 1
        print("You entered invalid amount")
        pass
    if status == 0:
        try:
            rate = c.get_rate(source, dest)
            output = rate * amount
            output = source+" Current Rate = "+str(rate)+"\nTotal amount you receive after conversion : "+str(round(output, 3))
        except Exception:
            output = "Sorry Given Source Currency is not Ready"
            pass
        print()
        print(output)
    print()
    print("Do you wish to continue Y or N : ")
    option = input()
    if option.strip() == "N" or option.strip() == "n":
        print("Bye")
        flag = False

