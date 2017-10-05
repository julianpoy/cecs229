
def cubes(L): return [ x*x*x for x in L if x%2 == 0 ]

print(cubes([1,2,3,4]))

def dict2list(dct, keylist): return [ dct[key] for key in keylist ]

print(dict2list({ 0:'A', 1:'B', 2:'C' }, [1,2,0]))

def list2dict(L, keylist): return { key:L[key] for key in keylist }

print(list2dict(['A', 'B', 'C'], [0, 1, 2]))