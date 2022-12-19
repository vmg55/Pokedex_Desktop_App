import random
import moves


class Pokemon:

    # All pokemon will be level 50
    LEVEL = 50

    # Pokemon Constuctor
    def __init__(self, name='', pokedex_id=0 ,  type1=None, type2=None, base_hp=0, base_attack=0, base_defense=0,
                 base_sp_attack=0, base_sp_defense=0, base_speed=0, move_set=None, gen=0, sprite=None):
        # Pokemon Meta Data
        self.name = name
        self.pokedex_id = pokedex_id
        self.type1 = type1
        self.type2 = type2
        self.gen = gen
        self.sprite = sprite
        # In Game Stats
        self.hp = base_hp
        self.attack = base_attack
        self.defense = base_defense
        self.sp_attack = base_sp_attack
        self.sp_defense = base_sp_defense
        self.speed = base_speed
        # Pokemon Moves
        self.move_set = move_set

    def calc_type_effectiveness(self):
        # dictionary type disadvantages against the pokemon; key = type, val = int
        # Goes through the resistances and weaknesses of the pokemon's type(s)
        type_effectiveness = {}
        weaknesses = type_chart[self.type1]['Weak Against'] + type_chart[self.type2]['Weak Against']
        resistances = type_chart[self.type1]['Resists'] + type_chart[self.type2]['Resists']

        # A weakness gets a multiplier of 2
        for t in weaknesses:
            if t in type_effectiveness:
                type_effectiveness[t] *= 2
            else:
                type_effectiveness[t] = 2
        # A resistance gets cut in half
        for t in resistances:
            if t in type_effectiveness:
                type_effectiveness[t] *= 0.5
            else:
                type_effectiveness[t] = 0.5

        return type_effectiveness

    def calculate_in_game_hp(self, base_stat):
        in_game_hp = int(((2 * base_stat) * self.LEVEL) / 100 + self.LEVEL + 10)
        return in_game_hp

    def calculate_in_game_stat(self, base_stat):
        in_game_stat = int(((2 * base_stat) * self.LEVEL) / 100 + 5)
        return in_game_stat

    def input_move(self):
        name = input('Move Name: ')
        power = int(input('Power: '))
        accuracy = int(input('Accuracy: '))
        move_type = input('Move Type: ')
        category = input('Physical, Special, or Status Move: ')
        if self.move_set is None:
            self.move_set = []
        self.move_set.append(moves.Move(name, power, accuracy, move_type, category))

    def assign_move(self, new_move):
        if self.move_set is None:
            self.move_set = []
        self.move_set.append(new_move)

    def display_moves(self):
        for move in self.move_set:
            print(move.name)

    def display_stats(self):
        print('Pokemon:', self.name, self.type1, self.type2, f'(Generation {self.gen})')
        print('HP:', self.hp)
        print('Attack:', self.attack)
        print('Defense:',  self.defense)
        print('Special Attack:', self.sp_attack)
        print('Special Defense:', self.sp_defense)
        print('Speed:', self.speed)

    # Pokemon uses an attack
    # Need stats of opposing pokemon to calculate damage taken
    def attack_move(self, opposing_pokemon):
        print(f'What will {self.name} do?')
        self.display_moves()
        user_input = input().lower()

        # Validate user input
        available_moves = [i.name.lower() for i in self.move_set]
        while user_input not in available_moves:
            print('Invalid move')
            print(f'What will {self.name} do?')
            self.display_moves()
            user_input = input().lower()

        # Select Move
        chosen_move = None
        for move in self.move_set:
            if user_input == move.name.lower():
                chosen_move = move

        # Initialize default values for damage calculator
        critical = 1
        random_int = random.randint(85, 100) / 100
        stab = 1
        burn = 1
        type_effectiveness = 1
        TYPE1 = opposing_pokemon.type1
        TYPE2 = opposing_pokemon.type2
        power = chosen_move.power
        accuracy = chosen_move.accuracy
        move_type = chosen_move.type
        category = chosen_move.category
        a = 1
        d = 1

        # Calculate type effectiveness
        if TYPE1 in type_chart[move_type]['Strong Against']:
            type_effectiveness *= 2
        if self.type2 is not None:
            if TYPE2 in type_chart[move_type]['Strong Against']:
                type_effectiveness *= 2
        if TYPE1 in type_chart[move_type]['Weak Against']:
            type_effectiveness *= 0.5
        if self.type2 is not None:
            if TYPE2 in type_chart[move_type]['Weak Against']:
                type_effectiveness *= 0.5

        # Check if critical hit
        ch_rand1 = random.randint(1, 16)
        ch_rand2 = random.randint(1, 16)
        if ch_rand1 == ch_rand2:
            critical = 2

        # Check if stab
        if move_type == TYPE1 or move_type == TYPE2:
            stab = 1.5

        # Check if Pokemon is burned
        if self.status == 'Burn' and category == 'Physical':
            burn = 0.5

        # Determine what Attack and Defense Stats will be used
        if category == 'Physical':
            a = self.attack
            d = opposing_pokemon.defense
        if category == 'Special':
            a = self.sp_attack
            d = opposing_pokemon.sp_defense

        # Calculate damage dealt
        damage = int(((((2 * self.LEVEL) / 5 + 2) * power * a / d) / 50 + 2) * critical * random_int * burn *
                     stab * type_effectiveness)

        # Display turn
        print(f'{self.name} used {chosen_move.name}!')

        # Calculate if the move lands
        threshold = random.randint(1,100)
        if threshold >= 1 and threshold <= accuracy:
            if critical == 2:
                print('It was a critical hit!')
            if type_effectiveness >= 2:
                print('It was super-effective!!')
            if type_effectiveness < 1:
                print("It's not very effective...")
            # Subtract damage from opposing pokemon
            opposing_pokemon.hp -= damage
            if opposing_pokemon.hp < 0:
                opposing_pokemon.hp = 0
        else:
            print(f"{self.name}'s attack missed!")

# Pokemon type weaknesses, resistances, and immunities
type_chart = {
    'Fire': {'Weak Against': ['Water', 'Ground', 'Rock'],
             'Strong Against': ['Grass', 'Ice', 'Bug', 'Steel'],
             'Resists': ['Bug', 'Steel', 'Fire', 'Ice', 'Grass'],
             'Immune': []},
    'Water': {'Weak Against': ['Electric', 'Grass'],
              'Strong Against': ['Fire', 'Ground', 'Rock'],
              'Resists': ['Steel', 'Fire', 'Ice', 'Water'],
              'Immune': []},
    'Grass': {'Weak Against': ['Fire', 'Ice', 'Flying', 'Poison', 'Bug'],
              'Strong Against': ['Water', 'Ground', 'Rock'],
              'Resists': ['Ground', 'Water', 'Grass', 'Electric'],
              'Immune': []},
    'Rock': {'Weak Against': ['Water', 'Steel', 'Fighting', 'Ground', 'Grass'],
             'Strong Against': ['Fire', 'Flying', 'Ice', 'Steel'],
             'Resists': ['Normal', 'Flying', 'Poison', 'Fire'],
             'Immune': []},
    'Ground': {'Weak Against': ['Water', 'Grass', 'Ice', ],
               'Strong Against': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'],
               'Resists': ['Poison', 'Rock'],
               'Immune': ['Electric']},
    'Electric': {'Weak Against': ['Ground'],
                 'Strong Against': ['Flying', 'Water'],
                 'Resists': ['Flying', 'Steel', 'Electric'],
                 'Immune': []},
    'Ice': {'Weak Against': ['Fire', 'Steel', 'Rock', 'Fighting'],
            'Strong Against': ['Grass', 'Ground', 'Flying', 'Dragon'],
            'Resists': ['Ice'],
            'Immune': []},
    'Dragon': {'Weak Against': ['Ice', 'Fairy', 'Dragon'],
               'Strong Against': ['Dragon'],
               'Resists': ['Fire', 'Grass', 'Electric', 'Water'],
               'Immune': []},
    'Dark': {'Weak Against': ['Bug', 'Fighting', 'Fairy'],
             'Strong Against': ['Psychic', 'Ghost'],
             'Resists': ['Ghost', 'Dark'],
             'Immune': ['Psychic']},
    'Psychic': {'Weak Against': ['Fighting', 'Poison'],
                'Strong Against': ['Bug', 'Ghost', 'Dark'],
                'Resists': ['Fighting', 'Psychic'],
                'Immune': []},
    'Ghost': {'Weak Against': ['Ghost', 'Dark'],
              'Strong Against': ['Ghost', 'Psychic'],
              'Resists': ['Poison', 'Bug'],
              'Immune': ['Normal', 'Fighting']},
    'Bug': {'Weak Against': ['Fire', 'Flying', 'Rock'],
            'Strong Against': ['Psychic', 'Dark', 'Grass'],
            'Resists': ['Fighting', 'Ground', 'Grass'],
            'Immune': []},
    'Flying': {'Weak Against': ['Ice', 'Electric', 'Rock'],
               'Strong Against': ['Grass', 'Fighting', 'Bug'],
               'Resists': ['Fighting', 'Bug', 'Grass'],
               'Immune': ['Ground']},
    'Steel': {'Weak Against': ['Fire', 'Ground', 'Fighting'],
              'Strong Against': ['Rock', 'Fairy', 'Ice'],
              'Resists': ['Normal', 'Flying', 'Bug', 'Psychic', 'Rock', 'Steel', 'Grass', 'Ice', 'Dragon', 'Fairy'],
              'Immune': ['Poison']},
    'Fighting': {'Weak Against': ['Flying', 'Psychic', 'Fairy'],
                 'Strong Against': ['Normal', 'Ice', 'Rock', 'Steel', 'Dark'],
                 'Resists': ['Rock', 'Dark', 'Bug'],
                 'Immune': []},
    'Poison': {'Weak Against': ['Psychic', 'Ground'],
               'Strong Against': ['Grass', 'Fairy'],
               'Resists': ['Fighting', 'Poison', 'Grass', 'Fairy', 'Bug'],
               'Immune': []},
    'Fairy': {'Weak Against': ['Posion', 'Steel'],
              'Strong Against': ['Fighting', 'Dragon', 'Dark'],
              'Resists': ['Fighting', 'Bug', 'Dark'],
              'Immune': ['Dragon']},
    'Normal': {'Weak Against': ['Fighting'],
               'Strong Against': [],
               'Resists': [],
               'Immune': ['Ghost']}
}

# Pokemon battle mechanic for later updates of the GUI (1 vs 1)
def one_on_one_battle(pokemon1, pokemon2):
    counter = 1
    while pokemon1.hp > 0 and pokemon2.hp > 0:
        print(f'*** turn {counter} ***')
        print(pokemon1.name, pokemon1.hp, pokemon2.name, pokemon2.hp, end=' ')
        print()
        # Determine which pokemon goes first
        # Faster pokemon moves first
        if pokemon1.speed > pokemon2.speed:
            pokemon1.attack_move(pokemon2)
            print(pokemon1.name, pokemon1.hp, pokemon2.name, pokemon2.hp, end=' ')
            print()
            # Check if pokemon has not fainted
            if pokemon2.hp > 0:
                pokemon2.attack_move(pokemon1)
        else:
            pokemon2.attack_move(pokemon1)
            print(pokemon1.name, pokemon1.hp, pokemon2.name, pokemon2.hp, end=' ')
            print()
            # Check if pokemon has not fainted
            if pokemon1.hp > 0:
                pokemon1.attack_move(pokemon2)
        counter += 1
        print('\n')

    if pokemon1.hp <= 0:
        print(f'{pokemon1.name} fainted!')
        return pokemon2
    else:
        print(f'{pokemon2.name} fainted!')
        return pokemon1


def display_team(team):
    for i in team:
        print(i.name)


# Pokemon battle mechanic for later updates of the GUI (team vs team)
def team_battle(team1=None, team2=None):
    # one team of pokemon will battle against another team of pokemon
    # need to battle pokemon one on one
    # after each battle 1 pokemon will faint
    # a fainted pokemon cannot be revived so remove the pokemon from the team
    # when a pokemon is removed from battle a new pokemon comes in to replace it
    # the pokemon that did not faint must stay in battle and their health and stats must stay the same
    # the battle ends when one team runs out of pokemon

    index1 = 0
    index2 = 0

    while team1 and team2:
        # choose what pokemon are battling
        team1_pokemon = team1[index1]
        team2_pokemon = team2[index2]

        # battle the two pokemon
        winner = one_on_one_battle(team1_pokemon, team2_pokemon)

        # Remove fainted pokemon
        # Ask user what pokemon should be subbed in
        if team2_pokemon.name == winner.name:
            team1.remove(team1[index1])
            if team1:
                print('What pokemon should be sent in?')
                display_team(team1)
                sub = input()
                for i, poke in enumerate(team1):
                    if poke.name.lower() == sub.lower():
                        index1 = i
                        print(f'Go {team1[index1].name}')

        if team1_pokemon.name == winner.name:
            team2.remove(team2[index2])
            if team2:
                print('What pokemon should be sent in?')
                display_team(team2)
                sub = input()
                for j, poke in enumerate(team2):
                    if poke.name.lower() == sub.lower():
                        index2 = j
                        print(f'Go {team1[index2].name}')

    if team1:
        print('Team 1 wins!!!')
    else:
        print('Team 2 wins!!!')