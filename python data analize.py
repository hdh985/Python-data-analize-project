import numpy as np
import pandas as pd
import matplotlib as plt

df = pd.read_csv("C:\\Users\\82108\\Downloads\\criminal_file.csv", skiprows = 2)

df = df.drop(columns= "자치구별(1)") 


class Fictional:
    
    def __init__(self):
        
        
        self.all = {}
        self.murder = {}
        self.thief = {}
        self.rape = {}
        self.theft = {}
        self.violence = {}
        self.occur = {}
        self.arrest = {}
        
    def sorting(self, command):
    
            
        if command == "전체":
            
            for i in range(2, 27):
        
                
                self.all[df.loc[i][0]] = [df.loc[i][1], df.loc[i][2]]
            
            return self.all
        
        elif command == "살인":
            
            for i in range(2, 27):
                
                self.murder[df.loc[i][0]] = [df.loc[i][3], df.loc[i][4]]
                
            return self.murder
        
        elif command == "강도":
            
            for i in range(2, 27):
                
                self.thief[df.loc[i][0]] = [df.loc[i][5], df.loc[i][6]]
                
            return self.thief
            
        elif command == "강간" or command == "강제추행":
            
            
            for i in range(2, 27):
                
                self.rape[df.loc[i][0]] = [df.loc[i][7], df.loc[i][8]]
                
            return self.rape
            
        elif command == "절도":
            
            
            for i in range(2, 27):
                
                self.theft[df.loc[i][0]] = [df.loc[i][9], df.loc[i][10]]
                
            return self.theft
        
        
        elif command == "폭력":
            
            
            for i in range(2, 27):
                
                self.violence[df.loc[i][0]] = [df.loc[i][11], df.loc[i][12]]
                
            return self.violence


        elif command == "발생":

            for i in range(2,27):

                self.occur[df.loc[i][0]] = df.loc[i][1]

            return self.occur

        elif command == "검거":

            for i in range(2, 27):
                
                self.arrest[df.loc[i][0]] = df.loc[i][2]

            return self.arrest


ch = Fictional()
print(ch.sorting("발생"))

class  Analize(Fictional):

    def __init__(self, name):
        super().__init__(self)
        
        self.name = name


    def occurrence_g(self):
        pass
    
    


                





        

        