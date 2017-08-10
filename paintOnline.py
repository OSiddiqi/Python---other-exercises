RoomWidth = 0
RoomHeight = 0
RoomTotal = 0
RoomPaint = 0

RoomWidth = float(input("Enter the room width, it must be between 1m-25m: "))
RoomHeight = float(input("Enter the room height, it must be between 2m-6m: ")) 
if ((RoomWidth <=25 and RoomWidth >=1) and (RoomHeight <=6 and RoomHeight >=2)): 

    RoomTotal = ((RoomWidth * RoomHeight)*4)

    PaintSelection = str (input("Please choose from a selection of paints: 'DuluxourousPaints', 'AverageJoes', or 'CheapoMax'."))
    if PaintSelection == "DuluxourousPaints":
        RoomPaint = RoomTotal * 1.50
    elif PaintSelection == "AverageJoes" :
        RoomPaint = RoomTotal * 1.00
    elif PaintSelection == "CheapoMax" :
        RoomPaint = RoomTotal * 0.45    

    TotalCost = RoomPaint
    print ("The total cost of painting this room is £",TotalCost)

else:
    print ("Invalid input. Please try again, you numpty.")