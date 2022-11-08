# Task 1
up_time = ["09:00", "11:00", "13:00", "15:00"]  
up_seats = [480, 480, 480, 480]  
up_passengers = [0, 0, 0, 0]  
up_total = [0.0, 0.0, 0.0, 0.0]  

down_time = ["10:00", "12:00", "14:00", "16:00"]  
down_seats = [480, 480, 480, 640]  
down_passengers = [0, 0, 0, 0]  
down_total = [0.0, 0.0, 0.0, 0.0]  


def output_screen():  
    print("\n\t               List of Train Yourney     \n")
    for index in range(0, 4):
        if up_seats[index] != 0:
            print(
                "Journey No:",
                index + 1,
                "| Departure Hour:",
                up_time[index],
                "\t| Tickets available:",
                up_seats[index],
            )
        else:
            print(
                "Journey No:",
                index + 1,
                "| Departure Hour:",
                up_time[index],
                "\t| Closed!",
            )

        if down_seats[index] != 0:
            print(
                "Journey No:",
                index + 1,
                "| Return Hour:",
                down_time[index],
                "\t| Tickets available:",
                down_seats[index],
            )
        else:
            print(
                "Journey No:",
                index + 1,
                "| Return Hour:",
                down_time[index],
                "\t| Closed!",
            )
        print()
        print("------------\n")

output_screen() 

# Task 2
NumOfPassengers = UpTrip = DownTrip = FreeTickets = 0  
OneWayTicket = 25.0  
OneWayCost = 0.0  

choice = input("Do you want to buy ticket? (True/False): ")
while choice != "True" and choice != "False":
    choice = input("Invalid Input! Enter True or False: ")

while choice != "False":
    print("\n-----------------------\n")
    
    UpTrip = int(input("Enter Journey number for your chosen departure hour: ")) - 1
    while UpTrip not in range(0, 4):
        UpTrip = int(input("Error! Enter Journey number from (1, 2, 3, 4): ")) - 1
    
    print("\n      Return Hours Available      \n")
    for num in range(UpTrip, 4):
        print(
            "Journey No:",
            num + 1,
            " | Return Hour:",
            down_time[num],
            " | Remaining Tickets:",
            down_seats[num],
        )
    print()
    DownTrip = int(input("Enter Journey number for your chosen Return hour: ")) - 1
    while DownTrip < UpTrip or DownTrip > 3:
        DownTrip = (
            int(input("Error! Enter Journey number from the given list above: ")) - 1
        )
    
    print()
    NumOfPassengers = int(input("Enter number of passengers for trip: "))
    while NumOfPassengers <= 0:
        NumOfPassengers = int(input("Error! Enter number greater than 0: "))

    if NumOfPassengers > up_seats[UpTrip] or NumOfPassengers > down_seats[DownTrip]:
        print("\n####################\n")
        print("Seats not available for chosen hours")
        print("Please check the display below for available Seats =>")

    else:
        print("\n//// Seats Booked ////")
        if NumOfPassengers >= 10 and NumOfPassengers <= 80:
            FreeTickets = NumOfPassengers // 10
        else:
            FreeTickets = 0
        OneWayCost = (NumOfPassengers - FreeTickets) * OneWayTicket
        print("Total price for two-way journey: $", OneWayCost * 2, sep="")
        
        up_passengers[UpTrip] = up_passengers[UpTrip] + NumOfPassengers
        up_seats[UpTrip] = up_seats[UpTrip] - NumOfPassengers
        up_total[UpTrip] = up_total[UpTrip] + OneWayCost
        
        down_passengers[DownTrip] = down_passengers[DownTrip] + NumOfPassengers
        down_seats[DownTrip] = down_seats[DownTrip] - NumOfPassengers
        down_total[DownTrip] = down_total[DownTrip] + OneWayCost

    ScreenDisplay()  
    print("Do you want to buy ticket(s)? Enter True or False")
    choice = input()
    while choice != "True" and choice != "False":
        choice = input("Invalid Input! Enter True or False: ")

# Task 3
TotalAmount = 0.0 
TotalPassengers = 0 
MaxTrain = ""  
MostPassengers = 0  


print("\n")
print(" ------ END OF THE DAY ------ ")
print("\n")
for counti in range(0, 4):
    print(
        "Journey No:",
        counti + 1,
        "\t| Departure Hour:",
        up_time[counti],
        "\t| Number of passengers:",
        up_passengers[counti],
        "\t| Total money: $",
        up_total[counti],
        sep="",
    )
    print(
        "Journey No:",
        counti + 1,
        "\t| Return Hour:",
        down_time[counti],
        "\t| Number of passengers:",
        down_passengers[counti],
        "\t| Total money: $",
        down_total[counti],
        sep="",
    )
    print("\n-----------------------\n")

for index in range(0, 4):
    TotalPassengers = TotalPassengers + up_passengers[index]
    TotalAmount = TotalAmount + (up_total[index] * 2)
for count in range(0, 4):
    if up_passengers[count] > MostPassengers:
        MostPassengers = up_passengers[count]
        MaxTrain = up_time[count]
    if down_passengers[count] > MostPassengers:
        MostPassengers = down_passengers[count]
        MaxTrain = down_time[count]


print("Total money earned: $", TotalAmount, sep="")
print("Total passengers travelled:", TotalPassengers)
print("The train journey with the highest number of passengers:", MaxTrain)
input("Press Enter to Exit!")

