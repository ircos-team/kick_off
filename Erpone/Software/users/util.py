

"""Les NQA autorisés par rapport à la taille du lot"""

def function (lot_quantity, nqa, type):
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