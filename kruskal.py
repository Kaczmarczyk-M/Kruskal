import numpy as np

def sprawdz(A,B,C): #A - lista węzłów, B - m.połączeń, C- m.wag
    if B.shape == C.shape and B.shape[0] == B.shape[1] and C.shape[0] == C.shape[1] and len(A)  == B.shape[0]:
        return tuple([A, B, C])
    else:
        raise Exception("Nie spełnia warunków")

def skierowany1(B): # B - m.połączeń, C- m.wag
    if (np.transpose(B) == B).sum() == B.shape[0] * B.shape[1]:
        return True
    else:
        return False
     
def dajkrawedzie(G):
    listakrawedzi = []
    for i in range(len(G[0])): 
        for j in range(i, len(G[0])): 
            if G[1][j][i] == 1: 
                listakrawedzi.append(tuple([ G[2][i][j], i, j ])) # [waga/ile tam potrzeba żeby dotrzeć, wezeł początkowy, w. końcowy]
    return listakrawedzi

def quickSort(A, p, r):
    licz=0
    if p < r:
        q,licz = partition(A, p, r)
        licz+=quickSort(A, p, q)
        licz+=quickSort(A, q + 1, r)
    return licz

def partition(A, p, r):
    x = A[p][0]
    i = p-1
    j = r+1
    l=0
    while True:

        j-=1
        while A[j][0] > x:
            j = j - 1
            l+=1
        i = i + 1
        while A[i][0] < x:
            i = i + 1
            l += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return [j, l]

def kruskal(lista_wezlow, macierz_polaczen, waga_galezi):
    if skierowany1(macierz_polaczen):
        Krawedzie = dajkrawedzie(sprawdz(lista_wezlow, macierz_polaczen, waga_galezi))
        quickSort(Krawedzie, 0, len(Krawedzie) - 1)

        lista = []
        for i in range(0, len(Krawedzie)):
            if Krawedzie[i][1] in lista and Krawedzie[i][2] in lista:
                pass
            else:
                lista.append((Krawedzie[i][1], Krawedzie[i][2]))
        return lista


if __name__ == "__main__":

    lista_wezlow=['A','B','C','D']
    macierz_polaczen=np.array([
        (0,1,0,0),
        (1,0,1,1),
        (0,1,0,1),
        (0,1,1,0)])
    waga_galezi=np.array([
        (0,5,0,0),
        (5,0,3,4),
        (0,3,0,2),
        (0,4,2,0)])

    print(kruskal(lista_wezlow, macierz_polaczen, waga_galezi))

    # lista_wezlow=('A','B','C','D')
    # macierz_polaczen=np.array((
    #             [[0,1,1,0],
    #             [1,0,0,1],
    #             [1,0,0,0],
    #             [0,1,0,0]]))
    # waga_galezi=np.array(([
    #       [0, 2, 1, 0],
    #       [2, 0, 0, 3],
    #       [1, 0, 0, 0],
    #       [0, 3, 0, 0]]))