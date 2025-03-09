from random import*
s=1*10**3
i=True #config ok
cadeau=casino=10
boostx2=boostx20=0
ct=False
unite="E" #Unite par defaut
solde=best=s
logMode="start"
logArgent="1000"

print("******************************************")
print("************** BIENVENUE ! ***************")
print("******* LE JEU COMMENCE AVEC 1000E *******")
print("******************************************")

while i==True :
  if boostx2>0:
    B2=2
  else:
    B2=1
  if boostx20>0:
    B20=20
  else:
    B20=1

  print("******************************************")
  print("")
  print("1. Affiche votre solde")
  print("2. Nombre aléatoire entre 1 et 10")
  print("3. Casino")
  print("4. Pierre Feuille Ciseaux")
  print("5. Coinflip")
  print("6. Double or nothing")
  print("7. Cadeau")
  print("8. Boost")
  print("9. Config")

  mode=input("Choisir le mode : ")
  if mode in {"1","2","3","4","5","6","7","8","9"}:
    dev1=10123
    dev2=1010
    mode=int(mode)
    
    if mode==1:
      logMode=logMode+",banque"
      print("")
      print("***************** Banque *****************")
      print("Vous possédez",solde,unite)

    if mode==2:
      logMode=logMode+",nombre"
      cadeau=cadeau-1
      valide=mvalide=False
      while valide==False:
        print("")
        print("************ Nombre Aléatoire ************")
        nombre=input("Nombre entre 0 et 10 : ")
        if nombre in {"0","1","2","3","4","5","6","7","8","9","10"}:
          nombre=int(nombre)
          valide=True

          while mvalide==False:
            mise=int(input("Mise : "))
            if mise<=solde:
              mvalide=True
              n=randint(0,10)
              if nombre==n:
                print("Vous choisissez",nombre)
                print("Le robot choisit",n)
                print("Résultat : GAGNE",mise*4*B2*B20,unite)
                solde=solde+mise*4*B2*B20
              else:
                print("Vous choisissez",nombre)
                print("Le robot choisit",n)
                print("Résultat : PERDU",mise,unite)
                solde=solde-mise
            else:
              print("Vous n'avez pas assez d'argent !")
              mvalide=False
        else:
          print("Le nombre doit être compris entre 0 et 10 !")
      if boostx2>0:
        boostx2=boostx2-1
      if boostx20>0:
        boostx20=boostx20-1
        
    if mode==3:
      logMode=logMode+",casino"
      if solde>=casino:
        cadeau=cadeau-1
        print("")
        print("***************** Casino *****************")
        n1=randint(0,9)
        n2=randint(0,9)
        n3=randint(0,9)
        print("3 nombres identiques = 100 000",unite,"(Sans Boost)")
        print("Cout :",casino,unite)
        print(" --- --- ---")
        print("|",n1,"|",n2,"|",n3,"|")
        print(" --- --- ---")

        if n1==n2 and n2==n3:
          print("JACKPOT !!!")
          jackpot=100000
          print("VOUS GAGNEZ",jackpot*B2*B20,unite)
          solde=solde+100000*B2*B20
          casino=casino+1000
        else:
          print("Vous perdez",casino,unite)
          solde=solde-casino
          casino=casino+5
      else:
        print("Vous n'avez pas assez d'argent !")

      if boostx2>0:
        boostx2=boostx2-1
      if boostx20>0:
        boostx20=boostx20-1
    
    if mode==4:
      logMode=logMode+",pfc"
      cadeau=cadeau-1
      valide=mvalide=False
      while valide==False:
        print("")
        print("********* Pierre Feuille Ciseaux *********")
        print("1. Pierre")
        print("2. Feuille")
        print("3. Ciseaux")
        nombre=input("Choix : ")
        if nombre in {"1","2","3"}:
          nombre=int(nombre)
          valide=True

          while mvalide==False:
            mise=int(input("Mise : "))
            if mise<=solde:
              mvalide=True

              n=randint(1,3)
              if nombre==1:
                print("Vous choississez Pierre")
                if n==1:
                  print("Le robot choisit Pierre")
                  print("Résultat : EGALITE")
                elif n==2:
                  print("Le robot choisit Feuille")
                  print("Résultat : PERDU",mise,unite)
                  solde=solde-mise
                else:
                  print("Le robot choisit Ciseaux")
                  print("Résultat : GAGNE",mise*2*B2*B20,unite)  
                  solde=solde+mise*2*B2*B20                
              
              elif nombre==2:
                print("Vous choississez Feuille")
                if n==1:
                  print("Le robot choisit Pierre")
                  print("Résultat : GAGNE",mise*2*B2*B20,unite)
                  solde=solde+mise*2*B2*B20
                elif n==2:
                  print("Le robot choisit Feuille")
                  print("Résultat : EGALITE")
                else:
                  print("Le robot choisit Ciseaux")
                  print("Résultat : PERDU",mise,unite)  
                  solde=solde-mise
              
              else:
                print("Vous choississez Ciseaux")
                if n==1:
                  print("Le robot choisit Pierre")
                  print("Résultat : PERDU",mise,unite)
                  solde=solde-mise
                elif n==2:
                  print("Le robot choisit Feuille")
                  print("Résultat : GAGNE",mise*2*B2*B20,unite)
                  solde=solde+mise*2*B2*B20
                else:
                  print("Le robot choisit Ciseaux")
                  print("Résultat : EGALITE")  
            else:
              print("Vous n'avez pas assez d'argent !")
              mvalide=False
        else:
          print("Le nombre doit être 1, 2 ou 3")

      if boostx2>0:
        boostx2=boostx2-1
      if boostx20>0:
        boostx20=boostx20-1

    if mode==5:
      logMode=logMode+",coinflip"
      cadeau=cadeau-1
      valide=mvalide=False
      while valide==False:
        print("")
        print("************** Pile ou Face **************")
        print("1. Pile")
        print("2. Face")
        select=input("Choix : ")
        if select in {"1","2"}:
          select=int(select)
          valide=True
          while mvalide==False:
            mise=int(input("Mise : "))
            if mise<=solde:
              mvalide=True

              n=randint(1,2)
              if select==1:
                print("Vous choisissez Pile")
              else:
                print("Vous choisissez Face")
              if n==1:
                print("La pièce tombe sur Pile")
              else:
                print("La piece tombe sur Face")
              if select==n:
                print("Résultat : GAGNE",mise*2*B2*B20,unite)
                solde=solde+mise*2*B2*B20
              else:
                print("Résultat : PERDU",mise,unite)
                solde=solde-mise
            else:
              print("Vous n'avez pas assez d'argent !")
              mvalide=False  
        else:
          print("Le nombre doit être 1 ou 2")
          valide = False

      if boostx2>0:
        boostx2=boostx2-1
      if boostx20>0:
        boostx20=boostx20-1

    if mode==6:
      logMode=logMode+",dn"
      cadeau=cadeau-1
      x=3
      continu=True
      don=10
      print("")
      print("*********** Double or nothing ************")

      while continu==True:
        if x==1:
          print("Vous avez tout perdu")
          continu=False
        else:
          selectok=False
          print(don,unite)
          print("1. Double")
          print("2. Récupérer")
          while selectok==False:
            select=input("Choix : ")
            if select in {"1","2"}:
              select=int(select)
              selectok=True
              if select==1:
                print("****************")
                don=don*2
                x=randint(1,3)
              else:
                print("****************")
                print("Vous récupérez",don,unite)
                continu=False
                solde=solde+don
            else:
              print("Sélectionner 1 ou 2")

    if mode==7:
      logMode=logMode+",cadeau"
      print("")
      print("***************** Cadeau *****************")
      print("Gagnez jusqu'a 100",unite)
      if cadeau>0:
        print("Jouez encore", cadeau, "fois")
      else:
        w=randint(0,100)
        print("Vous gagnez",w,unite)
        solde=solde+w
        cadeau=10

    if mode==8:
      logMode=logMode+"boost,"
      sverif=False
      while sverif==False:
        print("")
        print("***************** Boost ******************")
        print("1. Boost 10 prochaines mise x2 (500",unite,")")
        print("2. Boost prochaine mise x20 (1000",unite,")")
        print("3. Voir vos boost")
        print("4. Annuler")
        s=input("Choix : ")
        if s in {"1","2","3","4"}:
          sverif=True
          s=int(s)
          if s==1:
            if solde>500:
              print("Boost 10 prochaines mise x2 (500",unite,")")
              boostx2=boostx2+10
              solde=solde-500
              print("ACTIVE")
            else:
              print("Vous n'avez pas assez d'argent !")
          elif s==2:
            if solde>1000:
              print("Boost prochaine mise x20 (1000",unite,")")
              boostx20=boostx20+1
              solde=solde-1000
              print("ACTIVE")
            else:
              print("Vous n'avez pas assez d'argent !")
          
          elif s==3:
            print("Boost x2 :", boostx2, "Restant")
            print("Boost x20 :", boostx20, "Restant")    
          else:
            print("Annulé")

        else:
         print("nombre de 1 a 3 !")

    if mode==9:
      logMode=logMode+",config"
      vchoice=False
      while vchoice==False:
        print("")
        print("************* Configuaration *************")
        print("1. Infos")
        print("2. Récompenses")
        print("3. Unité")
        print("4. Quitter le jeu")
        print("5. Retour")
        choice=input("Choix : ")
        if choice in {"1","2","3","4","5"}:
          vchoice=True
          choice=int(choice)

          if choice==1:
            print("Informations :")
            print("Version 1.5 - 08/03/2025")
            print("Numworks N0120")

          if choice==3:
            okunite=False
            while okunite==False:
              print("1. Euro (E)")
              print("2. Dollar (S)")
              selectunite=input("Choix : ")
              if selectunite in {"1","2"} or int(selectunite)==dev1 or int(selectunite)==dev2:
                okunite=True
                selectunite=int(selectunite)
                if selectunite==1:
                  print("Unité en E activé")
                  unite="E"
                if selectunite==2:
                  print("Unité en S activé")
                  unite="S"
                if int(selectunite)==dev1:
                  for r in range(15):
                    print("*******************")
                  print("*** Développeur ***")
                  print(logArgent)
                  print(logMode)
                  modif=int(input("Ajouter : "))
                  solde=solde+modif
                if int(selectunite)==dev2:
                  if ct==False:
                    print("*** Code ***")
                    print("Vous gagnez 2000", unite)
                    solde=solde+2000
                    ct=True
                  else:
                    print("Code déja utilisé")
              else:
                print("Selectionnez 1 ou 2")

          if choice==2:
            print("Récompenses :")
            print("Nombre entre 1 et 10 : Mise x4 x Boost")
            print("Casino : 100 000",unite,"x Boost")
            print("Pierre Feuille Ciiseaux : Mise x2 x Boost")
            print("Coinflip : Mise x2 x Boost")
            print("Double or nothing ne prend pas les boosts !")

          if choice==4:
            i=False
            print("A bientot !")
        else:
          print("Nombre de 1 a 5 !")
  else:
    print("Nombre de 1 a 9 !")
    
  logArgent=logArgent+","+str(solde)
  
  if choice!=4:
    if solde>best:
      print("Nouveau record !",solde,unite)
      logArgent=logArgent+"!"
      best=solde
    continuer=input("Ok pour continuer")



  if solde<=0 :
    print("******************************************")
    print()
    print("******************************************")
    print("******* Vous n'avez plus d'argent ********")
    print("******************************************")
    i=False
  
print("")
print("Merci de jouer !")

#Ibotweat 2025
#https://my.numworks.com/python/ibotweat
#Version : 1.5
#08/03/2025
