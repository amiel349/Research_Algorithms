#i got help from https://stackoverflow.com/questions/11089655/sorting-dictionary-python-3
def sort_dict(x): #recursive sort for dictionary

    x = {k: x[k] for k in sorted(x)}
    for z,y in x.items():
        x[z]=print_sorted_wrap(y)
    return x

def sort_set(x): #recursive sort for set
    for y in x.items():
        y==print_sorted_wrap(y)
    try:
        x = sorted(x)
    except:
        print("error")
    return x

def sort_list(x):#recursive sort for list
    for i in range(len(x)):
        x[i]=print_sorted_wrap(x[i])
    try:
        x = sorted(x)
    except:
        print("error")
    return x

def sort_tuple(x): #recursive sort for tuple
    for y in x:
      y= print_sorted_wrap(y)
    try:
     x = sorted(x)
    except:
      print("error")
    return x

def print_sorted_wrap(x): #wrap function for the sort- call every sort by the instance
    if isinstance(x,dict):
        x=sort_dict(x)
    elif isinstance(x,set):
        x=sort_set(x)
    elif isinstance(x,list):
        x=sort_list(x)
    elif isinstance(x,tuple):
        x=sort_tuple(x)
    return x

def print_sorted(x):
    x=print_sorted_wrap(x)
    print(x)
if __name__ == '__main__':
    print_sorted({"a":5,"c":6,"b":[1,3,2,4]}) #should print {'a': 5, 'b': [1, 2, 3, 4], 'c': 6}
    print_sorted({6: 5, -3: 6, 4: ("a","z", "d","g" ,"h" )}) # should print {-3: 6, 4: ['a', 'd', 'g', 'h', 'z'], 6: 5}
    print_sorted([[8,3,9,4],[{1:5,-8:5,7:4}]])#should print [[3, 4, 8, 9], [{-8: 5, 1: 5, 7: 4}]]