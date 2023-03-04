# Same as clients_list = list()
clients = []
receipts = [12.24, 18.50, 4.99, 21.75]
receipt_total = 0

"""To add someone on the list at the end
clients.append('Emily')
clients.append('John')
clients.append('Mary')

print(clients) """
# To get a user to input their client
new_client = input("What is the name of the client? ")
clients.append(new_client)

# If you want it to print without brackets
for client in clients:
    print(client)


for receipt in receipts:
    receipt_total += receipt
print(f'The total is: {receipt_total:.2f}')