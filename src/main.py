from inventory import Inventory
from loan import Loan

inventory = Inventory()
loan_system = Loan()

# Menambahkan barang ke dalam inventory
inventory.add_item("B001", "Laptop")
inventory.add_item("B002", "Proyektor")
inventory.add_item("B003", "Speaker")

# Simulasi peminjaman
print(loan_system.request_loan("Alice", "B001", inventory))
print(loan_system.request_loan("Bob", "B002", inventory))
print(loan_system.return_item("B001", inventory))