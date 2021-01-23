

"""Les NQA autorisés par rapport à la taille du lot"""

def function (lot_quantity, nqa, type):       #(Nombre de pièces dans le lot, niveau de qualité accéptable, type de contrôle) 

    # IF principal numéro 1 : servant à traiter le type de contrôle à faire (Simple ou Double) ici Simple
    if type=="simple":
      object_de_comunication = {
            'type': 'simple',                 #Type de contrôle qualité
            'nsample':0,                      #Nombre d'échantillons à contrôler
            'alimit':0,                     #Limite d'acceptation
            'rlimit':0,                      #Limite de refus
            'frisk':0,                        #Risque fournisseur
            'crisk':0,                        #Risque client
            'possible_nqa':[],                #Les NQA possibles pour ce lot (en fonction du nombre de pièces)
            'advice': 'not implemented yet',   # A définir
              }
      # IF secondaire pour le type de ontrôle : Simple (IF par rapport à la taille du lot) 
      if 2<lot_quantity:
        return print("Error ! Lot size must be greater than 2 ")
      #------------------------------------------------------------------------------------        
      elif 2=<lot_quantit=<8:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] = 2
        object_de_comunication['possible_nqa'] =[6.5]
          if nqa == 6.5:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 2.53
            object_de_comunication['crisk'] = 68.4
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to 6.5 for this case ")
      #------------------------------------------------------------------------------------
      elif 9=<lot_quantit=<15:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] = 3
        object_de_comunication['possible_nqa'] =[4]
          if nqa == 4:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 1.7
            object_de_comunication['crisk'] = 53.6
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to 4 for this case ")
      #------------------------------------------------------------------------------------
      elif 16=<lot_quantit=<25:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] = 5
        object_de_comunication['possible_nqa'] =[10,2.5]
          if nqa == 2.5:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 1.02
            object_de_comunication['crisk'] = 36.9
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 7.63
            object_de_comunication['crisk'] = 58.4
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10, 2.5] for this case ")
      #------------------------------------------------------------------------------------
      elif 26=<lot_quantit=<50:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] = 8
        object_de_comunication['possible_nqa'] =[10,6.5,1.5]
          if nqa == 1.5:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.64
            object_de_comunication['crisk'] = 25
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 2.64
            object_de_comunication['crisk'] = 40.6
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 11.1
            object_de_comunication['crisk'] = 53.9
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,1.5] for this case ")
      #------------------------------------------------------------------------------------
      elif 51=<lot_quantit=<90:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] = 13
        object_de_comunication['possible_nqa'] =[10,6.5,4,1]
          if nqa == 1:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.394
            object_de_comunication['crisk'] = 16.1
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 2.81
            object_de_comunication['crisk'] = 26.8
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 6.63
            object_de_comunication['crisk'] = 36
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = 3
            object_de_comunication['rlimit'] = 4
            object_de_comunication['frisk'] = 11.3
            object_de_comunication['crisk'] = 44.4
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,1] for this case ")
      #------------------------------------------------------------------------------------
      elif 91=<lot_quantit=<150:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] = 20
        object_de_comunication['possible_nqa'] =[10,6.5,4,2.5,0.65]
          if nqa == 0.65:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.256
            object_de_comunication['crisk'] = 10.9
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 1.8
            object_de_comunication['crisk'] = 18.1
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 4.22
            object_de_comunication['crisk'] = 24.5
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = 3
            object_de_comunication['rlimit'] = 4
            object_de_comunication['frisk'] = 7.13
            object_de_comunication['crisk'] = 30.4
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = 5
            object_de_comunication['rlimit'] = 6
            object_de_comunication['frisk'] = 14
            object_de_comunication['crisk'] = 41.5
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,2.5,0.65] for this case ")
      #------------------------------------------------------------------------------------
      elif 151=<lot_quantit=<280:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] =32
        object_de_comunication['possible_nqa'] =[10,6.5,4,2.5,1.5,0.4]
          if nqa == 0.4:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.161
            object_de_comunication['crisk'] = 6.94
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 1.13
            object_de_comunication['crisk'] = 11.6
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 2.59
            object_de_comunication['crisk'] = 15.8
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = 3
            object_de_comunication['rlimit'] = 4
            object_de_comunication['frisk'] = 4.39
            object_de_comunication['crisk'] = 19.7
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = 5
            object_de_comunication['rlimit'] = 6
            object_de_comunication['frisk'] = 8.5
            object_de_comunication['crisk'] = 27.1
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = 7
            object_de_comunication['rlimit'] = 8
            object_de_comunication['frisk'] = 13.1
            object_de_comunication['crisk'] = 34.1
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,2.5,1.5,0.4] for this case ")
      #------------------------------------------------------------------------------------
      elif 281=<lot_quantit=<500:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] =50
        object_de_comunication['possible_nqa'] =[10,6.5,4,2.5,1.5,1,0.25]
          if nqa == 0.25:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.103
            object_de_comunication['crisk'] = 4.5
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 0.712
            object_de_comunication['crisk'] = 7.56
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 1.66
            object_de_comunication['crisk'] = 10.3
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = 3
            object_de_comunication['rlimit'] = 4
            object_de_comunication['frisk'] = 2.77
            object_de_comunication['crisk'] = 12.9
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = 5
            object_de_comunication['rlimit'] = 6
            object_de_comunication['frisk'] = 5.34
            object_de_comunication['crisk'] = 17.8
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = 7
            object_de_comunication['rlimit'] = 8
            object_de_comunication['frisk'] = 8.2
            object_de_comunication['crisk'] = 22.4
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = 10
            object_de_comunication['rlimit'] = 11
            object_de_comunication['frisk'] = 12.9
            object_de_comunication['crisk'] = 29.1
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,2.5,1.5,1,0.25] for this case ")
      #------------------------------------------------------------------------------------
      elif 501=<lot_quantit=<1200:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] =80
        object_de_comunication['possible_nqa'] =[10,6.5,4,2.5,1.5,1,0.65,0.15]
          if nqa == 0.15:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.064
            object_de_comunication['crisk'] = 2.84
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 0.444
            object_de_comunication['crisk'] = 4.78
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 1.03
            object_de_comunication['crisk'] = 6.52
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = 3
            object_de_comunication['rlimit'] = 4
            object_de_comunication['frisk'] = 1.73
            object_de_comunication['crisk'] = 8.16
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = 5
            object_de_comunication['rlimit'] = 6
            object_de_comunication['frisk'] = 3.32
            object_de_comunication['crisk'] = 11.3
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = 7
            object_de_comunication['rlimit'] = 8
            object_de_comunication['frisk'] = 5.06
            object_de_comunication['crisk'] = 14.2
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = 10
            object_de_comunication['rlimit'] = 11
            object_de_comunication['frisk'] = 7.91
            object_de_comunication['crisk'] = 18.6
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = 14
            object_de_comunication['rlimit'] = 15
            object_de_comunication['frisk'] = 11.9
            object_de_comunication['crisk'] = 24.2
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,2.5,1.5,1,0.65,0.15] for this case ")
      #------------------------------------------------------------------------------------
      elif 1201=<lot_quantit=<3200:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] =125
        object_de_comunication['possible_nqa'] =[10,6.5,4,2.5,1.5,1,0.65,0.4,0.1]
          if nqa == 0.1:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.041
            object_de_comunication['crisk'] = 1.84
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.4:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 0.284
            object_de_comunication['crisk'] = 3.11
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 0.654
            object_de_comunication['crisk'] = 4.26
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = 3
            object_de_comunication['rlimit'] = 4
            object_de_comunication['frisk'] = 1.09
            object_de_comunication['crisk'] = 5.35
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = 5
            object_de_comunication['rlimit'] = 6
            object_de_comunication['frisk'] = 2.09
            object_de_comunication['crisk'] = 7.42
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = 7
            object_de_comunication['rlimit'] = 8
            object_de_comunication['frisk'] = 3.19
            object_de_comunication['crisk'] = 9.42
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = 10
            object_de_comunication['rlimit'] = 11
            object_de_comunication['frisk'] = 4.94
            object_de_comunication['crisk'] = 12.3
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = 14
            object_de_comunication['rlimit'] = 15
            object_de_comunication['frisk'] = 7.4
            object_de_comunication['crisk'] = 16.1
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = 21
            object_de_comunication['rlimit'] = 22
            object_de_comunication['frisk'] = 11.9
            object_de_comunication['crisk'] = 22.5
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,2.5,1.5,1,0.65,0.4,0.1] for this case ")
      #------------------------------------------------------------------------------------
      elif 3201=<lot_quantit=<10000:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] =200
        object_de_comunication['possible_nqa'] =[6.5,4,2.5,1.5,1,0.65,0.4,0.25,0.065]
          if nqa == 0.065:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.0256
            object_de_comunication['crisk'] = 1.15
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.25:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 0.178
            object_de_comunication['crisk'] = 1.95
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.4:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 0.409
            object_de_comunication['crisk'] = 2.66
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = 3
            object_de_comunication['rlimit'] = 4
            object_de_comunication['frisk'] = 0.683
            object_de_comunication['crisk'] = 3.34
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = 5
            object_de_comunication['rlimit'] = 6
            object_de_comunication['frisk'] = 1.31
            object_de_comunication['crisk'] = 4.64
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = 7
            object_de_comunication['rlimit'] = 8
            object_de_comunication['frisk'] = 1.99
            object_de_comunication['crisk'] = 5.89
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = 10
            object_de_comunication['rlimit'] = 11
            object_de_comunication['frisk'] = 3.09
            object_de_comunication['crisk'] = 7.7
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = 14
            object_de_comunication['rlimit'] = 15
            object_de_comunication['frisk'] = 4.62
            object_de_comunication['crisk'] = 10.1
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = 21
            object_de_comunication['rlimit'] = 22
            object_de_comunication['frisk'] = 7.45
            object_de_comunication['crisk'] = 14.1
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [6.5,4,2.5,1.5,1,0.65,0.4,0.25,0.065] for this case ")
      #------------------------------------------------------------------------------------
      elif 10001=<lot_quantit=<35000:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] =315
        object_de_comunication['possible_nqa'] =[4,2.5,1.5,1,0.65,0.4,0.25,0.15,0.04]
          if nqa == 0.04:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.0163
            object_de_comunication['crisk'] = 0.731
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.15:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 0.112
            object_de_comunication['crisk'] = 1.23
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.25:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 0.259
            object_de_comunication['crisk'] = 1.69
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.4:
            object_de_comunication['alimit'] = 3
            object_de_comunication['rlimit'] = 4
            object_de_comunication['frisk'] = 0.433
            object_de_comunication['crisk'] = 2.12
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = 5
            object_de_comunication['rlimit'] = 6
            object_de_comunication['frisk'] = 0.829
            object_de_comunication['crisk'] = 2.94
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = 7
            object_de_comunication['rlimit'] = 8
            object_de_comunication['frisk'] = 1.26
            object_de_comunication['crisk'] = 3.74
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = 10
            object_de_comunication['rlimit'] = 11
            object_de_comunication['frisk'] = 1.96
            object_de_comunication['crisk'] = 4.89
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = 14
            object_de_comunication['rlimit'] = 15
            object_de_comunication['frisk'] = 2.94
            object_de_comunication['crisk'] = 6.39
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = 21
            object_de_comunication['rlimit'] = 22
            object_de_comunication['frisk'] = 4.73
            object_de_comunication['crisk'] = 8.95
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [4,2.5,1.5,1,0.65,0.4,0.25,0.15,0.04] for this case ")
      #------------------------------------------------------------------------------------
      elif 35001=<lot_quantit=<150000:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] =500
        object_de_comunication['possible_nqa'] =[2.5,1.5,1,0.65,0.4,0.25,0.15,0.1,0.025]
          if nqa == 0.025:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.0103
            object_de_comunication['crisk'] = 0.461
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.1:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 0.071
            object_de_comunication['crisk'] = 0.778
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.15:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 0.164
            object_de_comunication['crisk'] = 1.06
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.25:
            object_de_comunication['alimit'] = 3
            object_de_comunication['rlimit'] = 4
            object_de_comunication['frisk'] = 0.273
            object_de_comunication['crisk'] = 1.34
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.4:
            object_de_comunication['alimit'] = 5
            object_de_comunication['rlimit'] = 6
            object_de_comunication['frisk'] = 0.523
            object_de_comunication['crisk'] = 1.86
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = 7
            object_de_comunication['rlimit'] = 8
            object_de_comunication['frisk'] = 0.796
            object_de_comunication['crisk'] = 2.35
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = 10
            object_de_comunication['rlimit'] = 11
            object_de_comunication['frisk'] = 1.23
            object_de_comunication['crisk'] = 3.08
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = 14
            object_de_comunication['rlimit'] = 15
            object_de_comunication['frisk'] = 1.85
            object_de_comunication['crisk'] = 4.03
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = 21
            object_de_comunication['rlimit'] = 22
            object_de_comunication['frisk'] = 2.98
            object_de_comunication['crisk'] = 5.64
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [2.5,1.5,1,0.65,0.4,0.25,0.15,0.1,0.025] for this case ")
      #------------------------------------------------------------------------------------
      elif 150001=<lot_quantit=<500000:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] =800
        object_de_comunication['possible_nqa'] =[1.5,1,0.65,0.4,0.25,0.15,0.1,0.065,0.015]
          if nqa == 0.015:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.0064
            object_de_comunication['crisk'] = 0.288
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.065:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 0.044
            object_de_comunication['crisk'] = 0.468
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.1:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 0.102
            object_de_comunication['crisk'] = 0.665
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.15:
            object_de_comunication['alimit'] = 3
            object_de_comunication['rlimit'] = 4
            object_de_comunication['frisk'] = 0.171
            object_de_comunication['crisk'] = 0.835
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.25:
            object_de_comunication['alimit'] = 5
            object_de_comunication['rlimit'] = 6
            object_de_comunication['frisk'] = 0.327
            object_de_comunication['crisk'] = 1.16
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.4:
            object_de_comunication['alimit'] = 7
            object_de_comunication['rlimit'] = 8
            object_de_comunication['frisk'] = 0.498
            object_de_comunication['crisk'] = 3.47
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = 10
            object_de_comunication['rlimit'] = 11
            object_de_comunication['frisk'] = 0.771
            object_de_comunication['crisk'] = 1.93
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = 14
            object_de_comunication['rlimit'] = 15
            object_de_comunication['frisk'] = 1.16
            object_de_comunication['crisk'] = 2.52
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = 21
            object_de_comunication['rlimit'] = 22
            object_de_comunication['frisk'] = 1.86
            object_de_comunication['crisk'] = 3.52
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [1.5,1,0.65,0.4,0.25,0.15,0.1,0.065,0.015] for this case ")
      #------------------------------------------------------------------------------------
      else:
        object_de_comunication['type'] = 'simple'
        object_de_comunication['nsample'] =1250
        object_de_comunication['possible_nqa'] =[1,0.65,0.4,0.25,0.15,0.1,0.065,0.04,0.01]
          if nqa == 0.01:
            object_de_comunication['alimit'] = 0
            object_de_comunication['rlimit'] = 1
            object_de_comunication['frisk'] = 0.0041
            object_de_comunication['crisk'] = 0.184
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.04:
            object_de_comunication['alimit'] = 1
            object_de_comunication['rlimit'] = 2
            object_de_comunication['frisk'] = 0.028
            object_de_comunication['crisk'] = 0.310
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.065:
            object_de_comunication['alimit'] = 2
            object_de_comunication['rlimit'] = 3
            object_de_comunication['frisk'] = 0.065
            object_de_comunication['crisk'] = 0.426
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.1:
            object_de_comunication['alimit'] = 3
            object_de_comunication['rlimit'] = 4
            object_de_comunication['frisk'] = 0.109
            object_de_comunication['crisk'] = 0.534
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.15:
            object_de_comunication['alimit'] = 5
            object_de_comunication['rlimit'] = 6
            object_de_comunication['frisk'] = 0.209
            object_de_comunication['crisk'] = 0.742
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.25:
            object_de_comunication['alimit'] = 7
            object_de_comunication['rlimit'] = 8
            object_de_comunication['frisk'] = 0.318
            object_de_comunication['crisk'] = 0.942
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.4:
            object_de_comunication['alimit'] = 10
            object_de_comunication['rlimit'] = 11
            object_de_comunication['frisk'] = 0.494
            object_de_comunication['crisk'] = 1.23
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = 14
            object_de_comunication['rlimit'] = 15
            object_de_comunication['frisk'] = 0.74
            object_de_comunication['crisk'] = 1.61
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = 21
            object_de_comunication['rlimit'] = 22
            object_de_comunication['frisk'] = 1.19
            object_de_comunication['crisk'] = 2.25
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [1,0.65,0.4,0.25,0.15,0.1,0.065,0.04,0.01] for this case ")
      #Fin if------------------------------------------------------------------------------------      
      
      
      
      
      
      
      
      
      
      
      
      
      return object_de_comunication
      #Fin if------------------------------------------------------------------------------------
    
    # IF principal numéro 2 : servant à traiter le type de contrôle à faire (Simple ou Double) ici Double
    elif type=="double":
      object_de_comunication = {
            'type': 'double',                 #Type de contrôle qualité
            'nsample':[],                      #Nombre d'échantillons à contrôler
            'alimit': [],                     #Limite d'acceptation
            'rlimit':[],                      #Limite de refus
            'frisk':0,                        #Risque fournisseur
            'crisk':0,                        #Risque client
            'possible_nqa':[],                #Les NQA possibles pour ce lot (en fonction du nombre de pièces)
            'advice': 'not implemented yet',   # A définir
              }
      # IF secondaire pour le type de ontrôle : Double (IF par rapport à la taille du lot) 
      if 2<lot_quantity:
        return print("Error ! Double control is not possible! the lot size must be greater than 15 ")
      #------------------------------------------------------------------------------------        
      elif 2=<lot_quantit=<8:
        return print("Error, Double control is not possible! the lot size must be greater than 15 ")
      #------------------------------------------------------------------------------------
      elif 9=<lot_quantit=<15:
        return print("Error, Double control is not possible! the lot size must be greater than 15 ")
      #------------------------------------------------------------------------------------
      elif 16=<lot_quantit=<25:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] = [3,3]
        object_de_comunication['possible_nqa'] =[10,2.5]
          if nqa == 2.5:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 10:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 7.63
            object_de_comunication['crisk'] = 58.4
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10, 2.5] for this case ")
      #------------------------------------------------------------------------------------
      elif 26=<lot_quantit=<50:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] = [5,5]
        object_de_comunication['possible_nqa'] =[10,6.5,1.5]
          if nqa == 1.5:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 6.5:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 2.64
            object_de_comunication['crisk'] = 40.6
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 11.1
            object_de_comunication['crisk'] = 53.9
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,1.5] for this case ")
      #------------------------------------------------------------------------------------
      elif 51=<lot_quantit=<90:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] = [8,8]
        object_de_comunication['possible_nqa'] =[10,6.5,4,1]
          if nqa == 1:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 4:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 2.81
            object_de_comunication['crisk'] = 26.8
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 6.63
            object_de_comunication['crisk'] = 36
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = [1,4]
            object_de_comunication['rlimit'] = [4,5]
            object_de_comunication['frisk'] = 11.3
            object_de_comunication['crisk'] = 44.4
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,1] for this case ")
      #------------------------------------------------------------------------------------
      elif 91=<lot_quantit=<150:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] = [13,13]
        object_de_comunication['possible_nqa'] =[10,6.5,4,2.5,0.65]
          if nqa == 0.65:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 2.5:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 1.8
            object_de_comunication['crisk'] = 18.1
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 4.22
            object_de_comunication['crisk'] = 24.5
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = [1,4]
            object_de_comunication['rlimit'] = [4,5]
            object_de_comunication['frisk'] = 7.13
            object_de_comunication['crisk'] = 30.4
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = [2,6]
            object_de_comunication['rlimit'] = [5,7]
            object_de_comunication['frisk'] = 14
            object_de_comunication['crisk'] = 41.5
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,2.5,0.65] for this case ")
      #------------------------------------------------------------------------------------
      elif 151=<lot_quantit=<280:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] =32
        object_de_comunication['possible_nqa'] =[10,6.5,4,2.5,1.5,0.4]
          if nqa == 0.4:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 1.5:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 1.13
            object_de_comunication['crisk'] = 11.6
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 2.59
            object_de_comunication['crisk'] = 15.8
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = [1,4]
            object_de_comunication['rlimit'] = [4,5]
            object_de_comunication['frisk'] = 4.39
            object_de_comunication['crisk'] = 19.7
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = [2,6]
            object_de_comunication['rlimit'] = [5,7]
            object_de_comunication['frisk'] = 8.5
            object_de_comunication['crisk'] = 27.1
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = [3,8]
            object_de_comunication['rlimit'] = [7,9]
            object_de_comunication['frisk'] = 13.1
            object_de_comunication['crisk'] = 34.1
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,2.5,1.5,0.4] for this case ")
      #------------------------------------------------------------------------------------
      elif 281=<lot_quantit=<500:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] =[32,32]
        object_de_comunication['possible_nqa'] =[10,6.5,4,2.5,1.5,1,0.25]
          if nqa == 0.25:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 1:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 0.712
            object_de_comunication['crisk'] = 7.56
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 1.66
            object_de_comunication['crisk'] = 10.3
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = [1,4]
            object_de_comunication['rlimit'] = [4,5]
            object_de_comunication['frisk'] = 2.77
            object_de_comunication['crisk'] = 12.9
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = [2,6]
            object_de_comunication['rlimit'] = [5,7]
            object_de_comunication['frisk'] = 5.34
            object_de_comunication['crisk'] = 17.8
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = [3,8]
            object_de_comunication['rlimit'] = [7,9]
            object_de_comunication['frisk'] = 8.2
            object_de_comunication['crisk'] = 22.4
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = [5,12]
            object_de_comunication['rlimit'] = [9,13]
            object_de_comunication['frisk'] = 12.9
            object_de_comunication['crisk'] = 29.1
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,2.5,1.5,1,0.25] for this case ")
      #------------------------------------------------------------------------------------
      elif 501=<lot_quantit=<1200:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] =[50,50]
        object_de_comunication['possible_nqa'] =[10,6.5,4,2.5,1.5,1,0.65,0.15]
          if nqa == 0.15:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 0.65:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 0.444
            object_de_comunication['crisk'] = 4.78
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 1.03
            object_de_comunication['crisk'] = 6.52
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = [1,4]
            object_de_comunication['rlimit'] = [4,5]
            object_de_comunication['frisk'] = 1.73
            object_de_comunication['crisk'] = 8.16
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = [2,6]
            object_de_comunication['rlimit'] = [5,7]
            object_de_comunication['frisk'] = 3.32
            object_de_comunication['crisk'] = 11.3
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = [3,8]
            object_de_comunication['rlimit'] = [7,9]
            object_de_comunication['frisk'] = 5.06
            object_de_comunication['crisk'] = 14.2
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = [5,12]
            object_de_comunication['rlimit'] = [9,13]
            object_de_comunication['frisk'] = 7.91
            object_de_comunication['crisk'] = 18.6
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = [7,18]
            object_de_comunication['rlimit'] = [11,19]
            object_de_comunication['frisk'] = 11.9
            object_de_comunication['crisk'] = 24.2
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,2.5,1.5,1,0.65,0.15] for this case ")
      #------------------------------------------------------------------------------------
      elif 1201=<lot_quantit=<3200:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] =[80,80]
        object_de_comunication['possible_nqa'] =[10,6.5,4,2.5,1.5,1,0.65,0.4,0.1]
          if nqa == 0.1:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 0.4:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 0.284
            object_de_comunication['crisk'] = 3.11
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 0.654
            object_de_comunication['crisk'] = 4.26
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = [1,4]
            object_de_comunication['rlimit'] = [4,5]
            object_de_comunication['frisk'] = 1.09
            object_de_comunication['crisk'] = 5.35
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = [2,6]
            object_de_comunication['rlimit'] = [5,7]
            object_de_comunication['frisk'] = 2.09
            object_de_comunication['crisk'] = 7.42
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = [3,8]
            object_de_comunication['rlimit'] = [7,9]
            object_de_comunication['frisk'] = 3.19
            object_de_comunication['crisk'] = 9.42
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = [5,12]
            object_de_comunication['rlimit'] = [9,13]
            object_de_comunication['frisk'] = 4.94
            object_de_comunication['crisk'] = 12.3
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = [7,18]
            object_de_comunication['rlimit'] = [11,19]
            object_de_comunication['frisk'] = 7.4
            object_de_comunication['crisk'] = 16.1
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 10:
            object_de_comunication['alimit'] = [11,26]
            object_de_comunication['rlimit'] = [16,27]
            object_de_comunication['frisk'] = 11.9
            object_de_comunication['crisk'] = 22.5
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [10,6.5,4,2.5,1.5,1,0.65,0.4,0.1] for this case ")
      #------------------------------------------------------------------------------------
      elif 3201=<lot_quantit=<10000:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] =[125,125]
        object_de_comunication['possible_nqa'] =[6.5,4,2.5,1.5,1,0.65,0.4,0.25,0.065]
          if nqa == 0.065:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 0.25:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 0.178
            object_de_comunication['crisk'] = 1.95
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.4:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 0.409
            object_de_comunication['crisk'] = 2.66
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = [1,4]
            object_de_comunication['rlimit'] = [4,5]
            object_de_comunication['frisk'] = 0.683
            object_de_comunication['crisk'] = 3.34
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = [2,6]
            object_de_comunication['rlimit'] = [5,7]
            object_de_comunication['frisk'] = 1.31
            object_de_comunication['crisk'] = 4.64
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = [3,8]
            object_de_comunication['rlimit'] = [7,9]
            object_de_comunication['frisk'] = 1.99
            object_de_comunication['crisk'] = 5.89
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = [5,12]
            object_de_comunication['rlimit'] = [9,13]
            object_de_comunication['frisk'] = 3.09
            object_de_comunication['crisk'] = 7.7
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = [7,18]
            object_de_comunication['rlimit'] = [11,19]
            object_de_comunication['frisk'] = 4.62
            object_de_comunication['crisk'] = 10.1
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 6.5:
            object_de_comunication['alimit'] = [11,26]
            object_de_comunication['rlimit'] = [16,27]
            object_de_comunication['frisk'] = 7.45
            object_de_comunication['crisk'] = 14.1
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [6.5,4,2.5,1.5,1,0.65,0.4,0.25,0.065] for this case ")
      #------------------------------------------------------------------------------------
      elif 10001=<lot_quantit=<35000:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] =[200,200]
        object_de_comunication['possible_nqa'] =[4,2.5,1.5,1,0.65,0.4,0.25,0.15,0.04]
          if nqa == 0.04:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 0.15:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 0.112
            object_de_comunication['crisk'] = 1.23
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.25:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 0.259
            object_de_comunication['crisk'] = 1.69
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.4:
            object_de_comunication['alimit'] = [1,4]
            object_de_comunication['rlimit'] = [4,5]
            object_de_comunication['frisk'] = 0.433
            object_de_comunication['crisk'] = 2.12
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = [2,6]
            object_de_comunication['rlimit'] = [5,7]
            object_de_comunication['frisk'] = 0.829
            object_de_comunication['crisk'] = 2.94
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = [3,8]
            object_de_comunication['rlimit'] = [7,9]
            object_de_comunication['frisk'] = 1.26
            object_de_comunication['crisk'] = 3.74
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = [5,12]
            object_de_comunication['rlimit'] = [9,13]
            object_de_comunication['frisk'] = 1.96
            object_de_comunication['crisk'] = 4.89
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = [7,18]
            object_de_comunication['rlimit'] = [11,19]
            object_de_comunication['frisk'] = 2.94
            object_de_comunication['crisk'] = 6.39
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 4:
            object_de_comunication['alimit'] = [11,26]
            object_de_comunication['rlimit'] = [16,27]
            object_de_comunication['frisk'] = 4.73
            object_de_comunication['crisk'] = 8.95
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [4,2.5,1.5,1,0.65,0.4,0.25,0.15,0.04] for this case ")
      #------------------------------------------------------------------------------------
      elif 35001=<lot_quantit=<150000:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] =[315,315]
        object_de_comunication['possible_nqa'] =[2.5,1.5,1,0.65,0.4,0.25,0.15,0.1,0.025]
          if nqa == 0.025:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 0.1:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 0.071
            object_de_comunication['crisk'] = 0.778
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.15:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 0.164
            object_de_comunication['crisk'] = 1.06
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.25:
            object_de_comunication['alimit'] = [1,4]
            object_de_comunication['rlimit'] = [4,5]
            object_de_comunication['frisk'] = 0.273
            object_de_comunication['crisk'] = 1.34
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.4:
            object_de_comunication['alimit'] = [2,6]
            object_de_comunication['rlimit'] = [5,7]
            object_de_comunication['frisk'] = 0.523
            object_de_comunication['crisk'] = 1.86
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = [3,8]
            object_de_comunication['rlimit'] = [7,9]
            object_de_comunication['frisk'] = 0.796
            object_de_comunication['crisk'] = 2.35
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = [5,12]
            object_de_comunication['rlimit'] = [9,13]
            object_de_comunication['frisk'] = 1.23
            object_de_comunication['crisk'] = 3.08
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = [7,18]
            object_de_comunication['rlimit'] = [11,19]
            object_de_comunication['frisk'] = 1.85
            object_de_comunication['crisk'] = 4.03
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 2.5:
            object_de_comunication['alimit'] = [11,26]
            object_de_comunication['rlimit'] = [16,27]
            object_de_comunication['frisk'] = 2.98
            object_de_comunication['crisk'] = 5.64
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [2.5,1.5,1,0.65,0.4,0.25,0.15,0.1,0.025] for this case ")
      #------------------------------------------------------------------------------------
      elif 150001=<lot_quantit=<500000:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] =[500,500]
        object_de_comunication['possible_nqa'] =[1.5,1,0.65,0.4,0.25,0.15,0.1,0.065,0.015]
          if nqa == 0.015:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 0.065:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 0.044
            object_de_comunication['crisk'] = 0.468
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.1:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 0.102
            object_de_comunication['crisk'] = 0.665
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.15:
            object_de_comunication['alimit'] = [1,4]
            object_de_comunication['rlimit'] = [4,5]
            object_de_comunication['frisk'] = 0.171
            object_de_comunication['crisk'] = 0.835
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.25:
            object_de_comunication['alimit'] = [2,6]
            object_de_comunication['rlimit'] = [5,7]
            object_de_comunication['frisk'] = 0.327
            object_de_comunication['crisk'] = 1.16
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.4:
            object_de_comunication['alimit'] = [3,8]
            object_de_comunication['rlimit'] = [7,9]
            object_de_comunication['frisk'] = 0.498
            object_de_comunication['crisk'] = 3.47
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = [5,12]
            object_de_comunication['rlimit'] = [9,13]
            object_de_comunication['frisk'] = 0.771
            object_de_comunication['crisk'] = 1.93
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = [7,18]
            object_de_comunication['rlimit'] = [11,19]
            object_de_comunication['frisk'] = 1.16
            object_de_comunication['crisk'] = 2.52
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1.5:
            object_de_comunication['alimit'] = [11,26]
            object_de_comunication['rlimit'] = [16,27]
            object_de_comunication['frisk'] = 1.86
            object_de_comunication['crisk'] = 3.52
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [1.5,1,0.65,0.4,0.25,0.15,0.1,0.065,0.015] for this case ")
      #------------------------------------------------------------------------------------
      else:
        object_de_comunication['type'] = 'double'
        object_de_comunication['nsample'] =[800,800]
        object_de_comunication['possible_nqa'] =[1,0.65,0.4,0.25,0.15,0.1,0.065,0.04,0.01]
          if nqa == 0.01:
            return print("Error, This NQA is not possible for this case ! ")
          elif nqa == 0.04:
            object_de_comunication['alimit'] = [0,1]
            object_de_comunication['rlimit'] = [2,2]
            object_de_comunication['frisk'] = 0.028
            object_de_comunication['crisk'] = 0.310
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.065:
            object_de_comunication['alimit'] = [0,3]
            object_de_comunication['rlimit'] = [3,4]
            object_de_comunication['frisk'] = 0.065
            object_de_comunication['crisk'] = 0.426
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.1:
            object_de_comunication['alimit'] = [1,4]
            object_de_comunication['rlimit'] = [4,5]
            object_de_comunication['frisk'] = 0.109
            object_de_comunication['crisk'] = 0.534
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.15:
            object_de_comunication['alimit'] = [2,6]
            object_de_comunication['rlimit'] = [5,7]
            object_de_comunication['frisk'] = 0.209
            object_de_comunication['crisk'] = 0.742
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.25:
            object_de_comunication['alimit'] = [3,8]
            object_de_comunication['rlimit'] = [7,9]
            object_de_comunication['frisk'] = 0.318
            object_de_comunication['crisk'] = 0.942
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.4:
            object_de_comunication['alimit'] = [5,12]
            object_de_comunication['rlimit'] = [9,13]
            object_de_comunication['frisk'] = 0.494
            object_de_comunication['crisk'] = 1.23
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 0.65:
            object_de_comunication['alimit'] = [7,18]
            object_de_comunication['rlimit'] = [11,19]
            object_de_comunication['frisk'] = 0.74
            object_de_comunication['crisk'] = 1.61
            object_de_comunication['advice'] = 'not implemented yet'
          elif nqa == 1:
            object_de_comunication['alimit'] = [11,26]
            object_de_comunication['rlimit'] = [16,27]
            object_de_comunication['frisk'] = 1.19
            object_de_comunication['crisk'] = 2.25
            object_de_comunication['advice'] = 'not implemented yet'
          else:
            return print("Error, NQA must be equal to [1,0.65,0.4,0.25,0.15,0.1,0.065,0.04,0.01] for this case ")
      #Fin if------------------------------------------------------------------------------------        
      
    else:
      return print("Error, This type of control s not available ! ")
    #Fin if------------------------------------------------------------------------------------
    
    return object_de_comunication
    
    """



    elif type=="double":
      object_de_comunication = {
            'type': 'double',
            'nsample': [],
            'alimit': [],
            'rlimit':[],
            'frisk':0,
            'crisk':0,
            'possible_nqa':[],
            'advice': 'not implemented yet'      
              }
      ns1 = 100
      object_de_comunication['nsample'].append(ns1)
      ns2 = 500
      object_de_comunication['nsample'].append(ns2)

      # object_de_comunication['nsample'] = [ns1,ns2]

      

      
      return object_de_comunication


if N<2:
      print("Le lot doit avoir un nombre de pièces supérieur à 2")
elif 2=<N=<8:
  NQA = [6.5]
elif 9=<N=<15:
  NQA = [4]
elif 16=<N=<25:
  NQA = [10,2.5]
elif 26=<N=<50:
  NQA = [10,6.5,1.5]
elif 51=<N=<90:
  NQA = [10,6.5,4,1]
elif 91=<N=<150:
  NQA = [10,6.5,4,2.5,0.65]
elif 151=<N=<280:
  NQA = [10,6.5,4,2.5,1.5,0.4]
elif 281=<N=<500:
  NQA = [10,6.5,4,2.5,1.5,1,0.25]
elif 501=<N=<1200:
  NQA = [10,6.5,4,2.5,1.5,1,0.65,0.15]
elif 1201=<N=<3200:
  NQA = [10,6.5,4,2.5,1.5,1,0.65,0.4,0.1]
elif 3201=<N=<10000:
  NQA = [6.5,4,2.5,1.5,1,0.65,0.4,0.25,0.065]
elif 10001=<N=<35000:
  NQA = [4,2.5,1.5,1,0.65,0.4,0.25,0.15,0.04]
elif 35001=<N=<150000:
  NQA = [2.5,1.5,1,0.65,0.4,0.25,0.15,0.1,0.025]
elif 150001=<N=<500000:
  NQA = [1.5,1,0.65,0.4,0.25,0.15,0.1,0.065,0.015]
else:
  NQA = [1,0.65,0.4,0.25,0.15,0.1,0.065,0.04,0.01]

  """