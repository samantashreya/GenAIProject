#1 a.create a list of customer names

customer_names = ["Shreyasi", "Sneha", "Sarah", "Syncha", "Samuel", "Samantha", "Soilel", "Sonia", "Siddharth", "Suresh","Sakshi", "Sanjay", "Sahil", "Sanya", "Siddhi", "Saurabh", "Sonal", "Suhana", "Siddhant"]

#1 b.store each customer's orders details (customer name, product, price, category) as tuple inside a list
orders = [('Shreyasi', 'Apple Macbook Air', 150000, 'Electronics'),
          ('Shreyasi', 'Canva Pro', 4000, 'Software & Subscriptions'),
          ('Shreyasi', 'Nike Air Zoom Pegasus 38', 7999, 'Fashion & Apparel'),
          ('Sneha', 'M.A.C Macximal Matte Mini Lipstick', 3200, 'Health & Beauty'),
          ('Sneha', "L'Oreal Paris Revitalift Double Serum", 2999, 'Health & Beauty'),
          ('Sneha', 'Canva Pro', 4000, 'Software & Subscriptions:'),
          ('Sneha', 'Sony WH-1000XM4 Wireless Noise-Canceling Headphones', 24990, 'Electronics'),
          ('Sneha', 'Dyson V11 Torque Drive Cordless Vacuum Cleaner', 59900, 'Home Appliances'),
          ('Sarah', 'Apple iPhone 13 Pro Max', 129900, 'Electronics'),
          ('Sarah', 'Samsung Galaxy Z Fold 3', 159999, 'Electronics'),
          ('Sarah', 'Sony Bravia 55-inch 4K Ultra HD Smart LED TV', 79999, 'Electronics'),
          ('Sarah', 'Bose QuietComfort 35 II Wireless Bluetooth Headphones', 24900, 'Electronics'),
          ('Sarah', 'KitchenAid Artisan Stand Mixer', 49900, 'Home Appliances'),
          ('Sarah', 'LG 340 L Frost Free Double Door 2 Star Refrigerator', 52490, 'Home Appliances'),
          ('Syncha', 'Woman Zara Midi Halter Neck Dress With Dots', 3950, 'Fashion & Apparel'),
          ('Syncha', 'Zara Wide Short Sleeve Knit Top', 2050, 'Fashion & Apparel'),
          ('Syncha', 'H&M Cotton T-Shirt', 599, 'Fashion & Apparel'),
          ('Syncha', 'Puma Unisex Running Shoes', 3499, 'Fashion & Apparel'),
          ('Samuel', 'Borosil Best Digi Air Fryer', 10935, 'Home Appliances'),
          ('Samuel', 'Adobe Creative Cloud All Apps', 3276, 'Software & Subscriptions'),
          ('Samuel', 'Dyson Supersonic Nural Hair Dryer', 41900, 'Home Appliances'),
          ('Samuel', 'KitchenAid Artisan Stand Mixer', 49900, 'Home Appliances'),
          ('Samantha', 'WHOOP 5.0 Peak Health and Fitness Tracker', 33890, 'Electronics'),
          ('Samantha', 'Apple iPad Pro 12.9-inch (2021)', 137800, 'Electronics'),
          ('Samantha', 'Samsung Galaxy Watch Active2', 24900, 'Electronics'),
          ('Soilel', 'Apple Care', 7500, 'Software & Subscriptions'),
          ('Soilel', 'Nike Mens Dunk Low', 8295, 'Fashion & Apparel'),
          ('Soilel', 'Adidas Ultraboost 21 Running Shoes', 15995, 'Fashion & Apparel'),
          ('Sonia', 'Zara Wide Short Sleeve Knit Top', 2050, 'Fashion & Apparel'),
          ('Siddharth', 'Amazon Echo Pop Smart Speaker with Alexa', 3294, 'Electronics'),
          ('Siddharth', 'Zara Hooded Sweatshirt', 12990, 'Fashion & Apparel'),
          ('Siddharth', 'Dyson V11 Torque Drive Cordless Vacuum Cleaner', 59900, 'Home Appliances'),
          ('Suresh', 'Dyson Supersonic Nural Hair Dryer', 41900, 'Home Appliances'),
          ('Sakshi', 'Puma Unisex Running Shoes', 3499, 'Fashion & Apparel'),
          ('Sanjay', 'OnePlus Nord 2 5G', 29999, 'Electronics'),
          ('Sahil', 'Adidas Ultraboost 21 Running Shoes', 15995, 'Fashion & Apparel'),
          ('Sanya', 'H&M Cotton T-Shirt', 599, 'Fashion & Apparel'),
          ('Siddhi', 'Reebok CrossFit Nano X15 Training Shoes', 4495, 'Fashion & Apparel'),
          ('Saurabh', 'Sony WH-1000XM4 Wireless Noise-Canceling Headphones', 24990, 'Electronics'),
          ('Sonal', 'Philips HD7766/60 Airfryer XXL', 8495, 'Home Appliances'),
          ('Sonal', ' YouTube Music Premium', 149, 'Software & Subscriptions'),
          ('Siddhant', 'Apple iPad Pro 12.9-inch (2021)', 137800, 'Electronics')]

#1 c. Create a function which use a dictionary where keys are customer names and values are lists of ordered products
#This function will return a dictionary where each key is a customer name and the corresponding value is a list of products they have ordered.
def create_customer_orders_dict(orders_list):
    customer_orders = {}
    for order in orders_list:
        customer_name = order[0]
        product_name = order[1]
        
        if customer_name not in customer_orders:
            customer_orders[customer_name] = []
        customer_orders[customer_name].append(product_name)
    return customer_orders

    



#2 Classify products by category
#2 a. Create a function which use a dictionary to map each product to its respective category
def create_product_categories_dict(orders_list):
    product_categories = {}
    for order in orders_list:
        product_name = order[1]
        category = order[3]
        product_categories[product_name] = category
    return product_categories

product_categories = create_product_categories_dict(orders)

#2 b. Create a set of unique product categories
unique_categories = set(product_categories.values())

#2 c. Create a function to Display all available product categories
def display_product_categories(categories):
    print(f"\nUnique Product Categories: {categories}")

#display_product_categories(unique_categories)

# 3. Analyze customer orders
# 3 a. Loop 1: Calculate the final total amount each customer spends
customer_spending = {}
for order in orders:
    customer_name = order[0]
    product_price = order[2]
    
    if customer_name not in customer_spending:
        customer_spending[customer_name] = 0
    customer_spending[customer_name] += product_price

# 3b. Loop through each unique customer ONCE to classify and print
# create a function to classify customers based on their total spending
def classify_customers_spendingWise(customer_spending_dict):
    print("\n--- Final Customer Classifications ---")
    for customer_name, total_amount in customer_spending_dict.items():
        
        # Adjusted thresholds to match the INR data values:
        # High-value: Above ₹10,000
        if total_amount > 10000:
            print(f"{customer_name} is classified as a high-value buyer. (Total: ₹{total_amount:,})")

        # Moderate buyer: Between ₹5,000 and ₹10,000
        elif 5000 <= total_amount <= 10000:
            print(f"{customer_name} is classified as a moderate buyer. (Total: ₹{total_amount:,})")

        # Low-value buyer: Below ₹5,000
        else:
            print(f"{customer_name} is classified as a low-value buyer. (Total: ₹{total_amount:,})")

# 3. Analyze customer orders
# Loop 1: Calculate the final total amount each customer spends
customer_spending = {}
for order in orders:
    customer_name = order[0]
    product_price = order[2]
    
    if customer_name not in customer_spending:
        customer_spending[customer_name] = 0
    customer_spending[customer_name] += product_price

#4. Generate business insights
# 4a.Create a function to calculate the total revenue per product category and store it in a dictionary

def calculate_total_revenue_per_category(orders_list):
    total_revenue_per_category = {}
    for order in orders_list:
        category = order[3]
        price = order[2]
        if category not in total_revenue_per_category:
            total_revenue_per_category[category] = 0
        total_revenue_per_category[category] += price
    return total_revenue_per_category
  
#4b Extract unique products from all orders using a set
unique_categories = set(product_categories.values())
display_product_categories(unique_categories)


#4c create a function which uses a list comprehension to find all customers who purchased electronics
def find_customers_by_category(category):
    return [order[0] for order in orders if order[3] == category]


#4d Identify the top three highest-spending customers using sorting
top_customers = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)[:3] 

#5. 5. Organize and display data
#5a.create  a function to Print a summary of each customer’s total spending and their classification
def print_customer_summary():
    sorted_customer_spending = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)
    for customer, total in sorted_customer_spending:
        if total > 10000:
            classification = "High-value buyer"
            print(f"{customer}: ₹{total:,} - {classification}")
        elif 5000 <= total <= 10000:
            classification = "Moderate buyer"
            print(f"{customer}: ₹{total:,} - {classification}")
        else:
            classification = "Low-value buyer"
            print(f"{customer}: ₹{total:,} - {classification}")


#5b.create a function to find customers who purchased from multiple categories
def find_customers_from_multiple_categories():
    customer_categories = {}
    for order in orders:
        customer_name = order[0]
        category = order[3]

        if customer_name not in customer_categories:
            customer_categories[customer_name] = set()
        customer_categories[customer_name].add(category)

    return [customer for customer, categories in customer_categories.items() if len(categories) > 1]


#5c.create a function to identify common customers who bought both electronics and Fashion & Apparel    
def find_common_customers():
    electronics_customers = {order[0] for order in orders if order[3] == "Electronics"}
    fashion_apparel_customers = {order[0] for order in orders if order[3] == "Fashion & Apparel"}
    return electronics_customers.intersection(fashion_apparel_customers)

     

#5d. create a function to identify trend based on category wise sales.
def identify_sales_trends():
    total_revenue_per_category = calculate_total_revenue_per_category(orders)
    sorted_categories = sorted(total_revenue_per_category.items(), key=lambda x: x[1], reverse=True)
    
    print("\n--- Sales Trends by Category ---")
    for category, total_revenue in sorted_categories:
        print(f"{category}: ₹{total_revenue:,}")
#5e. Create a function to find the most frequently purchased products
def find_most_frequently_purchased_products():
    product_frequency = {}
    for order in orders:
        product_name = order[1]
        if product_name not in product_frequency:
            product_frequency[product_name] = 0
        product_frequency[product_name] += 1

    sorted_products = sorted(product_frequency.items(), key=lambda x: x[1], reverse=True)
    
    print("\n--- Most Frequently Purchased Products ---")
    for product, frequency in sorted_products:
        print(f"{product}: {frequency} purchases")


#5e. Generate business insights - 
# Calculate the total revenue per product category and store it in a dictionary
# Extract unique products from all orders using a set
# Use a list comprehension to find all customers who purchased electronics
# identify the top three highest-spending customers using sorting
#--- Organize and display data----
# Print a summary of each customer’s total spending and their classification
# Use set operations to find customers who purchased from multiple categories
# Identify common customers who bought both electronics and fashion & apparel   
# Extract the high-value customers and most frequently purchased products
# Identify trends based on category-wise sales
def generate_business_insights():
    total_revenue_per_category = calculate_total_revenue_per_category(orders)
    unique_products = set(order[1] for order in orders)
    electronics_customers = find_customers_by_category("Electronics")

    top_customers = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)[:3]
    
    print("\n--- Business Insights ---")
    print("\nTotal Revenue per Product Category:")
    for category, revenue in total_revenue_per_category.items():
        print(f"{category}: ₹{revenue:,}")
    
    print("\nUnique Products:")
    for product in unique_products:
        print(product)
    
    print("\nCustomers who purchased Electronics:")
    for customer in set(electronics_customers):
        print(customer)
    
    print("\nTop 3 Highest-Spending Customers:")
    for customer, total in top_customers:
        print(f"{customer}: ₹{total:,}")
    
    print("\nCustomer Spending Summary:")
    print_customer_summary()
    
    multiple_category_customers = find_customers_from_multiple_categories()
    print("\nCustomers who purchased from multiple categories:")
    for customer in multiple_category_customers:
        print(customer)
    
    common_customers = find_common_customers()
    print("\nCommon customers who bought both Electronics and Fashion & Apparel:")
    for customer in common_customers:
        print(customer)
    
    identify_sales_trends()
    find_most_frequently_purchased_products()


generate_business_insights()    