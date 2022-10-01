import pokemon

pokemon1 = pokemon.Pokemon('Charmander', 'fire', None, 39, 52, 43, 60, 50, 50)
pokemon2 = pokemon.Pokemon('Squirtle', 'water', None, 44, 48, 65, 50, 64, 43)

#print(pokemon2.name)
#print(pokemon.type_chart['Water'])

pokemon2.set_moves()

pokemon2.attack_move(pokemon1)



