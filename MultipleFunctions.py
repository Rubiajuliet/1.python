class multiplefunctions():
    def oddeven():
        num=int(input("Enter a Number:"))
        if(num%2==0):
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")
    
    def eligible():
        gender=input("Your Gender (female,male):")
        age=int(input("Your age:"))
        if(gender=="female"):
            if(age>=18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(gender=="male"):
            if(age>=21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
                
    def percentage():
        s1=int(input("Subject1:"))
        s2=int(input("Subject2:"))
        s3=int(input("Subject3:"))
        s4=int(input("Subject4:"))
        s5=int(input("Subject5:"))
        tot=s1+s2+s3+s4+s5
        print("Total:",tot)
        per=tot/5
        print("Percentage:",per)  
        
    def triangle():
        h=int(input("Height:"))
        b=int(input("Breadth:"))
        area=(h*b)/2
        print("Area of Triangle:",area)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b=int(input("Breadth:"))
        perimeter=(h1+h2+b)
        print("Perimeter of Triangle:",perimeter)
        
    def BMI():
        bmi=int(input("Enter the BMI Index:"))
        if(bmi<=18.4):
            print("Under weight")
        elif(bmi<24.9):
            print("Normal Weight")
        elif(bmi<39.9):
            print("Over Weight")
        else:
            
            print("Obese")