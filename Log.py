import time
with open('log.txt','r') as f:
    a=f.readlines()
    f.close()
print('The last entry was\n'+a[len(a)-2])
with open('log.txt','a+') as f:
    f.write('\n'+(time.strftime("%H:%M:%S"))+'--'+(time.strftime("%d/%m/%Y")))
    txts=str(input(':'))
    see=''
    while txts =! '':
        see=(see+'\n'+txts)
        print(see)
        txts=str(input(':'))
    f.write(see)
    f.close()
