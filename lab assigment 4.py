# Input voltage and resistance
V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (R): "))

# Calculate current
I = V / R

print("Current =", I)

# Check nature of current
if I < 0.5:
    print("Low current")
elif I <= 2:
    print("Normal current")
else:
    print("High current")