# Initial variable to track order status
ordering = 'y'

# List to track pie orders
pie_order = []

cart_list = []

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display welcome message
print("Welcome to the House of Pies! Here are our pies:")

# Show pie selection with index in brackets
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#for i in range(len(pie_list)):
#   print("[" + str(i) + "] " + candy_list[i])
print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
      " (9) Tamale, (10) Steak ") 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# While customer ordering
while ordering == "y":

    # Prompt user for order
    pie_choice = input("Please select the number of the pie you'd like to purchase.")         

    # Add selection to the order
    pie_order.append(pie_choice)

    # Add the selection to ther cart list
    cart_list.append(pie_list[int(pie_choice) - 1])

    # Acknowlege the customer order
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Great! We'll have that {pie_list[int(pie_choice) - 1]} right out for you.")

    # Prompt for order exit
    ordering = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the customer order is complete print order list
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"You purchased a total of {str(len(pie_order))} pie(s):")

for pie in cart_list:
    print(pie)