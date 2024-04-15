from user import session
from cart import cart
from product import products

payments = ['NetBanking', 'PayPal', 'UPI', 'COD']

def make_payment(user, payment_mode):
    if session['user'] == user:
        if payment_mode in payments:
             if user in cart and cart[user]:
                  total_amount = 0
                  for product_id,quantity in cart[user].items():
                      total_amount = total_amount + products[product_id]['price'] * quantity
                  cart[user] = {} # Clearing cart
                  if payment_mode == 'UPI':
                      print(f'You will be shortly redirected to the portal for Unified Payment Interface to make a payment of {total_amount}')
                  else:
                      print(f'Your order with {total_amount} amount is successfully placed')
             else:
                  print('Your cart is empty')
        else:
           print('Payment mode not available')
    elif session['admin']:
        print('Only users can make payment')
    else:
        print('Login required')

