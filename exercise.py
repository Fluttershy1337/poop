from functools import reduce

games = ['gaysex', '2gaysex4mepls', 'hug my cat', 'hug my love']
food = ['mayonaaaaiseee', 'riepa', 'vanilka']
favorite = games + food

print('this is my most favorite things really believe me', reduce((lambda x, y: x + ", "+ y),favorite))
