
nterms = input("Fibonacci sequence upto: ")
nstr = int(nterms)


n1 = 0
n2 = 1
count = 0

if(nstr>=0) :
   print("Fibonacci sequence upto :")
   while count < nstr:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1