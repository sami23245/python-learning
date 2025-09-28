import os

# Create a folder for storing tables (if it doesn’t exist already)
folder_name = "Multiplication_Tables"
os.makedirs(folder_name, exist_ok=True)

# Generate tables from 2 to 20
for num in range(2, 21):  
    file_path = os.path.join(folder_name, f"Table_of_{num}.txt")
    
    with open(file_path, "w") as f:   # write mode (new file for each table)
        for i in range(1, 11):
            t = f"{num} x {i} = {num * i}"
            f.write(t + "\n")   # save in file
