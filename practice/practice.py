Staff.__init__(self, 'Manager', pName, pPay)

# instances of a subclass
self.allownance = pAllowance
self.bonus = pBonus


def calculatePay(self):
    basicPay = super().calculatePay()
    self.pay = basicPay + self.allowance
    return self.pay

def calculatePerfBonus(self):
    prompt = "Enter performance grade for %s:" %(self.name)
    grade = input(prompt)
    if (grade == 'A'):
        self.bonus = 1000
    else:
        self.bonus = 0
        return self.bonus

# won't work cuz I haven't written the Staff class
class BasicStaff(Staff):
    def __init__(self, pName, pPay):
        super().__init__('Basic', pName, pPay)

def __add__(self, other):
    return self.pay + other.pay
    
