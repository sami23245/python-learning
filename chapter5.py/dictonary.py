marks ={
    "harry":33,
    "sam":45,
}
print(marks["harry"] ,type(marks))

form = {
    "name": "ali",
    "age":23,
    "profession":"driver",
    "salery":200,
}

print(form["salery"])

print(form.items())

form.update({"age": 34,})

print(form.items())