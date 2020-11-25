def homework_a(victims):
    for x in victims:
        victim_info = x.replace(';', ' ').replace(',', ' ').split(' ')
        if victim_info[len(victim_info) - 1] == 't':
            victim_info[len(victim_info) - 1] = True
        else:
            victim_info[len(victim_info) - 1] = False
        victims = {
            'name': victim_info[0],
            'surname': victim_info[1],
            'card_no': (int (victim_info[2])),
            'card_exp': victim_info[3],
            'card_that_third_thing': (int (victim_info[4])),
            'pwd': victim_info[5],
            '2factor': victim_info[6]
        }

        print(victims)

raw_data = [
    "Karel Vopěnka;1654731544681137,10/25,487;iamthecapitannow;t",
    "Ekaterina Pogonisheva;3685147993221530,12/22,369;<3pogoftw;f",
    "Jana Poláková;5168467833451129,02/19,498;lol;f"
]

def homework_b():
    pass
print(homework_a(raw_data))
