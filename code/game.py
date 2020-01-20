from jinja2 import Template

game_of_thrones = [
    {'house': 'House Lannister',
     'name': 'Tyrion',
     'motto': 'Hear Me Roar!, A Lannister Always Pays His Debts'},
    {'house': 'House Stark',
     'name': 'Jon Snow',
     'motto': 'Winter Is Coming'},
    {'house': 'House Targaryen',
     'name': 'Daenerys ',
     'motto': 'Fire And Blood'},
]

with open("game.j2") as f:
    house_in = Template(f.read())

house_out = house_in.render(inputs=game_of_thrones)

print(house_out)
