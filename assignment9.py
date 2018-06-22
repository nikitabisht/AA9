#question1

class Circle():
    def __init__(self,r):
        self.radius=r
    def getArea(self):
        return self.radius**2*3.14
    def getCircumfernce(self):
        return 2*self.radius*3.14
a=Circle(10)
print(a.getArea())
print(a.getCircumfernce())

#end

#question2

class Student():
    def __init__(self,name,rollno):
        self.n= name
        self.r= rollno
    def display(self):
        print("name is "+ self.n)
        print("rollno is "+ self.r)
s=Student("niki", str(7))
s.display()

#end


#question3

class Temperature():
    def __init__(self,far,cel):
        self.f=far
        self.c=cel
    def convertCelsius(self):
        celsius=((self.f)-32)*(5/9)
        print(celsius)
    def convertFarenhiet(self):
        farenhiet=(9/5*(self.c)+32)
        print(farenhiet)
t=Temperature(0,67)
t.convertFarenhiet()
t.convertCelsius()

#end


#question4

class MovieDetails():
    def __init__(self,Moviename, artistname, Yearofrelease, ratings):
        self.m=Moviename
        self.a=artistname
        self.y=Yearofrelease
        self.r=ratings
    def Display(self):
        print("movie name is "+ self.m)
        print("artist name is "+ self.a)
        print("year of release is "+self.y)
        print("ratings is"+self.r)
    def Update(self,Moviename, artistname, Yearofrelease, ratings):
        self.q= Moviename
        self.w= artistname
        self.e= Yearofrelease
        self.t= ratings
        print("movie name is "+self.q)
        print("artist name is "+self.w)
        print("year of release is "+self.e)
        print("ratings is " +self.t)
l=MovieDetails("sanju","ranbeer",str(2018),str(4))
l.Display()
l.Update("SANJU","SANJU",str(2019),str(5))

#end


#question5


class Expenditure():
    expenditure=5000
    savings=1
    def __init__(self):
        print(self.expenditure)
        print(self.savings)
    def display(self):
        print(self.expenditure)
        print(self.savings)
        salary=50001
        totalsalary=(self.expenditure)+(self.savings)
        print(salary)
        print(totalsalary)
a=Expenditure()
a.display()

#end














