#Importing libraries
import datetime

# CarRental class
class CarRental:
    
    # Constructor
    def __init__(self, available_cars):
        self.available_cars = available_cars
    
    # Display Available Cars
    def display_available_cars(self):
        print(f'Available Cars: {self.available_cars}')
    
    # Rent cars
    def rent_cars(self,num_cars, rental_mode):
        if num_cars < 0:
            print('Number of cars cannot be negative')
        
        elif(num_cars > self.available_cars):
            print('Insufficient cars available!')
        
        else:
            self.available_cars = self.available_cars - num_cars
            rental_time = datetime.datetime.now()
            print(f'{num_cars} cars rented successfully on a {rental_mode} basis at {rental_time}')
            return (rental_time, num_cars, rental_mode)
    
    # Return Cars
    def return_cars(self, rental_info):
        rental_time, num_cars, rental_mode = rental_info
        now = datetime.datetime.now()
        rental_duration = now - rental_time
        self.available_cars = self.available_cars + num_cars
        self.generate_bill(rental_duration, num_cars, rental_mode)
    
    # Generate Bill    
    def generate_bill(self, rental_duration, num_cars, rental_mode):
        base_cost = 200
        rates = {'HOURLY': 300, 'DAILY': 2000, 'WEEKLY':11000}
        hours, remainder = divmod(rental_duration.total_seconds(), 3600)
        days, remainder = divmod(hours, 24)
        weeks, days = divmod(days, 7)
        
        if rental_mode == 'HOURLY':
            cost = rates['HOURLY'] * hours * num_cars
        elif rental_mode == 'DAILY':
            cost = rates['DAILY'] * days * num_cars
        elif rental_mode == 'WEEKLY':
            cost = rates['WEEKLY'] * weeks * num_cars
            
        total_cost = base_cost + cost
        print(f'The total bill is {total_cost} INR')

# Customer class
class Customer:
    
    # Constructor
    def __init__(self, cust_id, cust_name):
        self.cust_id = cust_id
        self.cust_name = cust_name
    
    # Request Cars
    def request_cars(self, rental_service, num_cars, rental_mode):
        self.rental_info = rental_service.rent_cars(num_cars, rental_mode)
    
    # Return Cars
    def return_cars(self, rental_service):
        rental_service.return_cars(self.rental_info)