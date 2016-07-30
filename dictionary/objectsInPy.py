print('File is working')

objects_languages = {'m1':'python','web':'javascript','enterprise':'java','webassembly':'rust'}
print(objects_languages)

#querying
print(objects_languages['web'])

#making a new propert
objects_languages['vr'] = 'C++'
print(objects_languages)

#deleting a property
del objects_languages['vr']
print(objects_languages)
#loop thru an object
for key,val in objects_languages.items():
    print(key)
