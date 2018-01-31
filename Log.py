import time
with open('log.txt','r') as f:
    a=f.readlines()
    print(str(a))
    f.close()
b=-2
c=a[b]
d=[]
while c != '==========\n':
    c=a[len(a)+b]
    d.append(c)
    b=b-1
print('\n'.join(d[::-1]))
with open('log.txt','a+') as f:
    f.write('\n'+(time.strftime("%H:%M:%S"))+'--'+(time.strftime("%d/%m/%Y")))
    txts=str(input(':'))
    see=''
    while txts != '':
        see=(see+'\n'+txts)
        print(see)
        txts=str(input(':'))
    f.write(see)
    f.write('\n==========')
    f.close()
