from user import session
# List of categories
categories = ['Footwear', 'Clothing', 'Electronics', 'Cosmetics']

# Product catalog
products = {
    1 : {'name': 'Crocs', 'category': 'Footwear', 'price': 2000},
    2 : {'name': 'Denim Jacket', 'category': 'Clothing', 'price': 3000},
    3 : {'name': 'Headphones', 'category': 'Electronics', 'price': 2500},
    4 : {'name': 'Sunscreen', 'category': 'Cosmetics', 'price': 500}
}

def view_catalog():
    for id,product in products.items():
        print(f"Id: {id}, Name: {product['name']}, Category: {product['category']}, 'Price: {product['price']}")

def add_product(name, category, price):
    if session['admin']:
        if category in categories:
            product_id = len(products) + 1
            products[product_id] = {'name': name, 'category': category,'price':price}
            print(f'Product {name} added successfully')
        else:
            print('Category does not exist')
    else:
        print('Only admins can add products')

def update_product(product_id, name = None, category = None, price = None):
    if session['admin']:
        if product_id in products:
            if name:
                products[product_id]['name'] = name
            if category and category in categories:
                products[product_id]['category'] = category
            else:
                print('Category does not exist')
            if price:
                products[product_id]['price'] = price
            print(f'Product Id {product_id} updated successfully')
        else:
            print('Product not found')
    else:
        print('Only admins can update products')

def remove_product(product_id):
    if session['admin']:
        if product_id in products:
            products.pop(product_id)
            print(f'Product {product_id} removed successfully')
        else:
            print('Product does not exist')
    else:
        print('Only admins can remove products')

def add_category(category):
    if session['admin']:
        if category not in categories:
            categories.append(category)
            print('Category added successfully')
        else:
            print('Category already exists')
    else:
        print('Only admins can add categories')

def remove_category(category):
    if session['admin']:
        if category in categories:
            categories.remove(category)
            print('Category removed successfully')
            # Optionally, remove products of this category
        else:
            print('Category does not exist')
    else:
        print('Only admins can remove categories')




