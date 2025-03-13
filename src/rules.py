from config import Config


class Rules:
    rules_table = {
        "max_loan_days": Config.MAX_LOAN_DAYS,
        "max_items_per_user": Config.MAX_ITEMS_PER_USER,
    }
    
    @staticmethod
    def get_rules():
        return Rules.rules_table