from user import session
from product import products

cart = {}

def add_to_cart(user, product_id, quantity):
    if session['user'] == user:
        if product_id in products:
            if user not in cart:
                cart[user] = {}
            cart[user][product_id] = quantity
            print(f'Product Id {product_id} with quantity {quantity} added to {user} cart')
        else:
            print('Product does not exist ')
    elif session['admin']:
        print('Only users can add to cart')
    else:
        print('Login Required')

def remove_from_cart(user,product_id):
    if session['user'] == user:
        if product_id in products:
            if product_id in cart[user]:
                cart[user].pop(product_id)
            else:
                print('Product not in cart')
        else:
            print('Product does not exist')
    elif session['admin']:
        print('Only users can remove from cart')
    else:
        print('Login Required')

def view_cart(user):
    if session['user'] == user:
        for product_id,quantity in cart[user].items():
            print(f'Id : {product_id}, Quantity : {quantity}')
    elif session['admin']:
        print('Only users can view cart')
    else:
        print('Login required')
