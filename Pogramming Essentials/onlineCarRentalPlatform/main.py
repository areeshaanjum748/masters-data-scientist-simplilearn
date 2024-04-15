from car_rental import *
rental_service = CarRental(10)
customer = Customer(1, 'Areesha')

while True:
    print("\n1. Display available cars")
    print("2. Rent cars")
    print("3. Return cars")
    print("4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        rental_service.display_available_cars()
        
    elif choice == '2':
        num_cars = int(input("How many cars would you like to rent? "))
        rental_mode = input("Enter rental mode ('HOURLY', 'DAILY', 'WEEKLY'): ")
        customer.request_cars(rental_service, num_cars, rental_mode)
        
    elif choice == '3':
        if customer.rental_info:
            customer.return_cars(rental_service)
        else:
            print("You have no rentals to return.")
    
    elif choice == '4':
        print("Thank you for using the car rental system.")
        break
    else:
        print("Invalid choice. Please choose again.")
