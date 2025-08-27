groceries = {"products":[]}

while True:
    try:
        user_input = input("")
        groceries["products"].append(user_input)
    except EOFError:
         break

grocery_list = groceries["products"]

for product in sorted(set(grocery_list)):
    count = grocery_list.count(product)
    print(f"{count} {product.upper()}")