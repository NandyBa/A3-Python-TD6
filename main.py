"""
ESILV - A3 - Python - TD6 - Nandy Bâ
Consignes disponibles dans le fichier Python_TD6_Consignes.pdf
"""
import numpy as np
import tkinter as tk

class Vect4D():
    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t

    def __str__(self):
        res = "Vecteur : \n"
        res += " x: "+str(self.x) +"\n"
        res += " y: "+str(self.y) +"\n"
        res += " z: "+str(self.z) +"\n"
        res += " t: "+str(self.t) +"\n"
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
        if(type(other) != np.ndarray):  
            if(type(other) != Vect4D or np.isscalar(other)):
                raise ValueError("les deux objets doivent être des objets 4D ou un vecteur et un scalaire")
            if(type(other) != Vect4D  and other.t != self.t):
                raise ValueError("les deux vecteurs doivent avoir la même coordonée en temps")
        
        if(np.isscalar(other)):
            x = other * self.x
            y = other * self.y
            z = other * self.z
            t = self.t
            return Vect4D(x,y,z,t)
        elif(type(other) == np.ndarray):
            #On doit faire un produit matriciel
            v = np.array([[self.x], [self.y], [self.z], [self.t]])
            return  np.dot(other, v)
        else:
            #Other est une intense de Vect4D
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
            t = self.t
            return Vect4D(x,y,z,t)
    

class Mat4D():
    def __init__(self, v1, v2, v3, v4):
        if(type(v1) != Vect4D):
            raise ValueError("v1 doit est une instance de Vect4D")
        if(type(v2) != Vect4D):
            raise ValueError("v2 doit est une instance de Vect4D")
        if(type(v3) != Vect4D):
            raise ValueError("v3 doit est une instance de Vect4D")
        if(type(v4) != Vect4D):
            raise ValueError("v4 doit est une instance de Vect4D")
        
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        M = []
        M.append([v1.x, v2.x, v3.x, v4.x])
        M.append([v1.y, v2.y, v3.y, v4.y])
        M.append([v1.z, v2.z, v3.z, v4.z])
        M.append([v1.t, v2.t, v3.t, v4.t])
        M = np.array(M)
        self.M = M
    
    def __str__(self):
        res = "Matrice:\n"
        v1 = self.v1
        v2 = self.v2
        v3 = self.v3
        v4 = self.v4
        M = []
        M.append([v1.x, v2.x, v3.x, v4.x])
        M.append([v1.y, v2.y, v3.y, v4.y])
        M.append([v1.z, v2.z, v3.z, v4.z])
        M.append([v1.t, v2.t, v3.t, v4.t])
        M = np.array(M)
        res += str(M)
        return res
    
    """
    Surchages des opérations
    (surcharges simplifiée par l'utilisation de numpy)
    """
    def __add__(self, other):
        if(type(other) == np.ndarray):
            return self.M + other
        elif(type(other) == Mat4D):
            return self.M + other.M
        
    def __sub__(self, other):
        if(type(other) == np.ndarray):
            return self.M - other
        elif(type(other) == Mat4D):
            return self.M - other.M
    
    def __eq__(self, other):
        if(type(other) == np.ndarray):
            return self.M == other
        elif(type(other) == Mat4D):
            return self.M == other.M
    
    def __mul__(self, other):
        if(type(other) == np.ndarray):
            return np.dot(self.M * other)
        elif(type(other) == Mat4D):
            return np.dot(self.M, other.M)
        elif(type(other) == Vect4D):
            V = np.array([[other.x], [other.y], [other.z], [other.t]])
            return np.dot(self.M, V)

def Id4d():
    return np. identity(4)

def SysmX():
    M = Id4d()
    M[0][0] = -1
    return M

def SysmY():
    M = Id4d()
    M[1][1] = -1
    return M

def SysmZ():
    M = Id4d()
    M[2][2] = -1
    return M

def Trans(x,y,z):
    M = Id4d()
    M[0][3] = x
    M[1][3] = y
    M[2][3] = z
    return M

def TransX(a):
    return Trans(a,0,0)

def TransY(a):
    return Trans(0,a,0)

def TransZ(a):
    return Trans(0,0,a)

def RotX(theta):
    M = Id4d()
    c = np.cos(theta)
    s = np.sin(theta)
    M[1][1] = c
    M[1][2] = s
    M[2][1] = -s
    M[2][2] = c
    return M

def RotY(theta):
    M = Id4d()
    c = np.cos(theta)
    s = np.sin(theta)
    M[0][0] = c
    M[0][2] = s
    M[2][0] = -s
    M[2][2] = c
    return M

def RotZ(theta):
    M = Id4d()
    c = np.cos(theta)
    s = np.sin(theta)
    M[0][0] = c
    M[0][1] = s
    M[1][0] = -s
    M[1][1] = c
    return M




class Application():
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.rowconfigure(0, weight=7)
        self.fenetre.columnconfigure(0, weight=6)
        
        
        w = tk.Label(self.fenetre, text="Theta 1:")
        w.grid(row=0, column=1, sticky="nsew")
        theta1 = tk.StringVar(self.fenetre)
         
        self.var_theta1 = tk.Entry(self.fenetre, textvariable=theta1, width=30)
        self.var_theta1.grid(row=0, column=2, sticky="nsew")
         
        w = tk.Label(self.fenetre, text="Theta 2:")
        w.grid(row=0, column=3, sticky="nsew")
        
        
        theta2 = tk.StringVar(self.fenetre)
         
        self.var_theta2 = tk.Entry(self.fenetre, textvariable=theta2, width=30)
        self.var_theta2.grid(row=0, column=4, sticky="nsew")
        
        w = tk.Label(self.fenetre, text="Theta 3:")
        w.grid(row=1, column=1, sticky="nsew")
        
        theta3 = tk.StringVar(self.fenetre)
        
         
        self.var_theta3 = tk.Entry(self.fenetre, textvariable=theta3, width=30)
        self.var_theta3.grid(row=1, column=2, sticky="nsew")
        
        w = tk.Label(self.fenetre, text="Theta 4:")
        w.grid(row=1, column=3, sticky="nsew")
        
        theta4 = tk.StringVar(self.fenetre)
         
        self.var_theta4 = tk.Entry(self.fenetre, textvariable=theta4, width=30)
        self.var_theta4.grid(row=1, column=4, sticky="nsew")
        
        w = tk.Label(self.fenetre, text="L:")
        w.grid(row=2, column=3, sticky="nsew")
        
        L = tk.StringVar(self.fenetre)
        self.var_L = tk.Entry(self.fenetre, textvariable=L, width=30)
        self.var_L.grid(row=2, column=4, sticky="nsew")
        
        w = tk.Label(self.fenetre, text="X: ")
        w.grid(row=4, column=1, sticky="nsew")
        
        X = tk.StringVar(self.fenetre)
        self.var_X = tk.Entry(self.fenetre, textvariable=X, width=30)
        self.var_X.grid(row=4, column=2, sticky="nsew")
        
        w = tk.Label(self.fenetre, text="Y:")
        w.grid(row=4, column=3, sticky="nsew")
        
        Y = tk.StringVar(self.fenetre)
        self.var_Y = tk.Entry(self.fenetre, textvariable=Y, width=30)
        self.var_Y.grid(row=4, column=4, sticky="nsew")
        
        w = tk.Label(self.fenetre, text="Z:")
        w.grid(row=4, column=5, sticky="nsew")
        
        Z = tk.StringVar(self.fenetre)
        self.var_Z = tk.Entry(self.fenetre, textvariable=Z, width=30)
        self.var_Z.grid(row=4, column=6, sticky="nsew")
        
        valid_btn = tk.Button(self.fenetre)
        valid_btn["text"] = "Calculer"
        valid_btn["command"] = self.calculer
        valid_btn.grid(row=5, column=3, sticky="nsew")
        
         
         
        self.fenetre.mainloop()
        
    def calculer(self):
        theta1 = float(self.var_theta1.get())
        theta2 = float(self.var_theta2.get())
        theta3 = float(self.var_theta3.get())
        theta4 = float(self.var_theta4.get())
        X = float(self.var_X.get())
        Y = float(self.var_Y.get())
        Z = float(self.var_Z.get())
        L = float(self.var_L.get())
        V = Vect4D(X,Y,Z,1)
        M1 = RotX(theta1)
        M2 = RotY(theta2)
        M3 = RotX(theta3)
        M4 = RotZ(theta4)
        L = TransX(L)
        MatTransformation = np.dot(M1,np.dot(M2, np.dot(M3, np.dot(M4, L))))
        
        matrice = tk.Label(self.fenetre, text="Matrice:"+str(MatTransformation))
        matrice.grid(row=6, column=1, sticky="nsew")
        res =  V * MatTransformation #Avec la surcharge fait bien la calcum matTransformation * V
        vecteur = tk.Label(self.fenetre, text="Vecteur:"+str(res))
        vecteur.grid(row=7, column=1, sticky="nsew")
 
Application()
         
            
        

   
