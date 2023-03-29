import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num1', help="int to add", type= int)
parser.add_argument('num2', help="2nd number to add", type= int)
args = parser.parse_args()

class Student:
    
    stipend_hike_rate = 1.05

    def __init__(self, first, last, stipend):
        self.first = first
        self.last = last
        self.stipend = stipend

    @property
    def mail(self):
        return self.first + "." + self.last + "@xyz.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_hike(self):
        self.stipend = int(self.stipend) * self.stipend_hike_rate
        return self.stipend
    
    def sayHello(self):
        return (f'Hello {self.first}!')
    
    def __len__(self):
        return len(self.first) + len(self.last)

 
    
def adding(num1,num2):
    return num1 + num2
 
person1 = Student("Frank", "Riberyyyyy",12000)


if __name__=="__main__":
    print(adding(args.num1, args.num2))