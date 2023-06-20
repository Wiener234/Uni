import tkinter as tk

class Rotor:
    def __init__(self, wiring, rotorNo, rotorPos, position=0):
        self.wiring = wiring
    pass


class Enigma:
    def __init__(self, root):
        self.root = root

    def setRotors(first, second, third):
        global rotor1, rotor2, rotor3
        if first is not second is not third:
            rotor1 = Rotor(first, 1)
            rotor2 = Rotor(second, 2)
            rotor3 = Rotor(third, 3)
            pass

    def setRotorPosition(first, second, third):
        global rotor1, rotor2, rotor3
        rotor1.positon

#----------vars-----------
keyDown = None
keyIsDown = False

#----------setup----------
root = tk.Tk()
root.geometry("1600x900")


enigma = Enigma(root)

def keydown(e):
    global keyIsDown
    if keyIsDown is False:
        keyIsDown = True
        keyDown = e.char

def keyup(e):
    global keyIsDown
    keyIsDown = False
    keyDown = None

root.bind("<KeyPress>", keydown)
root.bind("<KeyRelease>", keyup)

root.mainloop()
