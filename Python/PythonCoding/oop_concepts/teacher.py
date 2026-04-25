from oop_concepts.college import College

#hierarchical ineheritance
class Teacher(College):
    def __init__(self, ccode, cname, ccity, eid, tn, de, bp):
        super().__init__(ccode, cname, ccity)
        self.empid = eid
        self.tname = tn
        self.dept = de
        self.basicpay = bp

    def calculate_salary(self):
        return self.basicpay + (self.basicpay*0.2) - (self.basicpay*0.08)
