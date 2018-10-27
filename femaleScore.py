import csv
code={}
file=open('singerCode.csv','r').read().split('\n')
for f in file:
    if len(f)>1:
        row=f.split(',')
        code[row[0]]=row[1]
path='Stats.tsv'
singers=[]
j=0
XY=[]
with open(path,'r') as csvfile:   
    readCSV = csv.reader(csvfile, delimiter='\t')
    for row in readCSV:   
        
        if j >0:
            S=row[3].split(',')
            R=row[7].replace(',','').split(' ')[0]
            s=[]
            for i in S:
                s.append(i.strip(' '))
            p=0
            for i in s:
                if code[i]=='1':
                    p=p+1
                
            #XY.append([float(p)/float(len(s)),row[9]])
            XY.append([float(p)/float(len(s)),R])
            #XY.append([p,row[9]])
            
        j=j+1

file=open('scores.csv','w')
for p in XY:
    file.write(str(p[0])+','+str(p[1])+'\n')

file.close()        