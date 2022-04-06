FloorPrice = input("Please enter the current floor price: ")
MintPrice = input("Please enter the mint price: ")
Quantity = input("Please enter the quantity: ")
GasLimit = input("Please enter the gas limit: ")
MaxBaseFee = 100
PriorityFee = 100


print("---------------------------------------------------------------------")
print("| Max Base Fee | Priority | Total Cost | Average Cost | Profit/Loss |")
print("---------------------------------------------------------------------")

while MaxBaseFee <= 10000:
    TotalCost = (float(MintPrice) * float(Quantity)) + ((int(GasLimit) * (int(MaxBaseFee) + int(PriorityFee))) / 1000000000)
    AverageCost = TotalCost / float(Quantity)
    ProfitOrLoss = float(FloorPrice) - AverageCost

    print("      " + str(MaxBaseFee) + "      |    " + str(PriorityFee) + "   |    " + str(round(TotalCost, 3))
          + "    |     " + str(round(AverageCost, 3)) + "     |     " + str(round(ProfitOrLoss, 3)))
    print("---------------------------------------------------------------------")

    MaxBaseFee += 100
    PriorityFee += 100

KeyPress = input("\nPress any key to exit...")
exit()

