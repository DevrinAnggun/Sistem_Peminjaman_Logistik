from datetime import datetime, timedelta
from config import Config

class Loan:
    def __init__(self):
        self.loans = {}

    def request_loan(self, user, item_id, inventory):
        if item_id not in inventory.items or inventory.items[item_id]["status"] != "Tersedia":
            return "Item tidak tersedia"
        if sum(1 for loan in self.loans.values() if loan["user"] == user and loan["status"] == "Dipinjam") >= Config.MAX_ITEMS_PER_USER:
            return "Melebihi batas peminjaman"
        
        self.loans[item_id] = {"user": user, "status": "Dipinjam", "due_date": datetime.now() + timedelta(days=Config.MAX_LOAN_DAYS)}
        inventory.items[item_id]["status"] = "Dipinjam"
        return "Peminjaman berhasil"

    def return_item(self, item_id, inventory):
        if item_id in self.loans and self.loans[item_id]["status"] == "Dipinjam":
            self.loans[item_id]["status"] = "Dikembalikan"
            inventory.items[item_id]["status"] = "Tersedia"
            return "Barang berhasil dikembalikan"
        return "Barang tidak dalam status dipinjam"