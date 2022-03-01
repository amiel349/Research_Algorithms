# i got help from https://www.youtube.com/watch?v=szQUIRPrAgQ
import math


def find_root(f,min,max):
    iterations=1000 # limit the iterations for fail case
    tolerance=0.0000001 # number for approximation
    for i in range(iterations):
        root=max-f(max)/d_fun(f,max)
        if abs(root-max)<tolerance:
            break
        max=root
    return max

def d_fun(fun,x): # function to find the derivative for f
    h = 0.0000000001
    return (fun(x+h)-fun(x-h))/(2*h)




if __name__ == '__main__':
   print(find_root(lambda x:(x-4)*(x+2),2,5)) # should print 4
   print(find_root(lambda x: math.sin(x), 0, 1))  # should print 2
   print(find_root(lambda x: math.sqrt(x)-3, 6, 10))  # should print 9
   print(find_root(lambda x: (x - 4) * (x + 2), 2, 5))

