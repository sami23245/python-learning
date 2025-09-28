import os 

with open("f.txt","r") as f: #open file 
    
    c = f.read()   #read file and save in "c"
    
with open("t.txt" ,"w") as f:  #create new file with name of t.txt
    
    f.write(c)   #now content of "c" of "t.txt"

    
    # this program is use to copy a file 
    
'''
firt this program open exiting file and the copy content of that file in a variable after that create a new file and then use same variable to paste that content inside new made file but using read = copy and write = paste 


'''