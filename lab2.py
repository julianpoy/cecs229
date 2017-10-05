L = ['A','B','C','D','E']
# 1
zip(range(0,5),L)

# 2
dlist = [{'James':'Sean','director':'Terence'}, {'James':'Roger','director':'Lewis'}, {'James':'Pierce','director':'Roger'}]
k = 'James'

# [d[i] for d in dlist for i in d if i == k]
[d[k] for d in dlist]

# 3
{i:i**2 for i in range(0,100)}

# 4
id2salary = {0:1000.0, 3:990, 1:1200.50}
names = ['Larry', 'Curly', '', 'Moe']

{ item:id2salary[i] for i,item in enumerate(names) if i in id2salary }

