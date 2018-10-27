import csv
path='Stats.tsv'
singers=[]
with open(path,'r') as csvfile:   
    readCSV = csv.reader(csvfile, delimiter='\t')
    for row in readCSV:   
        S=row[3].split(',')
        s=[]
        for i in S:
            s.append(i.strip(' '))
        singers=singers+s
        
singers=list(set(singers))
file=open('singers','w')
file.write('\n'.join(singers))
file.close()        