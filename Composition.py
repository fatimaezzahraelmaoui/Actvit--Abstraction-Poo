class Composition:
    def __init__(self,produit,quantite):
        self.__Produit = produit
        self.__Quantite = quantite
    
    @property
    def Produit(self):
        return self.__Produit
    @Produit.setter
    def SetProduit(self,produit):
        self.__Prix_achat =produit
        
    @property
    def Quantite(self):
        return self.__Quantite
    @Quantite.setter
    def setQuantite(self,quantite):
        self.__Quantite = quantite
        
    def AfficherInfo(self):
        print("Produit est :",self.__Produit)
        print("Quantite est :",self.__Quantite)
    
    def ToString(self):
        return ("Produit:",self.__Produit, "Quantite :",self.__Quantite)
    
po = Composition(1234,87)
print(po.AfficherInfo())