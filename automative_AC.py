import pandas as pd
from pandas import DataFrame

file = open('C:/Users/s4017/Desktop/WT67436X1AAZR_R.TFT120190111061559')
f1=file.read()
f=open('f.txt','w')
f.write(f1)
f.close()
f2=open('f.txt')

list1=[] # for first df
list2=[] # for second df
del_row_index = False #為了刪除第二個之後的標題列

for i in f2:
    if (i[:3] =='XYZ')&(len(i)>58) :
        x = i.translate({ord(c): None for c in ' '}).split(':')
        x.remove('\n')  #刪除\n
        if x[0] == 'XYZTCKB':
            count = 1 
            
        list1.append(x)
        
        if count == 209: #210 等於第二個  'XYZTCKB'
            df=DataFrame(list1)
            if del_row_index == True :     #刪除第二個以後的列標題 'XYZTCKB'
                del df[0]
            list2.append(df)
            list1=[] #清除list1
            del_row_index = True    #開啟刪除訊號
        #print(x)
        #print(x[0],count)
        count += 1
        
datas=pd.concat(list2,axis=1)
#datas.set_index['0'] #選第一行當列名稱
datas.to_csv('test.csv',encoding='utf_8_sig',header=False, index=False)        
