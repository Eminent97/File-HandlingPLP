with open("PLP", "r") as file:
    content = file.read()

with open("PLP2", "a") as file:
    file.write("Am adding this as an update")

with open("PLP3", "w") as file:
    file.write("Here is a new file that can be used to modify the content")

try:
    with open("PLPtwo", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File Not found")





