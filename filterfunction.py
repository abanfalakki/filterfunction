def fun(variable):
    letters=['a','e','i','o','u']
    if (variable in letters):
        return True
    else:
        return False
sequence=['g','e','e','f','k','s','p','r']
filterd=filter(fun,sequence)
print('the filtered letters are:')
for s in filterd:
    print(s)