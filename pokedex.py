from tkinter import *
from tkinter import ttk
import pokemon
import pandas as pd
from math import isnan


class Pokedex:
    # all widgets are created in the def __init__
    def __init__(self, master):
        # Title the top level window
        master.title('Pokedex Desktop App')
        # Master widget configurations
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=1)
        master.rowconfigure(3, weight=1)
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)

        # Header frame and widgets
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack(fill = BOTH)
        # Logo and Header Text
        self.logo = PhotoImage(file='pokemon_sprites/202.png')
        ttk.Label(self.header_frame, image=self.logo).grid(row=0, column=1)
        self.title = ttk.Label(self.header_frame, text='Poke Stats App')
        self.title.grid(row=0, column=0, rowspan=2)
        self.title.config(font=('Arial', '18'), foreground = 'blue')
        # Combobox configurations for pokemon selection
        self.pokemon_entered = StringVar()
        self.combobox = ttk.Combobox(self.header_frame, textvariable=self.pokemon_entered)
        self.combobox.config(values=[val.name for key, val in sorted_dict.items()])
        self.combobox.grid(row=3, column=0, columnspan=2,  padx=50, pady=20)
        self.combobox.set('Bulbasaur')

        # Frame for pokemon image and typing
        self.picture_frame = ttk.Frame(master, height=100, width=200)
        self.picture_frame.pack(fill=BOTH)
        self.pokemon_type1 = 'Grass'
        self.pokemon_type2 = 'Poison'
        self.pokemon_sprite = PhotoImage(file='pokemon_sprites/1.png')
        self.sprite_label = ttk.Label(self.picture_frame, image=self.pokemon_sprite)
        self.type1_label = ttk.Label(self.picture_frame,  text=self.pokemon_type1)
        self.type2_label = ttk.Label(self.picture_frame, text=self.pokemon_type2)
        # Buttons for pokemon type effectiveness
        ttk.Button(self.picture_frame, text='Resists', command=self.resistances).place(x=110, y=0)
        ttk.Button(self.picture_frame, text='Weaknesses', command=self.weaknesses).place(x=195, y=0)
        # Type effectiveness labels
        self.quarter_resistant = ttk.Label(self.picture_frame, text=f'1/4: ')
        self.quarter_resistant.place(x=110, y=30)
        self.half_resistant = ttk.Label(self.picture_frame, text=f'1/2: ')
        self.half_resistant.place(x=110, y=65)
        # Layout of image and typing
        self.type1_label.place(x=5, y=0)
        self.type2_label.place(x=60, y=0)
        self.sprite_label.place(x=0, y=10)

        # Frame for Pokemon stats
        self.stats_frame = ttk.Frame(master)
        self.stats_frame.pack(fill=BOTH, expand=True)
        # Labels for stats
        self.hp_label = ttk.Label(self.stats_frame, text=f"Health \t {pokedex_dict['bulbasaur'].hp}  ")
        self.attack_label = ttk.Label(self.stats_frame, text=f"Attack \t {pokedex_dict['bulbasaur'].attack}   ")
        self.defense_label = ttk.Label(self.stats_frame, text=f"Defense \t {pokedex_dict['bulbasaur'].defense}   ")
        self.sp_attack_label = ttk.Label(self.stats_frame, text=f"Sp Att \t {pokedex_dict['bulbasaur'].sp_attack}   ")
        self.sp_defense_label = ttk.Label(self.stats_frame, text=f"Sp Def \t {pokedex_dict['bulbasaur'].sp_defense}   ")
        self.speed_label = ttk.Label(self.stats_frame, text=f"Speed \t {pokedex_dict['bulbasaur'].speed}   ")
        # Label Configurations
        self.hp_label.grid(row=0, column=0)
        self.attack_label.grid(row=1, column=0)
        self.defense_label.grid(row=2, column=0)
        self.sp_attack_label.grid(row=3, column=0)
        self.sp_defense_label.grid(row=4, column=0)
        self.speed_label.grid(row=5, column=0)
        # Stat bar
        self.hp_bar = ttk.Progressbar(self.stats_frame, orient=HORIZONTAL, length=180)
        self.attack_bar = ttk.Progressbar(self.stats_frame, orient=HORIZONTAL, length=180)
        self.defense_bar = ttk.Progressbar(self.stats_frame, orient=HORIZONTAL, length=180)
        self.sp_attack_bar = ttk.Progressbar(self.stats_frame, orient=HORIZONTAL, length=180)
        self.sp_defense_bar = ttk.Progressbar(self.stats_frame, orient=HORIZONTAL, length=180)
        self.speed_bar = ttk.Progressbar(self.stats_frame, orient=HORIZONTAL, length=180)
        # Stat bar configurations
        self.hp_bar.grid(row=0, column=1)
        self.attack_bar.grid(row=1, column=1)
        self.defense_bar.grid(row=2, column=1)
        self.sp_attack_bar.grid(row=3, column=1)
        self.sp_defense_bar.grid(row=4, column=1)
        self.speed_bar.grid(row=5, column=1)
        self.hp_bar.config(mode='determinate', maximum=300, value=45)
        self.attack_bar.config(mode='determinate', maximum=300, value=54)
        self.defense_bar.config(mode='determinate', maximum=300, value=54)
        self.sp_attack_bar.config(mode='determinate', maximum=300, value=70)
        self.sp_defense_bar.config(mode='determinate', maximum=300, value=70)
        self.speed_bar.config(mode='determinate', maximum=300, value=50)

        # Event binding for pokemon combobox selection
        self.combobox.bind("<<ComboboxSelected>>", self.get_pokemon)
        self.combobox.bind("<Return>", self.get_pokemon)

    # These actions occur when a pokemon is entered in / selected from the combobox
    def get_pokemon(self, event):
        # Return pokemon name from combobox
        pokemon_selected = self.combobox.get().lower()
        pokedex_id = pokedex_dict[pokemon_selected].pokedex_id
        # Change sprite that is displayed along with types
        poke_sprite = PhotoImage(file=f'pokemon_sprites/{pokedex_id}.png')
        if type(pokedex_dict[pokemon_selected].type2) is float:
            self.type1_label.place(x=28, y=0)
            self.type1_label.config(text=pokedex_dict[pokemon_selected].type1)
            self.type2_label.place_forget()
        else:
            self.type1_label.place(x=5, y=0)
            self.type2_label.place(x=60, y=0)
            self.type1_label.config(text=pokedex_dict[pokemon_selected].type1)
            self.type2_label.config(text=pokedex_dict[pokemon_selected].type2)
        self.sprite_label.img = poke_sprite
        self.sprite_label.config(image=self.sprite_label.img)
        # Change pokemon stats to match selected pokemon
        self.hp_label.config(text=f"Health \t {pokedex_dict[pokemon_selected].hp}   ")
        self.attack_label.config(text=f"Attack \t {pokedex_dict[pokemon_selected].attack}   ")
        self.defense_label.config(text=f"Defense \t {pokedex_dict[pokemon_selected].defense}   ")
        self.sp_attack_label.config(text=f"Sp Att \t {pokedex_dict[pokemon_selected].sp_attack}   ")
        self.sp_defense_label.config(text=f"Sp Def \t {pokedex_dict[pokemon_selected].sp_defense}   ")
        self.speed_label.config(text=f"Speed \t {pokedex_dict[pokemon_selected].speed}   ")
        self.hp_bar.config(mode='determinate', maximum=300, value=pokedex_dict[pokemon_selected].hp)
        self.attack_bar.config(mode='determinate', maximum=300, value=pokedex_dict[pokemon_selected].attack)
        self.defense_bar.config(mode='determinate', maximum=300, value=pokedex_dict[pokemon_selected].defense)
        self.sp_attack_bar.config(mode='determinate', maximum=300, value=pokedex_dict[pokemon_selected].sp_attack)
        self.sp_defense_bar.config(mode='determinate', maximum=300, value=pokedex_dict[pokemon_selected].sp_defense)
        self.speed_bar.config(mode='determinate', maximum=300, value=pokedex_dict[pokemon_selected].speed)

    def resistances(self):
        pokemon_selected = self.combobox.get().lower()
        type_effectiveness = pokedex_dict[pokemon_selected].calc_type_effectiveness()
        quarter = [k for k, v in type_effectiveness.items() if v < 0.5]
        half = [k for k, v in type_effectiveness.items() if v == 0.5]
        quarter_str = ''
        half_str = ''
        for i, t in enumerate(quarter):
            quarter_str += t
            quarter_str += '   '
            if (i+1) % 3 == 0:
                quarter_str += '\n        '
        for i, t in enumerate(half):
            half_str += t
            half_str += '   '
            if (i +1) % 3 == 0:
                half_str += '\n        '
        self.quarter_resistant.config(text=f'1/4: {quarter_str}')
        self.quarter_resistant.place(x=110, y=30)
        self.half_resistant.config(text=f'1/2: {half_str}')
        self.half_resistant.place(x=110, y=65)

    def weaknesses(self):
        pokemon_selected = self.combobox.get().lower()
        type_effectiveness = pokedex_dict[pokemon_selected].calc_type_effectiveness()
        times2 = [k for k, v in type_effectiveness.items() if v == 2]
        times4 = [k for k, v in type_effectiveness.items() if v > 2]
        times_two_str = ''
        times_four_str = ''
        for i, t in enumerate(times2):
            times_two_str += t
            times_two_str += '     '
            if (i + 1) % 3 == 0:
                times_two_str += '\n      '
        for i, t in enumerate(times4):
            times_four_str += t
            times_four_str += '     '
            if (i + 1) % 3 == 0:
                times_four_str += '\n        '
        self.quarter_resistant.config(text=f'2x: {times_two_str}')
        self.quarter_resistant.place(x=110, y=30)
        self.half_resistant.config(text=f'4x: {times_four_str}')
        self.half_resistant.place(x=110, y=65)


pokemon_df = pd.read_csv('Pokemon_data.csv')

pokedex_dict = {}

for index, record in pokemon_df.iterrows():
    name = record['Name']
    pokedex_id = record['#']
    if "Mega" in name:
        continue
    generation = int(record['Generation'])
    if generation > 5:
        continue
    type1 = record['Type 1']
    type2 = record['Type 2']
    hp = record['HP']
    attack = record['Attack']
    defense = record['Defense']
    spAtk = record['Sp. Atk']
    spDef = record['Sp. Def']
    speed = record['Speed']

    pokedex_dict[name.lower()] = pokemon.Pokemon(name, pokedex_id, type1, type2, hp, attack, defense, spAtk,
                                                 spDef, speed, gen=generation)

# Sort pokemon into alphabetical order
sorted_tuples = sorted(pokedex_dict.items(), key=lambda item: item[1].name)
sorted_dict = {k: v for k, v in sorted_tuples}
