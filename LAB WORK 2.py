"""
    Program Purpose: To ask user to input data and select room type, number of rooms and numbers og nights staying at the hotel.
    Programmer: MUHAMMAD AFIF NAQIUDDIN BIN OTHMAN
    Date: 23 February 2024
"""

# Prompt the user when using the system about the hotel
while True:
    print("Welcome to Smiley Hotel")
    print("New Reservation:")
    print("Room Rates:")
    print("Single: RM100 per night")
    print("Double: RM150 per night")
    print("Suite: RM250 per night")

# Ask the user to input data about the room interested in
    room_type = input("Enter room type (S for Single, D for Double, T for Suite): ").upper()
    num_rooms = int(input("Enter the number of rooms to reserve: "))
    num_nights = int(input("Enter the number of nights to stay: "))

# Validate user input
    if room_type not in ['S', 'D', 'T'] or num_rooms <= 0 or num_nights <= 0:
        print("Error: Invalid room type, number of rooms, or number of nights. Please try again.")
        continue

# Define rates, discounts, and minimum stay requirements
    rates = {"S": 100, "D": 150, "T": 250}
    discounts = {True: 0.9, False: 1}
    min_stay = {"T": 3}

# Calculate total cost
    rate = rates.get(room_type)
    if not rate:
        print("Error: Invalid room type.")
        continue

    if room_type == "T" and num_nights < min_stay[room_type]:
        print(f"Error: Minimum stay for a Suite is {min_stay[room_type]} nights.")
        continue

    discount = discounts[num_rooms > 5]
    cost = rate * num_nights * num_rooms * discount

# Condition if the user input meet the requirement
    if room_type == "S" and num_nights > 7:
        print("Congratulations! You get a complimentary breakfast voucher.")

# Prompt user if they get discount
    discount_msg = "You are eligible for a 10% discount on the total cost!" if discount < 1 else ""
    print(discount_msg)

    print(f"Total cost of reservation: RM{cost:.2f}\n")

    if input("Do you want to make another reservation? (yes/no): ").lower() != "yes":
        break
