"""
Creates a surcure password
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import random
import pandas as pd
import os


class PasswordGenorator(toga.App):

    def generate_password(self, widget):
        self.password.value = ''
        # generate a password based on the user's input
        # get the password length
        length = self.length_input.value
        # get the password options
        numbers = self.numbers.is_on
        caps = self.caps.is_on
        symbols = self.symbols.is_on
        # create a list of all the characters that will be used for the password
        characters = []
        if numbers:
            characters.append('0123456789')
        if caps:
            characters.append('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if symbols:
            characters.append('!\\@#$%^&*()_+-=[]{};\':"<>?,./')
        # create the password
        password = ''
        characters.append("abcdefghijklmnopqrstuvwxyz")
        for i in range(0, int(length)):
            # randomly select a character from the list of characters
            character = random.choice(characters)
            # add the character to the password
            password += random.choice(character)
        # display the password in the text input field
        self.password.value = password
            

    def copy_password(self, widget):
        print(os.walk('.'))
        # put the password value to the text.txt file
        with open('text.txt', 'w') as file:
            file.write(self.password.value)
            file.close()

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        number_box = toga.Box(style=Pack(direction=ROW))
        option_box = toga.Box(style=Pack(direction=ROW))
        button_box = toga.Box(style=Pack(direction=ROW))

        # create a label title in the top center of the screen
        title = toga.Label('Password Generator', style=Pack(padding_top=10, alignment="top", text_align="center", font_size=20))
        # create a number input field for the length of the password
        numbers_l = toga.Label('How long: ', style=Pack(flex=3, font_size=16, padding_top=9))
        self.length_input = toga.NumberInput(style=Pack(flex=10, font_size=16, padding_top=9, padding_left=6), max_value=200, min_value=1)
        # create some radio buttons for the type of password E.G (numbers, letters, symbols)
        o_label = toga.Label('Options: ', style=Pack(flex=1, font_size=16, padding_top=10))
        self.numbers = toga.Switch(label='Numbers', style=Pack(padding_top=10, flex=1, font_size=16))
        self.caps = toga.Switch(label='Letters', style=Pack(padding_top=10, flex=1, font_size=16))
        self.symbols = toga.Switch(label='Symbols', style=Pack(padding_top=10, flex=1, font_size=16))
        # create a button to generate the password
        generate = toga.Button('Generate', style=Pack(padding_top=10, flex=0.5, font_size=16), on_press=self.generate_password)
        # create a text input field to display the password
        self.password = toga.MultilineTextInput(style=Pack(padding_top=10, flex=1, font_size=16))
        # create a button to copy the password to the clipboard
        copy = toga.Button('Copy', style=Pack(padding_top=10, flex=0.5, font_size=16), on_press=self.copy_password)

        # add the widgets to the main box
        number_box.add(numbers_l); number_box.add(self.length_input)
        option_box.add(o_label); option_box.add(self.numbers); option_box.add(self.caps); option_box.add(self.symbols)
        button_box.add(generate); button_box.add(copy)
        main_box.add(title); main_box.add(number_box); main_box.add(option_box); main_box.add(button_box);  main_box.add(self.password)
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        
        
def main():
    return PasswordGenorator()
