'''
28/4/2021
B Sumanth
create two classes of birds and animals with their features
read the input from user
check which category it belongs 
display the name of category and its feature
'''

query=input('Enter animal or bird name') # user input-animal name or bird name
class Birds:                             # created a class for birds
    
    def Bird(self,query):                      # defining a function for birds category
        Bird_dict={'Crow':'Black',       # dictionsry of birds with their colour
           'Parrot':'Green',
           'Pigeon':'White',
           'Sparrow':'Brown',
           'Chick':'Yellow'
           }

        for k in Bird_dict:              # for loop to go through all elements of dictionary
            if k==query:                 # checking the given input is in the dictionary or not
                print(query +' belongs to Bird category' )   # if in the dict,,prints that it belongs to this bird category
                print()
                print(query)
                print(query+' colour is '+Bird_dict[query]) # printing the available bird's colour
        

class Animals:                          # creating a class for animals
    def Domestic_Animals(self,query):         # defining a function for domestic animals
        Domest_dict={'Dog':'Brown',     # dictionary of domestic animals with their colour
           'Cat':'Black',
           'Sheep':'White',
           'Goat':'Brown',
           'Horse':'Black',
           }
        for i in Domest_dict:            # for loop to go through all elements of dictionary
            if i==query:                 # checking the given input is in the dictionary or not
                print(query+' belongs to Domestic_Animal category') # if in the dict,,prints that it belongs to this domestic animal category
                print(query+ ' belongs to animal category')
                print()
                print(query)
                print(query+' colour is '+Domest_dict[query])
            
           
    def Wild_Animals(self,query):              # defining a function for wild animals  
        Wild_dict={'Lion':'Brown',       # dictionary of domestic animals with their colour
           'Tiger':'Yellow',
           'Bear':'Black',
           'Cheetah':'Black',
           'Kangaroo':'Brown'}
        
        for j in Wild_dict:              # for loop to go through all elements of dictionary
            if j==query:                 # checking the given input is in the dictionary or not
                print(query+' belongs to Wild_Animal category') # if in the dict,,prints that it belongs to this wild animal category
                print()
                print(query)
                print(query+' colour is '+Wild_dict[query])
        
              
                
class Creatures(Animals,Birds):         # create class for inherting above classes 
      
    def __init__(self,query):
      super().Bird(query)                 # calling bird function from birds class
      super().Domestic_Animals(query)   # calling Domestic animals function from animals class
      super().Wild_Animals(query)       # calling wild animals function from animals class
        
                
A=Creatures(query)                           # calling the creatures class


