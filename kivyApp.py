import kivy
# imported to build all the graphics and windows related to an App, Grid layout, and to use text, buttons
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# using a grid layout insidegrid a class
class FirstGrid(GridLayout):

    # creating the initialization __init__
    # two stars meaning can get infinite amount of keywords
    # kwargs means keywords
    def __init__(self, **kwargs):

        # calling the GridLayout constructor and setting up
        super(FirstGrid, self).__init__(**kwargs)

        # creating another insidegrid grid layout and assigning the number of columns in the grid
        self.insidegrid = GridLayout()
        self.insidegrid.cols = 2

        # Assigning the number of columns in the main grid
        self.cols = 1

        # Adding a topic as a widget
        self.topic = Label(text="MY DETAILS", font_size=25, size_hint_y=None, height=52)
        self.add_widget(self.topic)

        # Adding widgets
        self.insidegrid.add_widget(Label(text="My First Name: ", font_size=16))
        # Removing multi-lines
        self.firstname = TextInput(multiline=False)
        # Add the widget accordingly
        self.insidegrid.add_widget(self.firstname)

        # Adding widgets
        self.insidegrid.add_widget(Label(text="My Last Name: ", font_size=16))
        # Removing multi-lines
        self.lastname = TextInput(multiline=False)
        # Add the widget accordingly
        self.insidegrid.add_widget(self.lastname)

        # Adding widgets
        self.insidegrid.add_widget(Label(text="My Email: ", font_size=16))
        # Removing multi-lines
        self.myemail = TextInput(multiline=False)
        # Add the widget accordingly
        self.insidegrid.add_widget(self.myemail)

        # To add the inside grid in the main grid as a widget
        self.add_widget(self.insidegrid)

        # Adding a submit button
        self.submit = Button(text="Submit", font_size=34, size_hint_y=None, height=70)
        self.submit.bind(on_press=self.clicked)
        self.add_widget(self.submit)

    # Function which allows to display the details on click
    def clicked(self, instance):
        print("CLICKED\n")
        topic = self.topic.text
        firstName = self.firstname.text
        lastName = self.lastname.text
        email = self.myemail.text
        instance = f"My Full name: {firstName} {lastName}\nMy Email Address: {email}"
        print(f"{topic}\n{instance}")

        # Writing the details to a .txt file
        with open('My Details.txt', 'w') as s:
            s.write(topic)
            s.write('\n----------------------- \n')
            s.write(str(instance))

        # To clear the text area when clicked on submit
        self.firstname.text = ""
        self.lastname.text = ""
        self.myemail.text = ""



# Creating a class and use App functions in kivy, insidegrid the class FirstApp class created below
# By default calling the constructor in the main App class
class FirstApp(App):
    def build(self):
        return FirstGrid()
        # return Label(text="My name is Gavin Manjitha.")


# Even-though we didn't run method, because insidegrid the App class there's a default run method
if __name__ == "__main__":
    # calling the function above and run it
    FirstApp().run()
