a=['st','pa','sc']
b=['st','pa','sc']


for i in a:
    for j in b:
            ##for stone...
            if j == 'st' and i == 'st' :
                 
                 print(j,"*",i,"=","tie")

            elif j == 'st' and i == 'pa':
                
                print(j,"*",i,"=",i)
            
            elif j == 'st' and i == 'sc':
                
                print(j,"*",i,"=",j)
            
            ##for paper...
            elif j == 'pa' and i == 'st':
                
                print(j,"*",i,"=",j)
            elif j == 'pa' and i == 'pa':
                
                print(j,"*",i,"=","tie")
            elif j == 'pa' and i == 'sc':
                
                print(j,"*",i,"=",i)
            
            ##for scior..
            elif j == 'sc' and i == 'st':
                
                print(j,"*",i,"=",i)
            elif j == 'sc' and i == 'pa':
                
                print(j,"*",i,"=",i)
            elif j == 'sc' and i == 'sc':
                
                print(j,"*",i,"=","tie")
            
            ##phase2:

            ##for stone...
            elif i == 'st' and j == 'st' :
                 
                 print(i,"*",j,"=","tie")

            elif i == 'st' and j == 'pa':
                
                print(i,"*",j,"=",j)
            
            elif i == 'st' and j == 'sc':
                
                print(i,"*",j,"=",i)
           
            ##for paper
            elif i == 'pa' and j == 'st':
                
                print(i,"*",j,"=",i)
            elif i == 'pa' and j == 'pa':
                
                print(i,"*",j,"=","tie")
            elif i == 'pa' and j == 'sc':
                
                print(i,"*",j,"=",j)
            
            ##for scisor..
            elif i == 'sc' and j == 'st':
                
                print(i,"*",j,"=",j)
            elif i == 'sc' and j == 'pa':
                
                print(i,"*",j,"=",j)
            elif i == 'sc' and j == 'sc':
                
                print(i,"*",j,"=","tie")
            else:
                print("invaliddd..")
            