class student:
    #attributes
    name="Yeonjun"
    age=13
    classNO="2gy2"

    #contructor
    def __init__(self, name, age, classNo):
        self.name=name
        self.age=age
        self.classNo=classNo
        print("Making a new student.")
        
        #methode-function
        #methode for showing details
    def showDetails(self):
            print("showDetails:")
            print("name is",self.name)
            print("age is",self.age)
            print("classNo",self.classNo)


     #object
yeonjun=student("Yeonjun",13,"2gy2")
print(yeonjun)
print(yeonjun.showDetails())


oelaboeroeski=student("Oelaboeroeski",204,"2gy2")
print(oelaboeroeski)
print(oelaboeroeski.showDetails())





