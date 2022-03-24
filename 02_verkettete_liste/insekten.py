from abc import ABC, abstractmethod
from liste_gen import *

class Fluginsekt(ABC):
    lebensdauer: int
    
    def __init__(self, lebensdauer: int):
        self.lebensdauer = lebensdauer    
    
    def fliegen(self):
        print("I believe I can fly, ...")
    
class Schmetterling(Fluginsekt):
    def fliegen(self):
        print("Flatter, Flatter")

class Stechmuecke(Fluginsekt):
    def beisen(self):
        print("Ich habe Duuuuuurst")
        
class Biene(Fluginsekt):
    def stechen(self):
        print("piiiieeeeks")

class Spielzeugdrohne:
    def __init__(self):
        pass
    
    def fliegen(self):
        print("pssssss pssssss")
        
insekten:ListIterativ[Fluginsekt] = ListIterativ()
insekten.append(Schmetterling(22))
insekten.append(Stechmuecke(40))
insekten.append(Biene(50))
insekten.append(Spielzeugdrohne())

for insekt in insekten:
    insekt.fliegen()
    
for insekt in insekten:
    if isinstance(insekt, Stechmuecke): insekt.beisen()
    
stechinsekten: ListIterativ[Stechmuecke] = ListIterativ()
stechinsekten.append(Stechmuecke(22))
stechinsekten.append(Biene(22))

