list_a = [-2,3,5,1,54,32,-65]
list_a_map = map(abs, list_a)

for l in list_a_map:
    print(l)

print('##############################')

list_b = ['apple', 'banana', 'grape', 'strawberry']
list_b_map = map(len, list_b)

for l in list_b_map:
    print(l)
    
print('##############################')

list_c = [-2,3,5,1]
list_c_map = map(lambda x: x * 2, list_c)

for l in list_c_map:
    print(l)