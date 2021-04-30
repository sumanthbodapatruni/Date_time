'''
28/4/2021
B Sumanth
create two classes of birds and animals with their features
read the input from user
check which category it belongs 
display the name of category and its feature
'''

query=input('Enter animal or bird name')
class Birds:
    
    def Bird(self):
        B={'Crow':'Black',
           'Parrot':'Green',
           'Pigeon':'White',
           'Sparrow':'Brown',
           'Chick':'Yellow'
           }

        for k in B:
            if k==query:
                print(query +' belongs to Bird category')
                print(query+' colour is '+B[query])
        

class Animals:
    def Domestic_Animals(self):
        D={'Dog':'Brown',
           'Cat':'Black',
           'Sheep':'White',
           'Goat':'Brown',
           'Horse':'Black',
           }
        for i in D:
            if i==query:
                print(query+' belongs to Domestic_Animal category')
                print(query+' colour is '+D[query])
            
           
    def Wild_Animals(self):
        W={'Lion':'Brown',
           'Tiger':'Yellow',
           'Bear':'Black',
           'Cheetah':'Black',
           'Kangaroo':'Brown'}
        
        for j in W:
            if j==query:
                print(query+' belongs to Wild_Animal category')
                print(query+' colour is '+W[query])
        
              
                
class Creatures(Animals,Birds):
      Birds.Bird(query)
      Animals.Domestic_Animals(query)
      Animals.Wild_Animals(query)
        
                
A=Creatures()  



