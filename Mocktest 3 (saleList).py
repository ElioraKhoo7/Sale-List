# Part A
dateList = []
timeList = []
nameList = []
saleList = []
qtyList  = []

staffName = input("Please enter your full name: ")
staffID = input("Please enter your staff ID: ")

# Part B
while True:
    dateInput = input("Please enter date of sales: ")
    timeInput = input("Please enter time of sales:")
    nameInput = input("Please enter product name: ")
    saleInput = float(input("Please enter sale amount: "))
    
    dateList.append(dateInput)
    timeList.append(timeInput)
    nameList.append(nameInput)
    saleList.append(saleInput)
    
    c = input("Do you want to enter another claim? [y/n]")
    if(c == "n"):
        break

# Part C
print(f"Staff Name: {staffName}")
print(f"Staff ID: {staffID}")

total = 0
for i in range(len(saleList)):
    #total += saleLis[i]*qtyList[i]
    total += saleList[i]
    
#total = sum(saleList)
Average = total / len(saleList)
highSale = max(saleList)

indexHighsale = saleList.index(highSale)
highSaleProduct = nameList[indexHighsale]
print(f"Total sales amount: {total}")

print(f"Highest sales product: {highSaleProduct}")
print(f"Highest sales amount: {highSale}")
