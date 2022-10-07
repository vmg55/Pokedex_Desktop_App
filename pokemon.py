import random
import moves


class Pokemon:

    LEVEL = 50

    def calculate_in_game_hp(self, base_stat):
        in_game_hp = int(((2 * base_stat) * self.LEVEL) / 100 + self.LEVEL + 10)
        return in_game_hp

    def calculate_in_game_stat(self, base_stat):
        in_game_stat = int(((2 * base_stat) * self.LEVEL) / 100 + 5)
        return in_game_stat

    # Pokemon Constuctor
    def __init__(self, name='', type1=None, type2=None, base_hp= (0), base_attack=0, base_defense=0,
                 base_sp_attack=0, base_sp_defense=0, base_speed=0, move_set=None):
        # Pokemon Info
        self.name = name
        self.type1 = type1
        self.type2 = type2
        # In Game Stats
        self.hp = self.calculate_in_game_hp(base_hp)
        self.attack = self.calculate_in_game_stat(base_attack)
        self.defense = self.calculate_in_game_stat(base_defense)
        self.sp_attack = self.calculate_in_game_stat(base_sp_attack)
        self.sp_defense = self.calculate_in_game_stat(base_sp_defense)
        self.speed = self.calculate_in_game_stat(base_speed)
        # Pokemon Moves
        self.move_set = move_set
        # Status Effects
        self.status = None

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
        damage = int(((((2 * self.LEVEL) / 5 + 2) * power * a / d) / 50 + 2) * critical * random_int * burn * \
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
        else:
            print(f"{self.name}'s attack missed!")


type_chart = {
    'Fire': {'Weak Against': ['Water', 'Ground', 'Rock'],
             'Strong Against': ['Grass', 'Ice', 'Bug', 'Steel']},
    'Water': {'Weak Against': ['Electric', 'Grass'],
              'Strong Against': ['Fire', 'Ground', 'Rock']},
    'Grass': {'Weak Against': ['Fire', 'Ice', 'Flying','Poison', 'Bug'],
              'Strong Against': ['Water', 'Ground', 'Rock']},
    'Rock': {'Weak Against': ['Water', 'Steel', 'Fighting', 'Ground', 'Grass'],
             'Strong Against': ['Fire', 'Flying', 'Ice', 'Steel']},
    'Ground': {'Weak Against': ['Water', 'Grass', 'Ice', ],
               'Strong Against': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel']},
    'Electric': {'Weak Against': ['Ground'],
                 'Strong Against': ['Flying', 'Water']},
    'Ice': {'Weak Against': ['Fire', 'Steel', 'Rock', 'Fighting'],
            'Strong Against': ['Grass', 'Ground', 'Flying', 'Dragon']},
    'Dragon': {'Weak Against': ['Ice', 'Fairy', 'Dragon'],
               'Strong Against': ['Dragon']},
    'Dark': {'Weak Against': ['Bug', 'Fighting', 'Fairy'],
             'Strong Against': ['Psychic', 'Ghost']},
    'Psychic': {'Weak Against': ['Fighting', 'Poison'],
                'Strong Against': ['Bug', 'Ghost', 'Dark']},
    'Ghost': {'Weak Against': ['Ghost', 'Dark'],
              'Strong Against': ['Ghost', 'Psychic']},
    'Bug': {'Weak Against': ['Fire', 'Flying', 'Rock'],
            'Strong Against': ['Psychic', 'Dark', 'Grass']},
    'Flying': {'Weak Against': ['Ice', 'Electric', 'Rock'],
               'Strong Against': ['Grass', 'Fighting', 'Bug']},
    'Steel': {'Weak Against': ['Fire', 'Ground', 'Fighting'],
              'Strong Against': ['Rock', 'Fairy', 'Ice']},
    'Fighting': {'Weak Against': ['Flying', 'Psychic', 'Fairy'],
                 'Strong Against': ['Normal', 'Ice', 'Rock', 'Steel', 'Dark']},
    'Poison': {'Weak Against': ['Psychic', 'Ground'],
               'Strong Against': ['Grass', 'Fairy']},
    'Fairy': {'Weak Against': ['Posion', 'Steel'],
              'Strong Against': ['Fighting', 'Dragon', 'Dark']},
    'Normal': {'Weak Against': ['Fighting'],
               'Strong Against': []},

}


def one_on_one_battle(pokemon1, pokemon2):
    print(f'Opponent sends out {pokemon2.name}!')
    print(f'Go {pokemon1.name}!')
    while pokemon1.hp > 0 and pokemon2.hp > 0:
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

    if pokemon1.hp <= 0:
        print(f'{pokemon1.name} fainted!')
    else:
        print(f'{pokemon2.name} fainted!')


def team_battle(team1=[], team2=[]):
    pass

