from tkinter import Tk
from slot_controller import SlotMachineController

if __name__ == "__main__":
    root = Tk()
    app = SlotMachineController(root)
    root.mainloop()
