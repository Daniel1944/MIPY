import os

# misto kde pracujeme
cwd = os.getcwd()
print(cwd)
print(os.getlogin())
files = os.listdir(cwd)
path = os.path.join(cwd, files[1])
print(os.path.split(path))

# cteni ze souboru
path_to_file = os.path.join("C:\\Users\\Daniel\\PycharmProjects\\pythonProject", "pyvenv.cfg")
f = open(path_to_file, "r")
data = f.read()
f.close()

# print(type(data))
# print(data)

# lepsi verze
# with open(path_to_file, "r") as f:
#    lines = f.readlines()
# print(data)

# settings = {}
# for line in lines:
#    line = line.strip() # vymaze white space  znaky ze zacatku a konce stringu
#    key, val = line.split(" = " ) # tuple list unpacklingh
#    settings[key] = val
# print(settings)
