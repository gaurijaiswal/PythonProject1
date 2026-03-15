# Vendor Details
name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

# Monthly Purchases
print("\nEnter purchase amount for each month:")

months = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

total = 0

for m in months:
    amount = float(input(f"{m}: "))
    total = total + amount

# Annual Report
print("\n------ Annual Purchase Billing Report ------")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Total Annual Purchase Amount:", total)