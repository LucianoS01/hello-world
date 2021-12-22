


archivo1=open('IDEC.txt','r') 
    
cont = 1
linea1=archivo1.readline().strip()
i = 0
while linea1 != '':
        
    print((linea1.split(',')[0]))
    cont = cont  + 1
    i = i + 1
    linea1=archivo1.readline().strip()