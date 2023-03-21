
T = int(input())

for i in range(T):
    N = str(input())
    lista = N.split()
    N=int(lista[0])
    K=int(lista[1]) 
    print((N % K) + (N // K))
    
# T = int(input())
# for i in range(T):
#   N = int(input())
#   K = int(input())
#   print((N % K) + (N // K))
      
    