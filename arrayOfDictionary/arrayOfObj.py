print('File is working')

obj1 = {'name':'kaka1','id':0}
obj2 = {'name':'kaka2','id':0}
obj3 = {'name':'kaka3','id':0}
arr = [obj1, obj2, obj3]
i = 0

for a in arr:
    if a['name'] == 'kaka1':
        i = 1
        a['id'] = i
        print(str(a['name'])+' got id '+str(a['id']))
    elif a['name'] == 'kaka2':
        i = 2
        a['id'] = i
        print(str(a['name'])+' got id ' + str(a['id']))
    else:
        i = 3
        a['id'] = i
        print(str(a['name'])+' got id ' + str(a['id']))
print(arr)