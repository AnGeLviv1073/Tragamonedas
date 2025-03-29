import random

class SlotMachine:
    SYMBOLS = ["lemon", "star", "bell", "diamond", "cherry"]
    
    def __init__(self):
        self.reels = [None, None, None]
        self.balance = 100
        self.bet = 10
    
    def spin(self):
        # Selecciona símbolos aleatorios para los 3 rodillos
        self.reels = [random.choice(self.SYMBOLS) for _ in range(3)]
        return self.reels
    
    def calculate_payout(self):
        if len(set(self.reels)) == 1:
            return self.bet * 10  # Premio mayor
        elif len(set(self.reels)) == 2:
            return self.bet * 2   # Premio menor
        return 0  # Sin premio
    
    def place_bet(self):
        if self.balance >= self.bet:
            self.balance -= self.bet
            return True
        return False
    
    def update_balance(self, winnings):
        self.balance += winnings
