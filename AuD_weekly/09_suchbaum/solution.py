class OperatingSystem:
    # Konstruktor
    def __init__(self, name=None, date=None):
        self.name = name
        self.releaseDate = date
        self.left = None
        self.right = None
        self.balance = None
        self.height = None

    # Destruktor
    def __del__(self):
        return 0

    # Methode, die die Timeline durchläuft (preorder) und eine Liste der enthaltenen Betriebssysteme zurückgibt
    def traverse(self, L=None):
        if L == None:
            L = []

        L.append((self.name, self.releaseDate))
        if self.left:
            self.left.traverse(L)
        if self.right:
            self.right.traverse(L)
            
        return L

	# Der Einfachheit halber nehmen wir an, dass die Betriebssysteme in der richtigen Reihenfolge hinzugefügt werden.
	# ACHTUNG: Ändern Sie diese Methode nicht, da Ihnen die Student-Test-Suite ansonsten ein falsches Ergebnis liefern kann!
    def addOS(self, os):
        if os.releaseDate < self.releaseDate:
            if self.left:
                return self.left.addOS(os)
            else:
                self.left = os
        else:
            if self.right:
                return self.right.addOS(os)
            else:
                self.right = os


    def determineBalanceFactors(self, balanceFactors=None):

        if balanceFactors == None:
            balanceFactors = []



        if self.left:
            self.left.determineBalanceFactors(balanceFactors)
        if self.right:
            self.right.determineBalanceFactors(balanceFactors)
        if self.balance == None:
            self.balance = 0
            self.height = 1
        if self.left != None and self.right != None:
            if self.left.height < self.right.height:
                self.height = self.right.height + 1
            else:
                self.height = self.left.height + 1

            self.balance = self.left.height - self.right.height
            balanceFactors.append((self.name, self.balance))
            return balanceFactors
        if self.left != None:
            self.height = self.left.height + 1
            self.balance = self.left.height
        if self.right != None:
            self.height = self.right.height + 1
            self.balance = -self.right.height

        balanceFactors.append((self.name, self.balance))



        return balanceFactors
        


        # if self.balance == None:
        #     self.balance = 0
        # if self.left != None and self.right != None:
        #     self.balance = abs(self.left.balance) - self.right.balance
        #     balanceFactors.append((self.name, self.balance))
        #     # print(self.name, self.balance)
        # if self.left != None:
        #     self.balance = abs(self.left.balance) + 1
        # if self.right != None:
        #     self.balance = self.right.balance - 1
        # return balanceFactors.append((self.name, self.balance))
        # print(self.name, self.balance)










