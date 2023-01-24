shares = 2000
price_per_share = 50.75
amount_paid = shares * price_per_share
print("Amount paid for the stock: $" + str(amount_paid))
shares = 2000
price_per_share = 40.00
commission_rate = 0.03
amount_paid = shares * price_per_share
commission = amount_paid * commission_rate
print("Commission paid on the purchase: $" + str(commission))
shares = 2000
price_per_share = 40.00
commission_rate = 0.03
amount_paid = shares * price_per_share
commission = amount_paid * commission_rate
total_amount = amount_paid + commission
print("Amount the stock sold for: $" + str(total_amount))
shares = 2000
selling_price_per_share = 42.75
commission_rate = 0.03
selling_amount = shares * selling_price_per_share
commission = selling_amount * commission_rate
total_amount = selling_amount - commission
print("Commission paid on the sale: $" + str(commission))
print("Total amount received for the stock: $" + str(total_amount))
