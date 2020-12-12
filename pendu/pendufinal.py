#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:34:48 2020

@author: falgayrettes
"""


from tkinter import Tk ,Label , Button , PhotoImage,Canvas  ,StringVar , Entry
import random



maxscore=[]
def mots_aléatoires():
    #choix du mot aléatoire
    fich=open("mot.txt",'r')
    mots=fich.readlines()
    mot_a_devine=random.choice(mots)
    return(mot_a_devine)

    


def affichage_mot(mot_a_devine,lettres_trouvées):
    # cette fonction permet d'afficher le mot que le joueur doit toruver , la fonction 
    #enumerate permet de créer le mot que le joueur doit trouver avec des tirets __
    a=""
    for i ,l in enumerate(mot_a_devine , start=1):
        if i==0 or l in lettres_trouvées:
            a+=l
        else:
            a+="_"
    v.set("mot à trouver:"+a)
    print(a)
    
def gagne(mot_a_devine,lettres_trouvées):
    #cette fonction permet de dire à l'utilisateur si il a gagné ou non
    i=0
    for j in mot_a_devine:
        if j in lettres_trouvées:
            i=i+1
    if i==len(mot_a_devine)-1:
        return(True)
        
def affichage_lettre_fausses(lettres_fausses):
    #cette fonction peremt d'afficher les lettres fausses qui ont était proposé par l'utilisateur
    lettre_faux=""
    for i in lettres_fausses:
        lettre_faux+=i
        lettre_faux+=" "
    List.set("Lettres fausses: " +lettre_faux)
    return lettre_faux

def afficher_le_pendu():
    #permet d'afficher les images en fonction du nombre d'erreur que fait le joueur
    global compteur
    if compteur==1:
        Canevas.create_image(150,150,image=image2)
    if compteur==2:
        Canevas.create_image(150,150,image=image3)
    if compteur==3:
        Canevas.create_image(150,150,image=image4)
    if compteur==4:
        Canevas.create_image(150,150,image=image5)
    if compteur==5:
        Canevas.create_image(150,150,image=image6)
    if compteur==6:
        Canevas.create_image(150,150,image=image7)
    if compteur==7:
        Canevas.create_image(150,150,image=image8)
        
        
def verification():
    # cette fonction permet de vérifier si la lettre que propose le joueur est bonne ou non
    global lettres_trouvées , lettres_fausses , mot_a_devine , compteur
    l=lettre.get()
    lettre.set('')
    if l in lettres_trouvées or l in lettres_fausses:
        info.set("Dommage votre mémoire vous joue des tours, vous avez déjà donné cette lettre")
    elif l in mot_a_devine:
        lettres_trouvées.append(l)
        affichage_mot(mot_a_devine,lettres_trouvées)
        info.set("POursuivez vos efforts vous allez y arriver")
    else:
        compteur+=1
        lettres_fausses.append(l)
        afficher_le_pendu()
        compt1.set("Il vous reste: " + str(8-compteur)+ "chances")
        info.set("loupez essayez une autre lettre")
        affichage_lettre_fausses(lettres_fausses)
        
        
def pendu():
    global mot_a_devine , lettres_trouvées , lettres_fausses , compteur
    affichage_mot(mot_a_devine,lettres_trouvées)
    
    if compteur <8:
        verification()
        if gagne (mot_a_devine,lettres_trouvées)==True:
            maxscore.append(8-compteur)
            info.set("Vous avez gagné! Vouz avez obtenu un score de :"+ str(8-compteur)+"votre meilleur score est "+str(max(maxscore)))
        if compteur==8 and gagne(mot_a_devine,lettres_trouvées)!=True:
            info.set("Vous avez perdu")
            
def rejouer():
    #permet à l'utilisateur de rejouer après la partie
    global mot_a_devine, lettres_trouvées , lettres_fausses , compteur
    mot_a_devine=mots_aléatoires()
    mot_a_devine=mots_aléatoires()
    lettres_trouvées=[mot_a_devine[0]]
    lettres_fausses=[]
    compteur=0
    pendu()
    return(mot_a_devine, lettres_trouvées , lettres_fausses , compteur)
    
    

mot_a_devine=mots_aléatoires()
lettres_trouvées=[mot_a_devine[0]]
lettres_fausses=[]
compteur=0

mw=Tk()
mw.title('Jeu du pendu')

image1=PhotoImage(master=mw, file='bonhomme8.gif')
image2=PhotoImage(master=mw, file='bonhomme7.gif')
image3=PhotoImage(master=mw, file='bonhomme6.gif')
image4=PhotoImage(master=mw, file='bonhomme5.gif')
image5=PhotoImage(master=mw, file='bonhomme4.gif')
image6=PhotoImage(master=mw, file='bonhomme3.gif')
image7=PhotoImage(master=mw, file='bonhomme2.gif')
image8=PhotoImage(master=mw, file='bonhomme1.gif')

largeur=300
hauteur=300
Canevas=Canvas(mw , width=largeur, height=hauteur)
Canevas.create_image(150,150, image=image1)

lettre=StringVar()
bouton_entry=Entry(mw , textvariable=lettre)

#création du bouton "Proposer" pour proposer une lettre
bouton_proposer=Button(mw, text='Proposer', command=pendu)

#création du boutton "Rejouer" pour pouvoir rejouer
bouton_rejouer=Button(mw , text='Rejouer', command=rejouer)

#création du bouton"Quitter" pour quitter le jeu
bouton_quitter=Button(mw , text='Quitter', command=mw.destroy)

#affiche le mot à trouver avec les tirets
v=StringVar()
label_mot_rech=Label(mw, textvariable=v )

#affiche la liste des lettres proposées qui sont fausses
List=StringVar()
label_lettres_fausses=Label(mw , textvariable=List)

#affiche le nombre de coups restants 
compt1=StringVar()
compt1.set("Nombre de coups restants :" +str(8-compteur))
label_coups=Label(mw , textvariable=compt1)

info=StringVar()
console=Label(mw , textvariable=info)

label_coups.grid(row=1)
label_mot_rech.grid(row=2)
bouton_entry.grid(row=3)
bouton_proposer.grid(row=4)
bouton_rejouer.grid(row=5)
bouton_quitter.grid(row=6)
label_lettres_fausses.grid(row=7)
Canevas.grid(row=1 , column=2 , rowspan=6)
console.grid(row=7, column=2)


mw.mainloop()

    