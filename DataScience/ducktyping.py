class Father:
    def display(self):
        print(f"I am a Father")

class Mother:
    def display(self):
        print(f"I am a Mother")

class Child:
    def show(self,obj):
        obj.display()

f=Father()
m=Mother()
c=Child()
c.show(m)
c.show(f)