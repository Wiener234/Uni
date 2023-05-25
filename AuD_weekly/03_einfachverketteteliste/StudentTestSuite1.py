import unittest
import solution

#Hinweis: Das Anfangsszenario in der Methode setUp wird vor jedem neuen Testbeispiel vorab ausgeführt und stellt somit die Ausgangssituation wieder her

class StudentTestSuite(unittest.TestCase):
    def setUp(self):
         self.os1 = solution.OperatingSystem(None, None)
         self.os2 = solution.OperatingSystem(None, None)
         self.timeline = solution.OSTimeline()
         #self.timeline.head = self.os1
         #self.timeline.head.next = self.os2

    def testExample12(self):
        self.assertFalse(self.timeline.remove(1977))
        self.assertTrue(self.timeline.insert("Unix", 1969))
        self.assertTrue(self.timeline.remove(1969))
        self.assertFalse(self.timeline.remove(1981))
        self.assertTrue(self.timeline.insert("Mac OS X 10.4", 2005))
        self.assertTrue(self.timeline.remove(2005))
        self.assertTrue(self.timeline.insert("macOS Catalina", 2019))
        self.assertFalse(self.timeline.remove(1995))
        self.assertTrue(self.timeline.insert("Windows 98", 1998))
        self.assertEqual(self.timeline.traverse(), [('Windows 98', 1998), ('macOS Catalina', 2019)])
