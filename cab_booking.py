
import random

print("===== CAB BOOKING CHATBOT =====")

while True:
    print("\nMAIN MENU")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        # Step 1: Choose cab type
        print("\nChoose Cab Type")
        print("1. Auto - Rs. 12/km")
        print("2. Sedan - Rs. 18/km")
        print("3. SUV - Rs. 25/km")

        cab_choice = input("Enter cab choice: ")

        if cab_choice == "1":
            cab_type = "Auto"
            rate = 12
        elif cab_choice == "2":
            cab_type = "Sedan"
            rate = 18
        elif cab_choice == "3":
            cab_type = "SUV"
            rate = 25
        else:
            print("Invalid cab choice!")
            continue

        # Step 2: Choose predefined route
        print("\nChoose Route")
        print("1. Pune Station to Shivajinagar - 5 km")
        print("2. Swargate to Kothrud - 8 km")
        print("3. Hinjawadi to Wakad - 10 km")

        route_choice = input("Enter route choice: ")

        if route_choice == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route_choice == "2":
            source = "Swargate"
            destination = "Kothrud"
            distance = 8
        elif route_choice == "3":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid route choice!")
            continue

        # Step 3: Calculate fare
        fare = distance * rate

        print("\n===== FARE DETAILS =====")
        print("Cab Type:", cab_type)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate per km: Rs.", rate)
        print("Total Fare: Rs.", fare)

        # Step 4: Confirm or cancel booking
        confirm = input(
            "\nConfirm booking? (yes/no): "
        ).lower()

        if confirm != "yes":
            print("Booking cancelled before OTP sharing.")
            continue

        # Step 5: Generate and share OTP
        otp = random.randint(1000, 9999)

        print("\nBooking confirmed!")
        print("Your 4-digit OTP is:", otp)
        print("Cancellation is now locked.")

        # Step 6: OTP verification
        entered_otp = input("Enter OTP to verify: ")

        if entered_otp == str(otp):
            print("OTP verified successfully!")
            print("Your cab booking is successful.")
        else:
            print("Incorrect OTP!")
            print("OTP verification failed.")
            print("Cancellation is still locked.")

    elif choice == "2":
        print("Thank you for using Cab Booking Chatbot!")
        break

    else:
        print("Invalid menu choice! Please try again.")
