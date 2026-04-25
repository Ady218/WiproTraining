class College:
    def __init__(self, ccode, cname, ccity):
        self.collcode = ccode                        #for instance variable use private access specifiers(name mangling)
        self.collname = cname
        self.collcity = ccity

    def welcome_message(self):
        print('Hello there!!!')

    def display_college_details(self):
        print(f'College code: {self.collcode} \nCollege Name: {self.collname} \nCity: {self.collcity}')