total_bill = float(input("What was the total bill? "))  #input returns strings, have to convert them to int or float
tip = int(input(" How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
cost_per_person = (total_bill + (total_bill * (tip / 100)))/ number_of_people

print (f"Each person should pay: {cost_per_person: .2f}") #:.2f rounds the output to 2 decimal places