f2=open('f.txt')
f3=open('f3.txt','w')
for i in f2:
    if (i[:3]=='-25' or i[:3]=='-18' ):
        switch = True
        f3.write(i)
    elif (i[:3]=='-30' or i[:3]=='-37' or i[:3]=='-50'):
        switch = False
    if (i[:7]=='DUT    ' and len(i)>13 and switch == True):
        f3.write(i)
        
f3.close()
