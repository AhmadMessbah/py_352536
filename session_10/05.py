# 10000
order_list = []
total = 0

while total < 10000:
    name = input("Name : ")
    price = int(input("Price :"))

    if total + price > 10000:
        print("You Hit the Limit ... exiting ...")
        break
    total += price
    order = {"name": name, "price": price}
    order_list.append(order)

for order in order_list:
    print(f"{order["name"]}:10 {order["price"]}")

print("------------------------------")
print(f"Total : {total}")
