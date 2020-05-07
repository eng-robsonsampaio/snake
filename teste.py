import math

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


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:6} ==> {phone:6.2f}')