from tkinter import *
from tkinter import ttk
import pokemon
import pandas as pd


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
        self.header_frame.pack()
        # Logo and Header Text
        self.logo = PhotoImage(file = 'crystal_sprites/202.gif')
        ttk.Label(self.header_frame, image = self.logo).grid(row=0, column=1)
        self.title = ttk.Label(self.header_frame, text='Poke App')
        self.title.grid(row=0, column=0, rowspan=2)
        self.title.config(font = ('Arial', '18'), foreground = 'blue')
        # Combobox configurations for pokemon selection
        self.pokemon_entered = StringVar()
        self.combobox = ttk.Combobox(self.header_frame, textvariable=self.pokemon_entered)
        self.combobox.config(values=[val.name for key, val in pokedex_dict.items()])
        self.combobox.grid(row=3, column=0, columnspan=2, padx = 20, pady=20)
        self.combobox.set('Bulbasuar')

        # Frame for pokemon image and typing
        self.picture_frame = ttk.Frame(master)
        self.picture_frame.pack()
        self.pokemon_type1 = 'Grass'
        self.pokemon_type2 = 'Poison'
        self.pokemon_sprite = PhotoImage(file='crystal_sprites/1.gif')
        self.sprite_label = ttk.Label(self.picture_frame, image=self.pokemon_sprite)
        self.type1_label = ttk.Label(self.picture_frame, text=self.pokemon_type1)
        self.type2_label = ttk.Label(self.picture_frame, text=self.pokemon_type2)
        self.type1_label.grid(row=0, column=0)
        self.type2_label.grid(row=0, column=1)
        self.sprite_label.grid(row=1, column = 0, columnspan=2)

        # Frame for Pokemon stats
        self.stats_frame = ttk.Frame(master)
        self.stats_frame.pack()

        # Event binding for pokemon combobox selection
        self.combobox.bind("<<ComboboxSelected>>", self.get_pokemon)

    # These actions occur when a button is pressed
    def get_pokemon(self, event):
        pokemon_selected = self.combobox.get()
        pokedex_id = pokedex_dict[pokemon_selected].pokedex_id
        poke_sprite = PhotoImage(file=f'crystal_sprites/{pokedex_id}.gif')
        self.type1_label.config(text=pokedex_dict[pokemon_selected].type1)
        self.type2_label.config(text=pokedex_dict[pokemon_selected].type2)
        self.sprite_label.img = poke_sprite
        self.sprite_label.config(image=self.sprite_label.img)


pokemon_df = pd.read_csv('Pokemon_data.csv')

pokedex_dict = {}

for index, record in pokemon_df.iterrows():
    name = record['Name']
    pokedex_id = record['#']
    if "Mega" in name:
        continue
    type1 = record['Type 1']
    type2 = record['Type 2']
    hp = record['HP']
    attack = record['Attack']
    defense = record['Defense']
    spAtk = record['Sp. Atk']
    spDef = record['Sp. Def']
    speed = record['Speed']
    generation = record['Generation']

    if type2 == '':
        type2 = None

    pokedex_dict[name] = pokemon.Pokemon(name, pokedex_id, type1, type2, hp, attack, defense, spAtk,
                                         spDef, speed, gen=generation)