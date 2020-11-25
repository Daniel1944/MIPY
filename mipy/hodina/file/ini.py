import configparser as cp
config = cp.ConfigParser()
config.read("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sample.ini")

for section in config:
    for key in config[section]:
        print("|- {}: {}".format(key, config[section][key]))