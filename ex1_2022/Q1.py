
def safe_call(f,**kwargs):
      if f is None:
          return
      dict=f.__annotations__
      for x,y in kwargs.items():
          if x in dict:
              if type(y)!=dict[x]:
                  print(y,x,type(y),dict[x])
                  raise print("The variables doesnt match")
      return f(**kwargs)
def f(x: int, y: float, z):
    print(x+y+z)
    return x+y+z
if __name__ == '__main__':
    safe_call(f,x=5,y=7.0,z=3) #should return 15.0
    safe_call(f, x=5, y="acb", z=3) #should raise an exception
    safe_call(f, x=1, y=-1.0, z=2.0)#should return 2.0





