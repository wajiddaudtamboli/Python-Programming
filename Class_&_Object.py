class list:
    
    def __init__(self):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        print("       LIST FUNCTIONS:     ")
        listl=[8,1,5,2,3,4,5,2]
        self.listl=listl
        print("\n")

    def fun1(self):         
        print("Copy: ",self.listl.copy())
        print("\n")

    def fun2(self):        
        print("Count: ",self.listl.count(2))
        print("\n")

    def fun3(self):
        print("Append: ",self.listl.append(13))
        print("\n")
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
obj=list()
obj.fun1()
obj.fun2()
obj.fun3()



