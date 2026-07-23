from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
import math


class MainLayout(BoxLayout):
      
    history = []

    def add_to_history(self, expression, result):
        self.history.append(f"{expression} = {result}")
    
    def show_history(self, *args):

        text = "\n".join(self.history)

        dialog = MDDialog(
            title="History",
            text=text if text else "No calculations yet.",
            buttons=[
                MDFlatButton(
                    text="CLOSE",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )

        dialog.open()


    def clear_history(self):
        self.history.clear()
        if hasattr(self, "menu"):
            self.menu.dismiss()

            dialog = MDDialog(
                title ="Success",
                text="History cleared successfully!",
                buttons=[
                MDFlatButton(
                        text="OK",
                        on_release=lambda x: dialog.dismiss()
                )
              ]
            )

            dialog.open()


    def show_menu(self, caller):

        menu_items = [
            {
                "text": "Scientific Mode",
                "on_release": lambda: self.scientific_mode()
            },
            {
                "text": "Clear History",
                "on_release": lambda: self.clear_history()
            },
            {
                "text": "About",
                "on_release": lambda: self.about()
            }
            ]

        self.menu = MDDropdownMenu(
            caller = caller,
            items=menu_items,
            width_mult=4
            )

        self.menu.open()

    def about(self):
        if hasattr(self, "menu"):
            self.menu.dismiss()
        dialog = MDDialog(
            title = "About", 
            text="""
        Calculator v1.0

        Developer: Aryan Rai

        Features:
        • Basic Calculator
        • History
        • Scientific Mode
        • Material Design UI

        Built with:
        Python
        Kivy
        KivyMD
        """,
        buttons=[
            MDFlatButton(
                text="Close",
                on_release=lambda x: dialog.dismiss()
                )
            ]
        )

        dialog.open()

    def scientific_mode(self):
        if hasattr(self, "menu"):
            self.menu.dismiss()
        dialog = MDDialog(
            title = "Scientific Mode",
            text = "Scientific mode is under development and will be available in future updates.",
            buttons = [
                MDFlatButton(
                    text="close",
                    on_release = lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()
       

class Calculator(MDApp):
   

    def build(self):
    
        
        return Builder.load_file("main.kv")
    
       

class CalcGridLayout(GridLayout):

    from kivy.app import App

    def calculate(self, calculation):
        if calculation:
            try:
                result = str(eval(calculation))
                self.display.text = result

                app = App.get_running_app()
                app.root.add_to_history(calculation, result)

            except Exception:
                self.display.text = "Error" 

    def delete_last(self):
        self.display.text = self.display.text[:-1]            



Calculator().run()

