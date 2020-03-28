"""
ESILV - A3 - Python - TD6 - Nandy Bâ
Consignes disponibles dans le fichier Python_TD6_Consignes.pdf
"""
import numpy as np

class Vect4D():
    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t

    def __str__(self):
        res = "Vecteur : "
        res += "x: "+str(self.x)
        res += " y: "+str(self.y)
        res += " z: "+str(self.z)
        res += " t: "+str(self.t)
        return res
    
    def module(self):
        return np.sqrt(self.x**2+self.y**2+self.z**2)

    def __add__(self, other):
        if(type(other) != Vect4D):
            raise ValueError("les deux objets doivent être des objets 4D")
        if(other.t != self.t):
            raise ValueError("les deux vecteurs doivent avoir la même coordonée en temps")
        if(self.t == other.t):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            t = self.t
            v = Vect4D(x,y,z,t)
            return v

    def __sub__(self, other):
        if(type(other) != Vect4D):
            raise ValueError("les deux objets doivent être des objets 4D")
        x = - other.x
        y = - other.y
        z = - other.z
        t = self.t
        v = Vect4D(x,y,z,t)
        return self.__add__(self, v)

    def __eq__(self, other):
        if(type(other) != Vect4D):
            raise ValueError("les deux objets doivent être des objets 4D")
        Eq_x = self.x == other.x
        Eq_y = self.y == other.y
        Eq_z = self.z == other.z
        Eq_t = self.t == other.t
        return Eq_x and Eq_y and Eq_z and Eq_t

    def __mul__(self, other):
        if(type(other) != Vect4D or np.isscalar(other)):
            raise ValueError("les deux objets doivent être des objets 4D ou un vecteur et un scalaire")
        if(type(other) != Vect4D and other.t != self.t):
            raise ValueError("les deux vecteurs doivent avoir la même coordonée en temps")
        
        if(np.isscalar(other)):
            x = other * self.x
            y = other * self.y
            z = other * self.z
            t = self.t
            return Vect4D(x,y,z,t)
        else:
            #Other est une intense de Vect4D
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
            t = self.t
            return Vect4D(x,y,z,t)
            
            
        

   
