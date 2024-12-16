from tkinter import Tk
from controller.main_controller import MainController

class Application:
    def __init__(self):
        self.root = Tk()  
        self.main_controller = MainController(self)

    def run(self):
        self.main_controller.start()
        self.root.mainloop()  

if __name__ == "__main__":
    app = Application()
    app.run()  
