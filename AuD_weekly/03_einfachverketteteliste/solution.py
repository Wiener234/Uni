class OperatingSystem:
    # Konstruktor
    def __init__(self, name=None, date=None):
        self.name = name
        self.releaseDate = date
        self.next = None


class OSTimeline:
    # Konstruktor
    def __init__(self):
        self.head = None

        # Methode, die die Timeline durchläuft und eine Liste der enthaltenen Betriebssysteme zurückgibt
        # ACHTUNG: Ändern Sie diese Methode nicht, da Ihnen die Student-Test-Suite ansonsten ein falsches Ergebnis liefern kann!
    def traverse(self):
        L = []
        currentNode = self.head
        while currentNode is not None:
            L.append((currentNode.name, currentNode.releaseDate))
            currentNode = currentNode.next
        return L


    # Methode, die ein neues Element in die Timeline einfügt
    def insert(self, name, releaseDate):
        # create new OS based on input
        newOS = OperatingSystem(name, releaseDate)
        # set currentNode to to first object in list
        currentNode = self.head

        if (self.head is None):
            self.head = newOS
            print("inserted")
            return True

        if (type(name) != str or type(releaseDate) != int or name == ""):
            print("invalid year")
            return False

        # edge case releaseDate befor head releaseDate
        if (newOS.releaseDate < currentNode.releaseDate):
            self.head = newOS
            newOS.next = currentNode
            print("inserted")
            return True
        # run till no currentNode
        while (currentNode is not None):
            # edge case check if newOS releaseDate exists
            # edge case check if next node exists
            if(currentNode.next == None):
                currentNode.next = newOS
                print("inserted")
                return True

            # check if releaseDate is lower or equal then next 
            if(newOS.releaseDate <= currentNode.next.releaseDate):
                # check if releaseDate is equal to next
                if(newOS.releaseDate == currentNode.next.releaseDate):
                    print("invalid year")
                    return False
                #---inserts newOS between to nodes---
                # set next node for new os
                newOS.next = currentNode.next
                # set next node for current node 
                currentNode.next = newOS
                print("inserted")
                return True
            #get next node for loop
            currentNode = currentNode.next
        return False

    
    	# Methode, die das übergebene Element in der Timeline löscht
    def remove(self, yearToRemove):
        currentNode = self.head
        if(currentNode == None or currentNode.releaseDate == None):
            print("invalid year")
            return False
        if(type(yearToRemove) != int):
            print("invalid year")
            return False
        # check if first node needs to be removed
        if currentNode == self.head and currentNode.releaseDate == yearToRemove:
            print("removed")
            self.head = currentNode.next
            return True
        
        while (currentNode.next is not None):
            if (currentNode.next.releaseDate > yearToRemove):
                print("invalid year")
                return False
            if currentNode.next.releaseDate < yearToRemove:
                currentNode = currentNode.next
            elif currentNode.next.releaseDate == yearToRemove:
                # check if node in middle of list needs to be removed
                if currentNode != self.head and currentNode.next is not None:#fucking allrounder
                    print("removed")
                    currentNode.next = currentNode.next.next
                    return True
        print("invalid year")
        return False
        	

# Hinweis: Der nachfolgende Code implementiert die Beispiel-Routine, wie im Aufgabenblatt dargestellt. 
# Sie können damit ihre Änderungen testen. Sie dürfen den Code beliebig anpassen, um weitere Fälle zu testen.
# Der Code zum Testen für die StudentTestSuite wird davon nicht beeinflusst. 

#os1  = OperatingSystem("BSD", 1977)
#os2  = OperatingSystem("Apple DOS 3.1", 1978)
#os3  = OperatingSystem("Ms Dos", 1981)
#os4  = OperatingSystem("Linux", 1991)
#os5  = OperatingSystem("Solaris", 1992)
#os6  = OperatingSystem("Windows 95", 1995)
#os7  = OperatingSystem("Mac OS X", 2000)
#
#
#timeline = OSTimeline()
#timeline.head = os1
#timeline.head.next = os2
#os2.next = os3
#os3.next = os4
#os4.next = os5
#os5.next = os6
#os6.next = os7
#
## routine
#timeline.insert("Red Hat Linux 6.2E", 2000);		
#timeline.remove(1977);			
#timeline.remove(1994);				
#timeline.insert("Unix", 1969);				
#timeline.remove(1981);				
#timeline.insert("Mac OS X 10.4", 2005);				
#timeline.remove(2005);				
#timeline.insert("macOS Catalina", 2019);				
#timeline.remove(1995);
#timeline.insert("Windows 98", 1998);
#timeline.remove(2019)
#print(timeline.traverse());
