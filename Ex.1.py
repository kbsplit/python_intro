def eur_to_gbp(value, rate):
    print("For ", value, " euros, you'll get ", value * rate, " GBP")


value = int(input("Insert value in Euros: "))
rate = float(input("Insert rate for GBP:"))
eur_to_gbp(value, rate)

