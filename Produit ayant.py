from abc import (ABC, abstractmethod)

class Produit:
    def __init__(self,nom,code):
        self.__nom = nom
        self.__code = code
    
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def Setnom(self,nom):
        self.__nom = nom
        
    @property
    def code(self):
        return self.__code
    @code.setter
    def setcode(self,code):
        self.__code = code
    
    def __str__(self):
        pass
    
    @abstractmethod
    def PrixHT(self):
        pass
    
    def Equals(self):
        pass
    
    
class Produit_Element(Produit):
    def __init__(self,nom,code,prixachat):
        super().__init__(nom,code)
        self.__nom = nom
        self.__code = code
        self.__prixAchat = prixachat
    
    @property
    def prixAchat(self):
        return self.__prixAchat
    @prixAchat.setter
    def setprixAchat(self,prixachat):
        self.__prixAchat = prixachat
    
    def __str__(self):
        return (" nom :",self.__nom ," code :",self.__code,"prix dachat :",self.__prixAchat)
    
    def getPrixHT(self):
        return self.__prixAchat
    
    def Equals(self,code):
        if self.__code == code :
            return True
        else:
            return False

class Produit_Compose(Produit):
    TVA = 0.18
    def __init__(self,nom,code,frais,liste):
        super().__init__(nom,code)
        self.__nom = nom
        self.__code = code
        self.__fraisDriction = frais
        self.__listeContituants = liste
        
    @property
    def fraisD(self):
        return self.__fraisDriction
    @fraisD.setter
    def fraisD(self,prixachat):
        self.__prixAchat = prixachat
    
    def __str__(self):
        return (" nom :",self.__nom ," code :",self.__code,"prix dachat :",self.__fraisDriction,
                "listeContituants :",self.__listeContituants)
        
    def Equals(self,code):
        if self.__code == code :
            return True
        else:
            return False
    
    def getPrixHT(self):
        return 

produit1 = Produit_Compose("v-soin",32,"SAFJ",["salah","sara"])
print(produit1.__str__())
print(produit1.Equals(32))
    
   