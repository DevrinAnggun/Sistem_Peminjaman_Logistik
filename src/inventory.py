class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name):
        self.items[item_id] = {"name": name, "status": "Tersedia"}

    def get_available_items(self):
        return {k: v for k, v in self.items.items() if v["status"] == "Tersedia"}
