from tkinter import *
from tkinter import ttk
import pokemon
import pandas as pd
from random import randint


class Pokedex:
    # all widgets are created in the def __init__
    def __init__(self, master):
        # This label is a child of the master window
        self.label = ttk.Label(master, text = 'Pokedex Demo')
        self.label.grid(row = 0, column = 0, columnspan=2)
        self.label.config(foreground='Red')
        self.label.config(font=('Arial', 18, 'bold'))

        self.label2 = ttk.Label(master, text='Random Pokemon Genertor')
        self.label2.grid(row=1, column=0, columnspan=2)
        self.label2.config(foreground = 'Red')
        self.label2.config(font='Arial')

        self.label3 = ttk.Label(master, text='Pokemon')
        self.label3.grid(row=4, column=0, columnspan=3)

        # the command argument indicates what command is called when the button is pressed
        ttk.Button(master, text = 'Gen 1', command = self.gen1_rand_pokemon).grid(row = 2, column = 0)
        ttk.Button(master, text='Gen 2', command=self.gen2_rand_pokemon).grid(row=2, column=1)

    # These actions occur when a button is pressed
    def gen1_rand_pokemon(self):
        pokedex_id = (randint(1,151))
        poke = PhotoImage(file=f'crystal_sprites/{pokedex_id}.gif')
        self.label3.config(text = pokedex_dict[pokedex_id].name)
        self.label3.config(compound='left')
        self.label3.img = poke
        self.label3.config(image=self.label3.img)

    def gen2_rand_pokemon(self):
        pokedex_id = (randint(152,251))
        poke = PhotoImage(file=f'crystal_sprites/{pokedex_id}.gif')
        self.label3.config(text=pokedex_dict[pokedex_id].name)
        self.label3.config(compound='left')
        self.label3.img = poke
        self.label3.config(image=self.label3.img)


pokemon_df = pd.read_csv('Pokemon_data.csv')

pokedex_dict = {}

for index, record in pokemon_df.iterrows():
    name = record['Name']
    pokedex_id = record['#']
    if pokedex_id in pokedex_dict:
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

    pokedex_dict[pokedex_id] = pokemon.Pokemon(name, pokedex_id, type1, type2, hp, attack, defense, spAtk,
                                         spDef, speed, gen=generation)
