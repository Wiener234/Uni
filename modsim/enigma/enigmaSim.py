import tkinter as tk
import random

#----------vars-----------
letterOrder = "QWERTZUIOPASDFGHJKPYXCVBNML"
letterOrderLowerCase = "qwertzuioasdfghjkpyxcvbnml"
keyLight = None
keyDown = None
keyIsDown = False




class Rotor:
    wiring = None
    position = 0
    rotorNo = None
    rotorPos = None


    def __init__(self, root, rotorNumber, rotorPosition):
        self.root = root
        self.rotorNo = rotorNumber
        self.rotorPos = rotorPosition
        if self.rotorNo == 0:
            wiring = [[0, 15 ], [1, 4 ], [2, 25 ], [3, 20 ], [4, 14 ], [5, 7 ], [6, 23 ], [7, 18 ], [8, 2 ], [9, 21 ], [10, 5 ], [11, 12 ], [12, 19 ], [13, 1 ], [14, 6 ], [15, 11 ], [16, 17 ], [17, 8 ], [18, 13 ], [19, 16 ], [20, 9 ], [21, 22 ], [22, 0 ], [23, 24 ], [24, 3 ], [25, 10 ]]  
        elif self.rotorNo == 1:
            wiring = [[0, 25 ], [1, 14 ], [2, 20 ], [3, 4 ], [4, 18 ], [5, 24 ], [6, 3 ], [7, 10 ], [8, 5 ], [9, 22 ], [10, 15 ], [11, 2 ], [12, 8 ], [13, 16 ], [14, 23 ], [15, 7 ], [16, 12 ], [17, 21 ], [18, 1 ], [19, 11 ], [20, 6 ], [21, 13 ], [22, 9 ], [23, 17 ], [24, 0 ], [25, 19 ]]
        elif self.rotorNo == 2:
            wiring = [[0, 4 ], [1, 7 ], [2, 17 ], [3, 21 ], [4, 23 ], [5, 6 ], [6, 0 ], [7, 14 ], [8, 1 ], [9, 16 ], [10, 20 ], [11, 18 ], [12, 8 ], [13, 12 ], [14, 25 ], [15, 5 ], [16, 11 ], [17, 24 ], [18, 13 ], [19, 22 ], [20, 10 ], [21, 19 ], [22, 15 ], [23, 3 ], [24, 9 ], [25, 2 ]]
        elif self.rotorNo == 3:
            wiring = [[0, 8 ], [1, 12 ], [2, 4 ], [3, 19 ], [4, 2 ], [5, 6 ], [6, 5 ], [7, 17 ], [8, 0 ], [9, 24 ], [10, 18 ], [11, 16 ], [12, 1 ], [13, 25 ], [14, 23 ], [15, 22 ], [16, 11 ], [17, 7 ], [18, 10 ], [19, 3 ], [20, 21 ], [21, 20 ], [22, 15 ], [23, 14 ], [24, 9 ], [25, 13 ]]
        elif self.rotorNo == 4:
            wiring = [[0, 16 ], [1, 22 ], [2, 4 ], [3, 17 ], [4, 19 ], [5, 25 ], [6, 20 ], [7, 8 ], [8, 14 ], [9, 0 ], [10, 18 ], [11, 3 ], [12, 5 ], [13, 6 ], [14, 7 ], [15, 9 ], [16, 10 ], [17, 15 ], [18, 24 ], [19, 23 ], [20, 2 ], [21, 21 ], [22, 1 ], [23, 13 ], [24, 12 ], [25, 11 ]]

    def runThrough(input, forward):
        if forward:
            input = input+positon % 26
            return wiring[input][1]
        else:
            for i in range(26):
                if input == wiring[i][1]:
                    output = wiring[i][0]-positon
                    while output < 0:
                        output = 26 + output
                    output = output % 26
                    return output
        return -1
    
    #----------show()----------------
    #TODO: display rotor 


    #---------click()----------------
    #TODO: write click to move rotor


    #---------nextRotor()------------
    #TODO: change rotor positon


class Enigma:
    def __init__(self, root):
        self.root = root

    def setRotors(self, first, second, third):
        global rotor1, rotor2, rotor3
        if first is not second is not third:
            rotor1 = Rotor(root, first, 1)
            rotor2 = Rotor(root, second, 2)
            rotor3 = Rotor(root, third, 3)
            pass

    def setRotorPosition(self, first, second, third):
        global rotor1, rotor2, rotor3
        rotor1.positon = first
        rotor2.positon = second
        rotor3.positon = third

    def runMachine(self, inputChar):
        if rotor1.rotorNo == rotor2.rotorNo or rotor2.rotorNo == rotor3.rotorNo or rotor1.rotorNo == rotor3.rotorNo:
            print("Error rotors cannnot have the same number")
            return '1'
        inputNo = letterOrderLowerCase.find(inputChar)
        #TODO: implement PlugBoard and set variables

    #---------moveRotators()-------------

    #---------show()---------------------

    def randomRotors(self):
        rand1 = random.randint(1,5)
        rand2 = random.randint(1,5)
        while rand1 == rand2:
            rand2 = random.randint(1,5)
        rand3 = random.randint(1,5)
        while rand1 == rand3 or rand2 == rand3:
            rand3 = random.randint(1,5)
        self.setRotors(rand1, rand2, rand3)

    def randomPosition(self):
        self.setRotorPosition(random.randint(1,26), random.randint(1,26), random.randint(1,26))

    #--------click()---------


    #--------processWord()--------


#----------------------enigmaSim------------------------------------

#----------setup----------
root = tk.Tk()
root.geometry("1600x900")


enigma = Enigma(root)
enigma.randomRotors()
enigma.randomPosition()

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
