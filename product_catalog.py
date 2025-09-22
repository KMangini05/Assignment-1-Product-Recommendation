from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

preference = input("Enter a product preference: ")
customer_preferences.append(preference)

print("Customer Preferences:", customer_preferences)

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_preferences_set = set([pref.lower() for pref in customer_preferences])
print("Unique Customer Preferences:", customer_preferences_set)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.

for product in products:
    product["tags"] = set(tag.lower() for tag in product["tags"])

print("Products with tags as sets:", products) #Help to check work


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    matches = product_tags.intersection(customer_tags)
    return len(matches)


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    matches = []

    for product in products:
        product_name = product["name"]
        product_tags = set(product["tags"])

        match_count = len(product_tags.intersection(customer_tags))
        if match_count > 0:
            matches.append({"name": product_name, "matches": match_count})

    matches.sort(key=lambda x: x["matches"], reverse=True)

    return matches



# TODO: Step 7 - Call your function and print the results

matching_products = recommend_products(products, customer_preferences_set)

print("Recommended Products:")
for product in matching_products:
    print(f"{product['name']} - Matches: {product['matches']}")


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#   Here are a few operations that I used:
#       Loops: Loops helping in looping over the list of products from the product_data.py to help process each individually.
#       Sorting: Sorting the lists helped in matching products to let the customer know what products would match their demands/preferences.
#       Intersections: This method helped in finding matching tags quickly for the user.

# 2. How might this code change if you had 1000+ products?
#   If this code had 1000+ products, the program might begin to run slower due to that fact that it is checking every product one by one.
#   To fix this issue, tags could by converted to sets before running the code so it wont have to be repeated later on. Dictionaries could also be added to help the program quickly find products that have specific tags rather than searching through every product.
#   By changing these few things, the program would be better at handling large amounts of product.
