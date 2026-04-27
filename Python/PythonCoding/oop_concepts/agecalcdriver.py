from oop_concepts.agecalc import AgeCalculation
from oop_concepts.myexception import AgeException

age = int(input('Age: '))

aobj = AgeCalculation()

'''try:
    if aobj.voting_age_check(age):
        print('Proceed to next step.')
except AgeException as ae:
    print(ae)'''


try:
    aobj.voting_age_check(age)
    aobj.pension_age_check(age)
        #print('Proceed to next step.')
except AgeException as ae:
    print(ae)

else:
    print('Proceed to next step.')

