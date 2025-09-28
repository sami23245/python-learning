name = input("enter your name :")
date = input("Enter you date of birth :")

print(f"good afternoon {name}")

print(f'''Dear {name} you are selected {date}''')


latter = ''' Dear name you are selected date'''

print(latter.replace("name", name).replace("date", date))
