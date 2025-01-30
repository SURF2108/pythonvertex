#WAP to split the tip of a bill
# input: bill, number of people, tip percentage

bill = int(input("Enter the Total amount on bill: "))
n = int(input("Enter the number of people to split among: "))
t = float(input("Enter percentage of tip: "))

split = ((bill*(t/100))+bill)/n

print("Split on tip: ",split)