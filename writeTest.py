#data = ['abc', 'def']

# with open('writeText.txt','a')as f:
#     f.write('\n')
#     f.write('\n'.join(data))

with open('writeText.txt','r')as f:
    data1 = f.readline()
    data2 = f.readlines()
    data = f.read()

    print (data)
    print (data1)
    print (data2)