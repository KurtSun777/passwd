password = '123456'
i=3

while i > 0:
    pw = input('plz input password: ')
    if password == pw:
        print('log in')
        break
    else:
        i -= 1
        print('you will have', i, 'chance')
        

    
