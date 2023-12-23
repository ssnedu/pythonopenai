"""
Mutli line comments
Press double/single quotes and
type enter after 3 quotes
this will be multi line comment
"""
#this is a single line comment

deposit = 50
item_price = 15
taxpercent = 3
balance = deposit - item_price - (item_price*(taxpercent/100))
print(balance)

#String format
print("bank balance is $",balance)
credit = input("enter the amount")
balance += int(credit)
print("new balance is",balance)