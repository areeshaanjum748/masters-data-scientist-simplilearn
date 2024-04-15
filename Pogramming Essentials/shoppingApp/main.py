# Importing all the files
from user import *
from product import *
from cart import *
from payment import *

print('Welcome to Demo MarketPlace')

# Login into the system
print('Login')
choice = input('Is Admin? y/n')
is_admin = choice == 'y'
username = input('Enter username')
password = input('Enter password')
login(username, password, is_admin)

if session['user']:
    # User Menu
    while(True):
        print('You are into User Menu')
        print('1. View catalog')
        print('2. Add to cart')
        print('3. Remove from cart')
        print('4. View cart')
        print('5. Make payment')
        print('6. Exit the system')
        choice = int(input('Enter you choice'))
        if choice == 1:
            print('View Catalog')
            view_catalog()
        elif choice == 2:
            print('Add to cart')
            product_id = 1
            quantity = 1
            add_to_cart(username, product_id, quantity)
        elif choice == 3:
            print('Remove from Cart')
            product_id = 1
            remove_product(product_id)
        elif choice == 4:
            print('View Cart')
            view_cart(username)
        elif choice == 5:
            print('Make Payment')
            payment_mode = 'UPI'
            make_payment(username, payment_mode)
        elif choice == 6:
            print('Exiting the system')
            exit()
        else:
            print('Invalid input')
else:
    # Admin Menu
    while(True):
        print('You are into Admin Menu')
        print('1. View catalog')
        print('2. Add product')
        print('3. Update product')
        print('4. Remove product')
        print('5. Add category')
        print('6. Remove category')
        print('7. Exit the system')

        choice = int(input('Enter your choice'))
        if choice == 1:
            print('View catalog')
            view_catalog()
        elif choice == 2:
            name = 'Sofa'
            category = 'Furniture'
            price = 30000
            print('Add product')
            add_category(name, category, price)
        elif choice == 3:
            print('Update product')
            product_id = 1
            name = 'Sofa'
            category = 'Furniture'
            price = 30000
            update_product(product_id, name, category, price)
        elif choice == 4:
            print('Remove product')
            product_id = 1
            remove_product(product_id)
        elif choice == 5:
            print('Add category')
            category = 'Furniture'
            add_category(category)
        elif choice == 6:
            print('Remove category')
            category = 'Furniture'
            remove_category(category)
        elif choice == 7:
            print('Exiting the system')
            exit()
        else:
            print('Invalid input')


# Importing all the files
from user import *
from product import *
from cart import *
from payment import *

print('Welcome to Demo MarketPlace')

# Login into the system
print('Login')
choice = input('Is Admin? y/n')
is_admin = choice == 'y'
username = input('Enter username')
password = input('Enter password')
login(username, password, is_admin)

if session['user']:
    # User Menu
    while(True):
        print('You are into User Menu')
        print('1. View catalog')
        print('2. Add to cart')
        print('3. Remove from cart')
        print('4. View cart')
        print('5. Make payment')
        print('6. Exit the system')
        choice = int(input('Enter you choice'))
        if choice == 1:
            print('View Catalog')
            view_catalog()
        elif choice == 2:
            print('Add to cart')
            product_id = 1
            quantity = 1
            add_to_cart(username, product_id, quantity)
        elif choice == 3:
            print('Remove from Cart')
            product_id = 1
            remove_product(product_id)
        elif choice == 4:
            print('View Cart')
            view_cart(username)
        elif choice == 5:
            print('Make Payment')
            payment_mode = 'UPI'
            make_payment(username, payment_mode)
        elif choice == 6:
            print('Exiting the system')
            exit()
        else:
            print('Invalid input')
else:
    # Admin Menu
    while(True):
        print('You are into Admin Menu')
        print('1. View catalog')
        print('2. Add product')
        print('3. Update product')
        print('4. Remove product')
        print('5. Add category')
        print('6. Remove category')
        print('7. Exit the system')

        choice = int(input('Enter your choice'))
        if choice == 1:
            print('View catalog')
            view_catalog()
        elif choice == 2:
            name = 'Sofa'
            category = 'Furniture'
            price = 30000
            print('Add product')
            add_category(name, category, price)
        elif choice == 3:
            print('Update product')
            product_id = 1
            name = 'Sofa'
            category = 'Furniture'
            price = 30000
            update_product(product_id, name, category, price)
        elif choice == 4:
            print('Remove product')
            product_id = 1
            remove_product(product_id)
        elif choice == 5:
            print('Add category')
            category = 'Furniture'
            add_category(category)
        elif choice == 6:
            print('Remove category')
            category = 'Furniture'
            remove_category(category)
        elif choice == 7:
            print('Exiting the system')
            exit()
        else:
            print('Invalid input')


# Importing all the files
from user import *
from product import *
from cart import *
from payment import *

print('Welcome to Demo MarketPlace')

# Login into the system
print('Login')
choice = input('Is Admin? y/n')
is_admin = choice == 'y'
username = input('Enter username')
password = input('Enter password')
login(username, password, is_admin)

if session['user']:
    # User Menu
    while(True):
        print('You are into User Menu')
        print('1. View catalog')
        print('2. Add to cart')
        print('3. Remove from cart')
        print('4. View cart')
        print('5. Make payment')
        print('6. Exit the system')
        choice = int(input('Enter you choice'))
        if choice == 1:
            print('View Catalog')
            view_catalog()
        elif choice == 2:
            print('Add to cart')
            product_id = 1
            quantity = 1
            add_to_cart(username, product_id, quantity)
        elif choice == 3:
            print('Remove from Cart')
            product_id = 1
            remove_product(product_id)
        elif choice == 4:
            print('View Cart')
            view_cart(username)
        elif choice == 5:
            print('Make Payment')
            payment_mode = 'UPI'
            make_payment(username, payment_mode)
        elif choice == 6:
            print('Exiting the system')
            exit()
        else:
            print('Invalid input')
else:
    # Admin Menu
    while(True):
        print('You are into Admin Menu')
        print('1. View catalog')
        print('2. Add product')
        print('3. Update product')
        print('4. Remove product')
        print('5. Add category')
        print('6. Remove category')
        print('7. Exit the system')

        choice = int(input('Enter your choice'))
        if choice == 1:
            print('View catalog')
            view_catalog()
        elif choice == 2:
            name = 'Sofa'
            category = 'Furniture'
            price = 30000
            print('Add product')
            add_category(name, category, price)
        elif choice == 3:
            print('Update product')
            product_id = 1
            name = 'Sofa'
            category = 'Furniture'
            price = 30000
            update_product(product_id, name, category, price)
        elif choice == 4:
            print('Remove product')
            product_id = 1
            remove_product(product_id)
        elif choice == 5:
            print('Add category')
            category = 'Furniture'
            add_category(category)
        elif choice == 6:
            print('Remove category')
            category = 'Furniture'
            remove_category(category)
        elif choice == 7:
            print('Exiting the system')
            exit()
        else:
            print('Invalid input')


# Importing all the files
from user import *
from product import *
from cart import *
from payment import *

print('Welcome to Demo MarketPlace')

# Login into the system
print('Login')
choice = input('Is Admin? y/n')
is_admin = choice == 'y'
username = input('Enter username')
password = input('Enter password')
login(username, password, is_admin)

if session['user']:
    # User Menu
    while(True):
        print('You are into User Menu')
        print('1. View catalog')
        print('2. Add to cart')
        print('3. Remove from cart')
        print('4. View cart')
        print('5. Make payment')
        print('6. Exit the system')
        choice = int(input('Enter you choice'))
        if choice == 1:
            print('View Catalog')
            view_catalog()
        elif choice == 2:
            print('Add to cart')
            product_id = 1
            quantity = 1
            add_to_cart(username, product_id, quantity)
        elif choice == 3:
            print('Remove from Cart')
            product_id = 1
            remove_from_cart(username, product_id)
        elif choice == 4:
            print('View Cart')
            view_cart(username)
        elif choice == 5:
            print('Make Payment')
            payment_mode = 'UPI'
            make_payment(username, payment_mode)
        elif choice == 6:
            print('Exiting the system')
            exit()
        else:
            print('Invalid input')
else:
    # Admin Menu
    while(True):
        print('You are into Admin Menu')
        print('1. View catalog')
        print('2. Add product')
        print('3. Update product')
        print('4. Remove product')
        print('5. Add category')
        print('6. Remove category')
        print('7. Exit the system')

        choice = int(input('Enter your choice'))
        if choice == 1:
            print('View catalog')
            view_catalog()
        elif choice == 2:
            name = 'Sofa'
            category = 'Furniture'
            price = 30000
            print('Add product')
            add_product(name, category, price)
        elif choice == 3:
            print('Update product')
            product_id = 1
            name = 'Sofa'
            category = 'Furniture'
            price = 30000
            update_product(product_id, name, category, price)
        elif choice == 4:
            print('Remove product')
            product_id = 1
            remove_product(product_id)
        elif choice == 5:
            print('Add category')
            category = 'Furniture'
            add_category(category)
        elif choice == 6:
            print('Remove category')
            category = 'Furniture'
            remove_category(category)
        elif choice == 7:
            print('Exiting the system')
            exit()
        else:
            print('Invalid input')


