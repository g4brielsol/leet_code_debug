import numpy as np

def PALU(A):
    print("A ", A)
    print()
    # linhas
    n = A.shape[0]
    print("n ", n)
    # lista do 0 ate o valor de n-1, exemplo: n = 4, p = [0,1,2,3] 
    p = list(range(n))
    print("pppppppppppppppppppppp ", p)
    # faz copia do A
    LU = A.copy()
    print("LU ", LU)
    print()

    for i in range (n):
        print("iiiiiiiiiiiiiiiiiiii = ", i)
        # np.abs() transforma todos numeros negativos em positivos
        # np.argmax() retorna o indice da matriz que possui o numero maior, 
        # ex: para a "matriz" [1,4] vai retornar 1 pq o indice 1 ta relacionado ao elemento 4, 
        # o indice 0 ao elemento 1
        I = i + np.argmax(np.abs(LU[i:,i]))
        print("i = {}, I = {} ".format(i, I))
        print("np.abs(LU[i:,i]) ", np.abs(LU[i:,i]))
        print("np.argmax(np.abs(LU[i:,i])) ", np.argmax(np.abs(LU[i:,i])))
        #qtd_zero = len(LU[0, :]) - len(np.abs(LU[i:,i])
        # pega a linha i da matriz
        tmp = LU[i,:].copy()
        print("tmp ", tmp)
        print()
        # transforma a linha i da matriz na linha I
        LU[i,:] = LU[I,:]
        print("LU[i,:] ", LU[i,:])
        print()
        # transforma a linha I na linha i, que foi copiada na variavel tmp
        #if i > 0:
        #    LU[I,:] = tmp - LU[i,i] / LU[i,i]#- LU[0, 0]  
        #else:
        LU[I,:] = tmp
        print("LU[I,:] ", LU[I,:])
        print()
        # copia o elemento do indice i do vetor p na variavel tmp
        tmp = p[i] #- 1
        print("tmp ", tmp)
        # troca o elemento do indice i pelo elemento do indice I
        p[i] = p[I] 
        print("p[i] ", p[i])
        # troca o elemento do indice I pelo elemento do indice i copiado na variavel tmp
        p[I] = tmp
        print("p[I] ", p[I])
        print()

        #for k in range (i+1,n):
        #print("k = {}, i = {}".format(k,i))
        print("k = {}, i = {}".format(i+1,i))
        # faz o elemento do indice k,i da matriz ser igual a divisao do elemento k,i
        # pelo elemento i,i
        #LU[k,i] = LU[k,i] / LU[i,i]
        if i+1 < n:
            print("LU, ", LU)
            LU[i+1,i] = LU[i+1,i] / LU[i,i]
            #print('LU[k,i] ', LU[k,i])
            print('LU[k,i] ', LU[i+1,i])
            print()

            #for j in range (i+1,n):
                #print("k = {}, i = {}, j = {}".format(k,i,j))
            # subtrai do elemento k,j o resultado da multiplicacao entre k,i e i,j
                #LU[k,j] -= LU[k,i] * LU[i,j]
            #LU[k, i+1:n] -= LU[k, i] * LU[i, i+1:n]
        if i > 0 and i < n:
            print("k = {}, i = {}, j = {}".format(i+1,i,i+1))
            LU[i, :len(p[])] -= LU[i+1, i] * LU[i, i:n]# + i
            #print("LU[k,j] ", LU[k,j])
            print("LU[k,j] ", LU[i+1,i+1:n])
        print()
    return (p, LU)

#A = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
A = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
result = PALU(A)
print()
# valor de p = result[0], para o valor de A = np.array([[1,2,3], [4,5,6]]),
# o valor de p = [1,0]
print(result[0])
print()
# valor de LU = result[1], para o valor de A = np.array([[1,2,3], [4,5,6]]),
# o valor de LU = [[4 5 6], [0 2 3]]
print(result[1])