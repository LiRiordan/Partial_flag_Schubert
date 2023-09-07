from itertools import permutations
from itertools import combinations

def aggre(i):
    s = ''
    for j in i:
        s += j
    return s


def sfroml(L):
    st = ''
    for i in L:
        st += i
    return st

class Comb_Schub_init():
    def __init__(self,J,n):
        self.J = sorted(J,reverse=True)
        self.n = n
        exten = [self.n] + self.J + [0]
        self.char = ''
        for i in range(len(exten) - 1):
            for _ in range(exten[i] - exten[i+1]):
                self.char += f'{len(exten[:i])}'
        self.Schub_num = len(set(permutations(self.char)))
        self.Schub = list(set(permutations(self.char)))







class singular():
    def __init__(self,a):
        self.a = a
        self.sing = self.pattern_avoidance(self.a)

    def levels(self,i):
        Output = []
        max = sorted(i,reverse=True)[0]
        Max = int(max)
        for j in range(Max+1,0,-1):
            P = []
            for k in range(len(i)):
                if int(i[k]) == j-1:
                    P.append(k)
            Output += sorted(P,reverse=True)
        return Output

    def index_gen(self,L):
        List = self.levels(L)
        ind = [0 for _ in range(len(List))]
        M = [[i,j] for (i,j) in zip(range(len(L)),List)]
        for k in range(len(M)):
            ind[M[k][1]] = M[k][0] + 1
        return ind

    def ind_flattener(self,i):
        T = [0,0,0,0]
        M = [0,1,2,3]
        G = [[l,k] for (l,k) in zip(M,i)]
        G = sorted(G,key = lambda x : x[1])
        for s in M:
            T[G[s][0]] = s + 1
        return T

    def pattern_avoidance(self,i):
        output = False
        ind = self.index_gen(i)
        T = [i for i in range(len(i))]
        for j in combinations(T,4):
            P = [ind[j[l]] for l in range(4)]
            M = self.ind_flattener(P)
            if M == [4, 2, 3, 1]:
                output = True
            if M == [3, 4, 1, 2]:
                output = True
        return output




class Schub_struct():
    def __init__(self,J,n):
        self.J = J
        self.n = n
        self.M = Comb_Schub_init(J,n)
        self.decomposition = self.split(self.M.Schub)




    def length(self,a):
        counter = 0
        for i in range(len(a)-1):
            for j in range(len(a[i+1:])):
                if a[i] < a[i+1+j]:
                    counter +=1
        return  counter

    def len_list(self,L,k):
        B = []
        for i in L:
            if self.length(i) == k:
                M = singular(sfroml(i))
                if M.sing == True:
                    B.append(['Sing' + sfroml(i)])
                else:
                    B.append(sfroml(i))
        return B
    def split(self,L):
        Dec = []
        for i in range(len(L)*(len(L)+1)):
            if self.len_list(L,i) != []:
                p = [f'dimension = {i}']
                p.append(self.len_list(L,i))
                Dec += [p]
        for j in Dec:
            print(j)
            print('\n---------------------------------')


def per(a,n):
    t = [i+1 for i in range(n)]
    while len(a) > 0:
        t[a[-1]-1], t[a[-1]] = t[a[-1]], t[a[-1]-1]
        del a[-1]
    return t














