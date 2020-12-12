#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:13:52 2020

@author: falgayrettes
"""
import random 

from tkinter import Tk ,Label , Button , PhotoImage,Canvas  ,StringVar , Entry

def motaleatoire():
    fich=open("mot.txt",'r')
    mots=fich.readlines()
    L=random.choice(mots)
    return(L)
    
def conversionmotenliste(mot):
    
    levraimot=[]
    
    for x in mot: 
        levraimot.append(x)
    levraimot.pop()

    return levraimot



def creationdumot(L):
    M=[L[0]]
    for i in range (1,len(L)-1):
        M.append('_')
    return(M)
    
def restart():
    replay=input('Pour rejouer écrivez  pour arrêter et afficher votre meilleur score écrivez stop')
    if replay=='r':
        findtheword()
    else:
        print('voici votre meilleur score de vos parties')
        
        
def findtheword():
    meilleurscore=0
    L=motaleatoire()
    compteur=0
    lettretrouve=[]
    lettrefausse=[]
    score=[]
    motatrouve=creationdumot(L)
    print(motatrouve)
    while compteur<8 and len(lettretrouve)<len(L)-2:
        proposition=input('proposer une lettre ou un mot')
        if len(proposition)>1:
            print('mauvais choix de mot')
            compteur+=1
            affichage_bonhomme()

        else:
            if proposition in lettrefausse :
                print('deja essayé')
            if proposition in lettretrouve : 
                print('deja essayé')
            if proposition not in L:
                lettrefausse.append(proposition)
                print('incorrect')
                print('cette lettre est déjè essayée et fausse , les lettres déjà essayé sont' )
                print(lettrefausse)
                compteur+=1
                affichage_bonhomme()
            else:       
                for k in range(1,len(L)):
                    if proposition==L[k]:
                        motatrouve[k]=proposition
                        print(motatrouve)
                        lettretrouve.append(proposition)
                        print('les lettres trouvées sont:')
                        print(lettretrouve)
    if compteur==8:
        print("Vous avez perdu. Votre score est donc de", 0)
                       
    elif len(lettretrouve)==len(L)-2:
        score.append(8-compteur)
        print("Vous avez gagné avec un score de", 8-compteur)
        
        if 8-compteur>meilleurscore:
            print("Félicitations ! vous avez battu votre record ! votre meilleur score est",max(score))
                        
    Rejouerounon(compteur)

    
    
    
    
def Rejouerounon(compteur):
    rejouer=input("Voulez vous rejouer ? o pour oui ; n pour non")
    if rejouer=="o":
        findtheword()
    else:
        print ("Vous avez fini ce jeu avec un score de",compteur,", au revoir")
        return('cestfini')
        

photos=[]

'''
def affichage_bonhomme():
    global compteur
    if compteur==0:
        item=Canevas.create_image(150,150,image=Image1)
    if compteur==1:
        item=Canevas.create_image(150,150,image=Image2)
    if compteur==2:
        item=Canevas.create_image(150,150,image=Image3)
    if compteur==3:
        item=Canevas.create_image(150,150,image=Image4)
    if compteur==4:
        item=Canevas.create_image(150,150,image=Image5)
    if compteur==5:
        item=Canevas.create_image(150,150,image=Image6)
    if compteur==6:
        item=Canevas.create_image(150,150,image=Image7)
    if compteur==7:
        item=Canevas.create_image(150,150,image=Image8)
    
'''



mw=Tk()
mw.title('jeu du pendu')
mw.geometry("800x400")


largeur=300
hauteur=300

Canevas=Canvas(mw,width=largeur,height=hauteur,bg="#3E3F3F")
Canevas.place(x=0,y=0)





'''
Image1 = PhotoImage(file="bonhomme8.gif")
Image2= PhotoImage(file="bonhomme7.gif")
Image3 = PhotoImage(file="bonhomme6.gif")
Image4 = PhotoImage(file="bonhomme5.gif")
Image5 = PhotoImage(file="bonhomme4.gif")
Image6 = PhotoImage(file="bonhomme3.gif")
Image7 = PhotoImage(file="bonhomme2.gif")
Image8 = PhotoImage(file="bonhomme1.gif")


#Canevas.itemconfig(img,image=Image1)
item=Canevas.create_image(600,200,image=Image2)
'''


def affichage_bonhomme():
    global photos , image_Caneva
    compteur=0
    photo=PhotoImage(file="bonhomme"+str(8-compteur)+".gif")
    image_Caneva.create_image(200,100,image=photo)
    photos.append(photo)
 
image_Caneva=Canvas(mw , width=largeur , height=hauteur)
affichage_bonhomme()
image_Caneva.pack()


lettre=StringVar()
bouton_entry=Entry(mw,textvariable=lettre)

#création du bouton "Proposer" pour proposer une lettre
bouton_proposer=Button(mw, text='Proposer',command=findtheword)
bouton_proposer.pack()
bouton_entry.pack()

'''
#création du bouton "Rejouer" pour pouvoir rejouer
bouton_rejouer=Button(mw , text='Rejouer' , command=lambda:Rejouerounon(compteur))


#création du bouton "quitter" pour pouvoir rarréter le jeu
bouton_quitter=Button(mw , text='quitter' , command=mw.destroy)
'''
'''
#création d'un label pour afficher le mot trouver avec les _ _ _
a=StringVar()
a.set("Mot à trouver:" + creationdumot(L))
label_mot_rech=Label(mw , textvariables=a)

compt1=StringVar()
compt1.set("Nombre de coups restant:" + str(8-compteur))
label_coups=Label(mw, textvariable=compt1)


label_coups.grid(row=1,sticky=NE)
label_mot_rech.grid(row=2)
bouton_rejouer.grid(row=5)
bouton_quitter.grid(row=6)
Canevas.grid(row=1, column=2 ,rowspan=6)
'''
mw.mainloop()


