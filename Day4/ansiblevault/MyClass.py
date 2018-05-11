
class MyClass:
   def __init__(self):
     print("Inside Constructor")
     self.__privateData = 100
     self._protectedData = 200
     self.publicData = 300
  
   def setValues(self, val1, val2, val3):
    
     self.__privateData = val1
     self._protectedData = val2
     self.publicData = val3

   def printValues(self):
     print("Value of private data is" + str(self.__privateData))
     print("Value of protected data" + str(self._protectedData))
     print("Value of public data" + str(self.publicData)) 


def main():
    obj1 = MyClass()
    print("Value of member variables before calling setValus function")
    obj1.printValues()
    obj1.setValues(500,600,700)
    print("Value of member variables afer calling setValues function")
    obj1.printValues()

    print("Attempt to read public variable directly " ,obj1.publicData)
    print("Attempt to read protected variable directly ", obj1._protectedData)
   # print("Attempt to read private variable directly ", obj1.__privateData)

main()    
     
