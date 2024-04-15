Overview of the Car Rental System  
The provided Python code is designed to simulate an online car rental system. It contains two classes: CarRental and Customer. These classes interact to manage car rentals, track available inventory, process rental requests, and calculate bills based on rental duration and mode.

CarRental Class   
Constructor (__init__ method)
The CarRental class is initialized with available_cars, which represents the total number of cars available for rent at the start. This parameter is stored as an instance variable.

Display Available Cars (display_available_cars method)
This method prints the current number of available cars. It's a straightforward utility to give users visibility into car availability.

Rent Cars (rent_cars method)
This method handles the renting of cars. It accepts num_cars (the number of cars to rent) and rental_mode (how the cars are rented: hourly, daily, or weekly). The method performs several checks:

If the requested number of cars is negative, it prints an error message.
If the requested number exceeds available cars, it also notifies the user of insufficient availability.
If the request can be fulfilled, it updates the inventory by subtracting the rented cars and records the rental time using the current datetime. A success message is printed, and it returns a tuple with rental details (time, number of cars, rental mode).
Return Cars (return_cars method)
When cars are returned, this method takes rental_info (a tuple containing the details of the rental) to process the return. It calculates the rental duration, updates the inventory by adding back the returned cars, and calls generate_bill to compute the final cost.

Generate Bill (generate_bill method)
This method calculates the billing amount based on the rental duration and mode. It breaks down the total rental duration into hours, days, and weeks to compute the cost according to a predefined rate table. A base cost is added to the calculated cost, and the total is printed.

Customer Class   
Constructor (__init__ method)
The Customer class is initialized with cust_id and cust_name, which store the customer's ID and name, respectively.

Request Cars (request_cars method)
This method allows a customer to request cars from the rental service. It takes the rental_service instance, the number of cars, and the rental mode as arguments. The method calls rent_cars on the rental_service and stores the returned rental information (if any).

Return Cars (return_cars method)
This method facilitates the return of rented cars. It calls the return_cars method of the rental_service using the stored rental information from the request_cars method.

Screenshots   
![image](https://github.com/areeshaanjum748/masters-data-scientist-simplilearn/assets/55443395/64bf9946-4c4a-4248-97dc-598980292404)   
![image](https://github.com/areeshaanjum748/masters-data-scientist-simplilearn/assets/55443395/89b25fb7-667c-4cb0-a3c2-19b54ae9db83)

