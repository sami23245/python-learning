#this program is use to check content in thses files is same or not

with open("testerfilesofch9/file1.txt" , "r") as f,open("testerfilesofch9/file2.txt" , "r") as f2:
    c1 = f.read()
    c2 = f2.read()
    

    
    
if c1 == c2 :
    print("both are same ")
    print(c2)
else:
    print("no match")
    