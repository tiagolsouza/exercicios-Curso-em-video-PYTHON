import time

class tTabela:
    def __init__(self):
        self.dados = []
        
    def load_from_file(self,filename):
        f = open(filename,"r")
        for line in f:
            dado_lido = line.split()
            dado_lido.append(int(dado_lido[4]))
            self.dados.append(dado_lido)
        f.close()
        self.n = len(self.dados)

    def save_to_file(self,filename):
        f = open(filename,"w")
        for dado in self.dados:
            f.write("\n % -8s % -30s % -4s % -8s % -10s % 10d" %
                    (dado[0],dado[1],dado[2],dado[3],dado[4],dado[5]))
        f.close()    

    def selection_sort(self,col,ordem):
        t1 = time.time()
        if ordem == "a":
            for i in range(self.n):
                jmin = i
                for j in range(i+1,self.n):
                    if self.dados[j][col] < self.dados[jmin][col]:
                        jmin = j
                if jmin != i:
                    aux = self.dados[i]
                    self.dados[i] = self.dados[jmin]
                    self.dados[jmin] = aux
        elif ordem == "d":
            for i in range(self.n):
                jmax = i
                for j in range(i+1,self.n):
                    if self.dados[j][col] > self.dados[jmax][col]:
                        jmax = j
                if jmax != i:
                    aux = self.dados[i]
                    self.dados[i] = self.dados[jmax]
                    self.dados[jmax] = aux
        t2 = time.time()
        print("CPU time = ",t2-t1)

    def ms(self,values,col,ordem):
        if len(values) > 1: 
            m = len(values)//2
            left = values[:m] 
            right = values[m:] 
            left = self.ms(left,col,ordem) 
            right = self.ms(right,col,ordem)
            
            values =[] 
  
            if ordem == "a":
                while len(left) > 0 and len(right) > 0: 
                    if left[0][col] < right[0][col]: 
                        values.append(left[0]) 
                        left.pop(0)
                    else: 
                        values.append(right[0]) 
                        right.pop(0)
            elif ordem == "d":
                while len(left) > 0 and len(right) > 0: 
                    if left[0][col] >= right[0][col]: 
                        values.append(left[0]) 
                        left.pop(0)
                    else: 
                        values.append(right[0]) 
                        right.pop(0)  
            for i in left:
                values.append(i)
            for i in right:
                values.append(i)                      
        return values
    
    def merge_sort(self,col,ordem):
        t1 = time.time()
        lista = self.dados[:]
        lista = self.ms(lista,col,ordem)
        self.dados = lista[:]
        t2 = time.time()
        print("CPU time = ",t2-t1)

    def filtrar(self,col,valor):
        v = tTabela()
        for i in self.dados:
            if i[col] == valor:
                v.dados.append(i)
        return v
    
    def distintos(self,col):
        v = list()
        for d in self.dados:
            v.append(d[col])
        v = list(dict.fromkeys(v))
        return v
            

