import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols=1
        self.inside=GridLayout()
        self.inside.cols=2
        #Creating the label
        self.inside.add_widget(Label(text="Numero1"))
        self.num=TextInput(multiline=False)
        self.inside.add_widget(self.num)
        #Create the 2° Label
        self.inside.add_widget(Label(text="Numero2"))
        self.nume=TextInput(multiline=False)
        self.inside.add_widget(self.nume)
        #We assign here the variable to the label
        self.suma=(Label(text=""))
        self.inside.add_widget(self.suma)
        #Esta linea de aqui abajo es para que se agregue todo lo de arriba
        self.add_widget(self.inside)
#Agregando el boton
        self.submit=Button(text="Calcular",font_size=20)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    def pressed(self,instance):
        num1=int(self.num.text)
        num2=int(self.nume.text)
        s=num1+num2
        print("{0}".format(s))
        self.suma.text=("La suma es {0}".format(s))
class MyApp(App):
    def build(self):
        return MyGrid()
if __name__ =="__main__":
    MyApp().run()
