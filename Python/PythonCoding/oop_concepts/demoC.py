from oop_concepts.demoA import A
from oop_concepts.demoB import B

class C(B, A):
    def __init__(self, n1, n2, msg):
        A.__init__(self, n1, n2)   # explicitly call A's constructor
        B.__init__(self, msg)      # explicitly call B's constructor

    def final(self):
        print('Done')
