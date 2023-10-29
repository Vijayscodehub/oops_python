class engineering:  #made a class
    def domainName(self):   #made a method/function
        print(f"Name fo engineering domain : {self.Domain}")  #print statement within the method domainName
    
Vijay_study = engineering()  #made a object
Vijay_study.Domain = "Mechanical"   #made a instance attibute

# made a method call for the function domainName within the object Vijay_study
Vijay_study.domainName()  #Engineering.domainName(Vijay_study)

# The method call Vijay_study.domainName() executes 
# the code within the domainName method for the Vijay_study 
# object and, in your case, it will print the name of the 
# engineering domain, which is "Mechanical" as specified 
# in your previous code.

# Vijay_study is an instance of the engineering class.
# domainName is a method defined within the engineering class.
# When you write Vijay_study.domainName(), you are calling
# (invoking) the domainName method on the Vijay_study object.