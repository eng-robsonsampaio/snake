import math
import json

with open("teste.json", "a") as file:
    if not file.read():
        json.dump(json.loads({"highscore":"0"}), file, indent=4)
    else:
        print(file.read())

# def read_highscore():
#     with open("highscore.json") as file:
#         return json.loads(file.read())

# def save_highscore():
#     with open("highscore.json", "w") as file:
#         json.dump(jfile, file, indent = 4, sort_keys=True)

# jfile = read_highscore()
# jfile["highscore"] = 10
# print(jfile)
# save_highscore()

# number = 128
# print(f"number: {number}")
# li = list(chr(number).encode("utf-8"))
# print(f"List of byte: {li}")
# dec = int.from_bytes(li, byteorder='big')
# print(f"Type dec: {type(dec)}")
# print(f"Value dec: {dec}")

# print(bytes([195, 136]).decode('utf8'))

# start = 0
# step = 1
# stop = 5
# top_wall = [(min(n+step-1, stop), start) for n in range(start, stop+1, step)]

# String format examples
# year = 2020
# event = 'COVID-19'
# print(f"Results of the {event} in {year}")

# samples = 50
# acaminho = 23/25
# indisponivel = 18/25
# print("A caminho: {:2.2%}\nIndispinivel: {:2.2%}".format(acaminho, indisponivel))


# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name:6} ==> {phone:6.2f}')