import unittest
import solution

#Hinweis: Das Anfangsszenario in der Methode setUp wird vor jedem neuen Testbeispiel vorab ausgeführt und stellt somit die Ausgangssituation wieder her

class StudentTestSuite(unittest.TestCase):
    def setUp(self):
        self.root = solution.OperatingSystem("Windows 95", 1995)
        self.root.addOS(solution.OperatingSystem("1BSD", 1977))
        self.root.addOS(solution.OperatingSystem("macOS Catalina",2019))
        self.root.addOS(solution.OperatingSystem("Debian 1.1", 1996))
        self.root.addOS(solution.OperatingSystem("Mac OS X", 2000))
        self.root.addOS(solution.OperatingSystem("Unics", 1969))
        self.root.addOS(solution.OperatingSystem("Windows 10", 2015))

    def testExample1(self):
        actual = self.root.determineBalanceFactors()
        print(actual)
        expected = [('Unics', 0), ('1BSD', 1), ('Windows 10', 0), ('Mac OS X', -1), ('Debian 1.1', -2), ('macOS Catalina', 3), ('Windows 95', -2)]
        self.assertEqual(actual, expected)

    # def setUp(self):
    #     self.root = solution.OperatingSystem("Windows 95", 1995)
    #     self.root.addOS(solution.OperatingSystem("1BSD", 1977))
    #     self.root.addOS(solution.OperatingSystem("shit", 1978))
    #     self.root.addOS(solution.OperatingSystem("macOS Catalina",2019))
    #     self.root.addOS(solution.OperatingSystem("Debian 1.1", 1996))
    #     self.root.addOS(solution.OperatingSystem("Mac OS X", 2000))
    #     self.root.addOS(solution.OperatingSystem("Unics", 1969))
    #     self.root.addOS(solution.OperatingSystem("Windows 10", 2015))
    #     self.root.addOS(solution.OperatingSystem("Test", 1970))


    # def testExample1(self):
    #     actual = self.root.determineBalanceFactors()
    #     print(actual)
    #     expected = [('Test', 0), ('Unics', -1), ('shit', 0), ('1BSD', 1), ('Windows 10', 0), ('Mac OS X', -1), ('Debian 1.1', -2), ('macOS Catalina', 3), ('Windows 95', -1)]
    #     self.assertEqual(actual, expected)





    # def setUp(self):
    #     self.root = solution.OperatingSystem("Windows 95", 1995)
    #     self.root.addOS(solution.OperatingSystem("1BSD", 1977))
    #     self.root.addOS(solution.OperatingSystem("shit", 1978))
    #     self.root.addOS(solution.OperatingSystem("macOS Catalina",2019))
    #     self.root.addOS(solution.OperatingSystem("Debian 1.1", 1996))
    #     self.root.addOS(solution.OperatingSystem("Mac OS X", 2000))
    #     # self.root.addOS(solution.OperatingSystem("Test3", 1997))
    #     # self.root.addOS(solution.OperatingSystem("Test4", 1998))
    #     self.root.addOS(solution.OperatingSystem("Unics", 1969))
    #     self.root.addOS(solution.OperatingSystem("Windows 10", 2015))
    #     self.root.addOS(solution.OperatingSystem("Test", 1970))
    #     self.root.addOS(solution.OperatingSystem("Test1", 1968))


    # def testExample1(self):
    #     actual = self.root.determineBalanceFactors()
    #     print(actual)
    #     expected = [('Test1', 0), ('Test', 0), ('Unics', 0), ('shit', 0), ('1BSD', 1), ('Windows 10', 0), ('Mac OS X', -1), ('Debian 1.1', -2), ('macOS Catalina', 3), ('Windows 95', -1)]
    #     self.assertEqual(actual, expected)

    # def setUp(self):
    #     self.root = solution.OperatingSystem("Windows 95", 1995)
    #     self.root.addOS(solution.OperatingSystem("1BSD", 1977))
    #     self.root.addOS(solution.OperatingSystem("shit", 1978))
    #     self.root.addOS(solution.OperatingSystem("macOS Catalina",2019))
    #     self.root.addOS(solution.OperatingSystem("Debian 1.1", 1996))
    #     self.root.addOS(solution.OperatingSystem("Mac OS X", 2000))
    #     self.root.addOS(solution.OperatingSystem("Test3", 1997))
    #     self.root.addOS(solution.OperatingSystem("Test4", 1998))
    #     self.root.addOS(solution.OperatingSystem("Unics", 1969))
    #     self.root.addOS(solution.OperatingSystem("Windows 10", 2015))
    #     self.root.addOS(solution.OperatingSystem("Test", 1970))
    #     self.root.addOS(solution.OperatingSystem("Test1", 1968))


    # def testExample1(self):
    #     actual = self.root.determineBalanceFactors()
    #     print(self.root.traverse())
    #     print(actual)
    #     expected = [('Test1', 0), ('Test', 0), ('Unics', 0), ('shit', 0), ('1BSD', 1), ('Test4', 0) , ('Test3', -1), ('Windows 10', 0), ('Mac OS X', 1), ('Debian 1.1', -3), ('macOS Catalina', 4), ('Windows 95', -2)]
    #     self.assertEqual(actual, expected)

