# Course-End Project: Analyzing Customer Orders Using Python
# Name: Richard Wagner
#
# This script processes a small set of customer orders using only Python's
# built-in data structures (lists, tuples, dictionaries, sets). No external
# libraries are used. The output is printed to the console.


# ---- Part 1: store the order data ----

# list of customer names
customers = ["Priya", "Marcus", "Leah", "Tom",
             "Zoe", "Noah", "Maya", "Jaden"]

# each order is a tuple: (customer, product, price, category)
orders = [
    ("Priya",  "Gaming Laptop",     1100, "Electronics"),
    ("Priya",  "Hoodie",              45, "Clothing"),
    ("Marcus", "Wireless Earbuds",    85, "Electronics"),
    ("Marcus", "Coffee Maker",        65, "Home Essentials"),
    ("Leah",   "Bluetooth Speaker",   55, "Electronics"),
    ("Leah",   "Running Shoes",       90, "Clothing"),
    ("Leah",   "Desk Lamp",           30, "Home Essentials"),
    ("Tom",    "Baseball Cap",        18, "Clothing"),
    ("Tom",    "Water Bottle",        15, "Home Essentials"),
    ("Zoe",    "Fitness Tracker",    180, "Electronics"),
    ("Zoe",    "Windbreaker",         75, "Clothing"),
    ("Noah",   "Cargo Shorts",        40, "Clothing"),
    ("Noah",   "Throw Blanket",       35, "Home Essentials"),
    ("Maya",   "e-Reader",           140, "Electronics"),
    ("Maya",   "Hoodie",              45, "Clothing"),
    ("Maya",   "Air Purifier",       120, "Home Essentials"),
    ("Jaden",  "Gaming Mouse",        55, "Electronics"),
    ("Jaden",  "Running Shoes",       40, "Clothing"),
]

# dictionary mapping each customer to a list of products they bought
customer_products = {}
for order in orders:
    name = order[0]
    product = order[1]
    if name in customer_products:
        customer_products[name].append(product)
    else:
        customer_products[name] = [product]

print("---- Part 1: order storage ----")
print("Number of customers:", len(customers))
print("Number of orders:", len(orders))
print()
print("Products per customer:")
for name in customers:
    print(" ", name, "->", customer_products[name])


# ---- Part 2: classify products by category ----

# dictionary: product -> category
product_category = {}
for order in orders:
    product = order[1]
    category = order[3]
    product_category[product] = category

# set of unique categories
unique_categories = set()
for order in orders:
    unique_categories.add(order[3])

print()
print("---- Part 2: product categories ----")
print("Available categories:", unique_categories)
print()
print("Product category mapping:")
for product in product_category:
    print(" ", product, "->", product_category[product])


# ---- Part 3: compute totals and classify each customer ----

# total amount spent per customer
customer_totals = {}
for order in orders:
    name = order[0]
    price = order[2]
    if name in customer_totals:
        customer_totals[name] += price
    else:
        customer_totals[name] = price

# assign each customer a spending class
customer_class = {}
for name in customer_totals:
    total = customer_totals[name]
    if total > 100:
        customer_class[name] = "High-Value Buyer"
    elif total >= 50:    # $50 to $100 inclusive
        customer_class[name] = "Moderate Buyer"
    else:
        customer_class[name] = "Low-Value Buyer"

print()
print("---- Part 3: customer classification ----")
for name in customers:
    print(" ", name, "- Total $" + str(customer_totals[name]),
          "-", customer_class[name])


# ---- Part 4: business insights ----

# revenue per category
category_revenue = {}
for order in orders:
    category = order[3]
    price = order[2]
    if category in category_revenue:
        category_revenue[category] += price
    else:
        category_revenue[category] = price

# unique products as a set
unique_products = set()
for order in orders:
    unique_products.add(order[1])

# customers who bought electronics (list comprehension)
electronics_customers = list({order[0] for order in orders
                              if order[3] == "Electronics"})

# top 3 spenders using sorting
totals_as_list = list(customer_totals.items())
totals_as_list.sort(key=lambda pair: pair[1], reverse=True)
top_three = totals_as_list[:3]

print()
print("---- Part 4: business insights ----")
print("Revenue per category:")
for category in category_revenue:
    print(" ", category, "-> $" + str(category_revenue[category]))

print()
print("Unique products (" + str(len(unique_products)) + "):")
print(" ", sorted(unique_products))

print()
print("Customers who bought Electronics:")
print(" ", sorted(electronics_customers))

print()
print("Top 3 highest-spending customers:")
rank = 1
for name, total in top_three:
    print(" ", rank, name, "- $" + str(total))
    rank += 1


# ---- Part 5: organize and display ----

# map each customer to the set of categories they bought from
customer_categories = {}
for order in orders:
    name = order[0]
    category = order[3]
    if name in customer_categories:
        customer_categories[name].add(category)
    else:
        customer_categories[name] = {category}

# customers who bought in more than one category
multi_category_customers = []
for name in customer_categories:
    if len(customer_categories[name]) > 1:
        multi_category_customers.append(name)

# customers who bought BOTH electronics and clothing (set intersection)
electronics_set = set()
clothing_set = set()
for order in orders:
    if order[3] == "Electronics":
        electronics_set.add(order[0])
    if order[3] == "Clothing":
        clothing_set.add(order[0])
both_buyers = electronics_set & clothing_set

print()
print("---- Part 5: summary ----")
print("Customer spending summary:")
for name in customers:
    line = " " + name + " -> $" + str(customer_totals[name])
    line += " (" + customer_class[name] + ")"
    print(line)

print()
print("Customers buying from multiple categories:")
print(" ", sorted(multi_category_customers))

print()
print("Customers who bought BOTH Electronics and Clothing:")
print(" ", sorted(both_buyers))


# ---- simple wrap-up ----

total_revenue = 0
for order in orders:
    total_revenue += order[2]

best_category = ""
best_value = 0
for category in category_revenue:
    if category_revenue[category] > best_value:
        best_value = category_revenue[category]
        best_category = category

high_count = 0
mod_count = 0
low_count = 0
for name in customer_class:
    if customer_class[name] == "High-Value Buyer":
        high_count += 1
    elif customer_class[name] == "Moderate Buyer":
        mod_count += 1
    else:
        low_count += 1

print()
print("---- wrap-up ----")
print("Total revenue: $" + str(total_revenue))
print("Top category:", best_category, "($" + str(best_value) + ")")
print("Top customer:", top_three[0][0], "($" + str(top_three[0][1]) + ")")
print("High-value buyers:", high_count)
print("Moderate buyers:", mod_count)
print("Low-value buyers:", low_count)
