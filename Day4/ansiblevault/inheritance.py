class Parent1:
   def __init__(self):
     print("Paren1 Inside Constructor")
     self.__privateData1 = 100
     self._protectedData1 = 200
     self.publicData1 = 300
  
   def setValues(self, val1, val2, val3):
    
     self.__privateData1 = val1
     self._protectedData1 = val2
     self.publicData1 = val3

   def printValues(self):
     print("Value of private data is" + str(self.__privateData1))
     print("Value of protected data" + str(self._protectedData1))
     print("Value of public data" + str(self.publicData1)) 

class Parent2:
   def __init__(self):
     print("Paren2 Inside Constructor")
     self.__privateData2 = 400
     self._protectedData2 = 500
     self.publicData2 = 600

   def setValues(self, val1, val2, val3):

     self.__privateData2 = val1
     self._protectedData2 = val2
     self.publicData2 = val3

   def printValues(self):
     print("Value of private data is" + str(self.__privateData2))
     print("Value of protected data" + str(self._protectedData2))
     print("Value of public data" + str(self.publicData2))
    

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        

def main():
    obj1 = Child()
    print("Value of member variables before calling setValus function")
    obj1.printValues()
    
    print("Attempt to read public variable directly " ,obj1.publicData1)
    print("Attempt to read protected variable directly ", obj1._protectedData2)
    #print("Attempt to read private variable directly ", obj1.__privateData)

main()    
     
