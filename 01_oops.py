class Things:
    electronics_company = "boat" #class attribute
    bags_company = "thi"
    shoes_company = "vans"

    def __init__(self,electronics,bags,shoes) :   #Method1 ---> NONDynamic attribute creation
        self.electronics = electronics  #instance attributes
        self.bags = bags
        self.shoes = shoes
        
# # Create an instance/onject  #This doest work because the following
#five lines of  code are dynamic way of attribute creation 
#which cannot be use when method has been defined in init way
     
#     Vijay_owns = Things() Dynamic attribute creation
    
# #adding instance attributes
#     Vijay_owns.electronics = "Earbuds" 
#     Vijay_owns.bags = "schoolbag" 
#     Vijay_owns.shoes = "casual" 


# Create an instance/object -->#NONDynamic attribute creation
#Vijay_owns = Things(electronics="Earbuds", bags="schoolbag", shoes="casual") 
Vijay_owns = Things("Earbuds","schoolbag", "casual") 

# Modify the class attribute
Things.bags_company = "Deuter"
Things.shoes_company = "Vans"
   
   
#print instances attributes
print(Vijay_owns.shoes ,"\n" )
print(f"Bags : {Vijay_owns.bags}","\n")
print(f"electronics : {Vijay_owns.electronics}","\n")
    
#print class attributes
print(f"Vijay's ShoesCompany : {Things.shoes_company}")



# This is a valid approach, and it works in Python.
# It's called "dynamic attribute creation." You're adding attributes
# to the instance after it's created. However, it's important to
# understand the difference between instance attributes created this
# way and those defined in the __init__ method:

# Attributes defined in __init__ are created during object 
# initialization and are available as soon as the object is created.

# Attributes added dynamically to an instance (like in your 
# original code) can be added or modified at any point in the program, even after the object is created.

# The choice between the two approaches depends on your specific 
# requirements. If you know that an attribute will be part of 
# every instance and should be initialized when the object is 
# created, it's better to define it in the __init__ method. 
# If an attribute's presence and value are more flexible and 
# may vary during the program's execution, dynamic attribute
# creation can be useful. Both approaches have their use cases.



