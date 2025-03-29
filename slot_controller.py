import threading
from slot_model import SlotMachine
from slot_view import SlotMachineView

class SlotMachineController:
    def __init__(self, root):
        self.model = SlotMachine()
        self.view = SlotMachineView(root, self)
    
    def handle_spin(self):
        if not self.model.place_bet():
            return
        threading.Thread(target=self.run_spin, daemon=True).start()
    
    def run_spin(self):
        results = self.model.spin()
        self.view.update_reels(results)
        winnings = self.model.calculate_payout()
        self.model.update_balance(winnings)
        self.view.update_balance(self.model.balance)
