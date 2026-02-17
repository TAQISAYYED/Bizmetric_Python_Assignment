import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"  
    "SERVER=LAYLA\\SQLEXPRESS;"
    "DATABASE=TAQI;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

cursor.execute("SELECT menu_id, menu_name, price FROM MENU")
menu_data = cursor.fetchall()


menu = {row.menu_id: {'name': row.menu_name, 'price': row.price} for row in menu_data}

print("\n===== MENU =====")
for id, item in menu.items():
    print(f"{id:3}. {item['name']:12} - {item['price']:.2f}")
print("================\n")


order_items = []

while True:
    try:
        menu_id = int(input("Enter Menu ID to order (0 to finish): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if menu_id == 0:
        break

    if menu_id not in menu:
        print("Invalid Menu ID. Try again.")
        continue

    try:
        qty = int(input(f"Enter quantity for {menu[menu_id]['name']}: "))
        if qty <= 0:
            print("Quantity must be at least 1")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    total_price = menu[menu_id]['price'] * qty
    order_items.append({'menu_id': menu_id, 'quantity': qty, 'total_price': total_price})
    print(f"Added {qty} x {menu[menu_id]['name']} to your order. Subtotal: ${total_price:.2f}\n")


for item in order_items:
    cursor.execute(
        "INSERT INTO ORDERS (menu_id, quantity, total_price) VALUES (?, ?, ?)",
        item['menu_id'], item['quantity'], item['total_price']
    )
conn.commit()


print("\n" + "="*40)
print(" " * 12 + "RESTAURANT BILL")
print("="*40)
print(f"{'Item':20} {'Qty':>3} {'Price':>7} {'Total':>8}")
print("-"*40)

grand_total = 0
for item in order_items:
    name = menu[item['menu_id']]['name']
    qty = item['quantity']
    price = menu[item['menu_id']]['price'] 
    total = item['total_price']
    grand_total += total
    print(f"{name:20} {qty:>3} {price:>6.2f} {total:>7.2f}")

print("-"*40)
print(f"{'GRAND TOTAL':>32} {grand_total:>7.2f}")
print("="*40)
print("Thank you for visiting! Please come again.\n")


cursor.close()
conn.close()
