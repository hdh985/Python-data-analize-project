import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

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
    
        if command == "살인":
            
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


class  Analize(Fictional):

    def __init__(self):
        super().__init__()
        
    def show_graph(self, command):

        value_dict = self.sorting(command)
        
        if command == "발생":
            
            x = list(value_dict.keys())
            y = []
            
            for i in value_dict:

                y.append(float(value_dict.get(i)))
            plt.title("서울시 구별 5대 범죄 발생 그래프", fontsize = 20)
            plt.ylabel("발생 수", fontsize = 18)
            plt.xlabel("서울시 구",fontsize = 18)
            plt.bar(x, y, color = "green")
            plt.show()

        elif command == "검거":

            x = list(value_dict.keys())
            y = []

            for i in value_dict:
                y.append(float(value_dict.get(i)))
            plt.title("서울시 구별 5대 범죄 검거 그래프", fontsize = 20)
            plt.ylabel("검거 수", fontsize = 18)
            plt.xlabel("서울시 구",fontsize = 18)
            plt.bar(x, y, color = "pink")
            plt.show()
    
        elif command == "살인":

            label = list(value_dict.keys())

            occur = []           
            arrest = []

            x = np.arange(len(label))
            plt.xticks(x, label)
            for i in value_dict:
                value = value_dict.get(i)
                occur.append(float(value[0]))
                arrest.append(float(value[1]))

            g_1 = plt.bar(x - 0.0 , occur, width = 0.3 , color = "blue")
            g_2 = plt.bar(x + 0.3, arrest, width = 0.3, color = "red")
            plt.title("서울시 구별 살인 발생/검거 그래프",fontsize = 20)
            plt.legend((g_1[0], g_2[0]), ("발생", "검거"), fontsize = 15)
            plt.ylabel("사건 수", fontsize = 18)
            plt.xlabel("서울시 구",fontsize = 18)
            plt.show()

        elif command == "강도":
            label = list(value_dict.keys())
            occur = []           
            arrest = []
            x = np.arange(len(label))
            plt.xticks(x, label)

            for i in value_dict:
                value = value_dict.get(i)
                occur.append(float(value[0]))
                arrest.append(float(value[1]))

            g_1 = plt.bar(x - 0.0 , occur, width = 0.3 , color = "blue")
            g_2 = plt.bar(x + 0.3, arrest, width = 0.3, color = "red")

            plt.title("서울시 구별 강도 발생/검거 그래프",fontsize = 20)
            plt.legend((g_1[0], g_2[0]), ("발생", "검거"), fontsize = 15)
            plt.ylabel("사건 수", fontsize = 18)
            plt.xlabel("서울시 구",fontsize = 18)
            plt.show()            
        
        elif command == "강간" or command == "강제추행":
            label = list(value_dict.keys())
            occur = []           
            arrest = []
            x = np.arange(len(label))
            plt.xticks(x, label)

            for i in value_dict:
                value = value_dict.get(i)
                occur.append(float(value[0]))
                arrest.append(float(value[1]))

            g_1 = plt.bar(x - 0.0 , occur, width = 0.3 , color = "blue")
            g_2 = plt.bar(x + 0.3, arrest, width = 0.3, color = "red")

            plt.title("서울시 구별 강간(강제추행) 발생/검거 그래프",fontsize = 20)
            plt.legend((g_1[0], g_2[0]), ("발생", "검거"), fontsize = 15)
            plt.ylabel("사건 수", fontsize = 18)
            plt.xlabel("서울시 구",fontsize = 18)
            plt.show()

        elif command == "절도":
            label = list(value_dict.keys())
            occur = []           
            arrest = []
            x = np.arange(len(label))
            plt.xticks(x, label)

            for i in value_dict:
                value = value_dict.get(i)
                occur.append(float(value[0]))
                arrest.append(float(value[1]))

            g_1 = plt.bar(x - 0.0 , occur, width = 0.3 , color = "blue")
            g_2 = plt.bar(x + 0.3, arrest, width = 0.3, color = "red")

            plt.title("서울시 구별 절도 발생/검거 그래프",fontsize = 20)
            plt.legend((g_1[0], g_2[0]), ("발생", "검거"), fontsize = 15)
            plt.ylabel("사건 수", fontsize = 18)
            plt.xlabel("서울시 구",fontsize = 18)
            plt.show()
        
        elif command == "폭력":
            label = list(value_dict.keys())
            occur = []           
            arrest = []
            x = np.arange(len(label))
            plt.xticks(x, label)

            for i in value_dict:
                value = value_dict.get(i)
                occur.append(float(value[0]))
                arrest.append(float(value[1]))

            g_1 = plt.bar(x - 0.0 , occur, width = 0.3 , color = "blue")
            g_2 = plt.bar(x + 0.3, arrest, width = 0.3, color = "red")

            plt.title("서울시 구별 폭력 발생/검거 그래프",fontsize = 20)
            plt.legend((g_1[0], g_2[0]), ("발생", "검거"), fontsize = 15)
            plt.ylabel("사건 수", fontsize = 18)
            plt.xlabel("서울시 구",fontsize = 18)
            plt.show()


p = Analize()

print(p.show_graph("폭력"))



    
    


                





        

        