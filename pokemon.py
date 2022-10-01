class Pokemon:

    # Pokemon Constuctor
    def __init__(self, name='', type1=None, type2=None, hp=0, attack=0, defense=0,
                 sp_attack=0, sp_defense=0, speed=0, move_set={}):
        # Pokemon Info
        self.name = name
        self.type1 = type1
        self.type2 = type2
        # Basic Stats
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        # Pokemon Moves
        # Key = move name
        # Value = list [power, accuracy, type]
        self.move_set = move_set

    def set_moves(self):
        empty_moves = 4 - len(self.move_set)
        for i in range(empty_moves):
            move = input('Move Name: ')
            power = int(input('Power: '))
            accuracy = int(input('Accuracy: '))
            move_type = input('Move Type: ')
            category = input('Physical, Special, or Status Move: ')
            self.move_set[move] = [power, accuracy, move_type, category]

    def display_moves(self):
        for i in self.move_set:
            print(i)

    # Pokemon uses an attack
    # Need stats of opposing pokemon to calculate damage taken
    def attack_move(self, opposing_pokemon):
        self.display_moves()
        chosen_move = input(f'What will {self.name} do?')
        # Validate user input
        while chosen_move not in self.move_set:
            print('Invalid move')
            chosen_move = input(f'What will {self.name} do?')
        print(f'{self.name} used {chosen_move}!')


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
    while pokemon1.hp != 0 and pokemon2.hp != 0:
        # Determine which pokemon goes first
        # Faster pokemon moves first
        if pokemon1.speed > pokemon2.speed:
            pokemon1.attack_move(pokemon2)
            # Check if pokemon has not fainted
            if pokemon2.hp != 0:
                pokemon2.attack_move(pokemon1)
        else:
            pokemon2.attack_move(pokemon1)
            # Check if pokemon has not fainted
            if pokemon1.hp != 0:
                pokemon1.attack_move(pokemon2)

    if pokemon2.hp == 0:
        print(f'{pokemon2.name} fainted!')
    if pokemon1.hp == 0:
        print(f'{pokemon1.name} fainted!')


def team_battle(team1=[], team2=[]):
    pass

