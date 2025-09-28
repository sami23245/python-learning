# Open the file in read mode first
with open("f.txt", "r") as f:
    content = f.read()

# Replace all occurrences of "Donkey" with "#####"
content = content.replace("Donkey", "#####")

# Write the updated content back to the same file
with open("f.txt", "w") as f:
    bad_words = ["donkey", "idiot", "stupid"]
    for word in bad_words:
        content = content.replace(word, "#####")

    f.write(content)
print("all bad word replace by #####")