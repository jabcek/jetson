
class Rectangle:
    def __init__(self,c,w,l):
        self.width=w
        self.length=l
        self.color=c
    def area(self):
        self.area=self.width*self.length
        return self.area
    def per(self):
        self.per=2*self.width+2*self.length
        return self.per


clr1='Red'
w1=3
l1=4

rect1=Rectangle(clr1,w1,l1)
areaRect1=rect1.area()
print('Rectangle1 is :',rect1.color, 'with area=',areaRect1)


clr2='Blue'
w2=5
l2=4

rect2=Rectangle(clr2,w2,l2)
areaRect2=rect2.area()
print('Rectangle2 is :',rect2.color, 'with area=',areaRect2)

print('Rectangle1 is:' ,rect1.color)
per2=rect2.per()
print('Preimeter2 is:' ,per2)