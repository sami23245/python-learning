# Open the file in read mode first
with open("filter.txt", "r") as f:
    content = f.read()

# Replace all occurrences of "Donkey" with "#####"
content = content.replace("Donkey", "#####")

# Write the updated content back to the same file
with open("filter.txt", "w") as f:
    f.write(content)


with open("filter.txt") as f:
    print(f.read())
    

print("All 'Donkey' words have been replaced with ##### successfully!")
