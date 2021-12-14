import os 

for i in os.listdir('.'):
    if i.endswith('.png'):
        name_new = 'r_'+ i
        print(name_new)
        os.rename(i,name_new)