


# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.boxlayout import BoxLayout
#
# Builder.load_file("QuizPage.kv")
# class QuizPageApp(App):
#     def build(self):
#         return QuizManager()
#
#
# class QuizManager(ScreenManager):
#     pass
#
# class Question1Screen(Screen, BoxLayout):
#     def answer_question(self, bool):
#         if bool:
#             self.manager.current = "correct"
#         else:
#             self.manager.current = "incorrect"
#
#
# class Question2Screen(Screen, BoxLayout):
#     def answer_question(self,text):
#         if text.lower() == "yes":
#             # self.manager.current = "correct"
#             self.ids.test.text = "CORRECT"
#             self.ids.test.font_size = 100
#             self.ids.test.color = "blue"
#         elif text == "no":
#             # self.manager.current = "incorrect"
#             self.ids.test.text = "WRONG"
#             self.ids.test.font_size = 100
#             self.ids.test.color = "green"
#
# class CorrectScreen(Screen, BoxLayout):
#     def go_back(self):
#         self.manager.current = "question two"
#
#
# class IncorrectScreen(Screen, BoxLayout):
#     def go_back(self):
#         self.manager.current = "question two"
#
# QuizPageApp().run()




from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

Builder.load_file("LoginPage.kv")
class LoginPageApp(App):
    def build(self):
        return LoginManager()


class LoginManager(ScreenManager):
    pass

class LoginPageScreen(Screen, BoxLayout, GridLayout):
    def land(self,username,password):
        if username in user_login and user_login[username]==password:
            self.manager.current = "landing"
        else:
            self.ids.invalid.text = "INVALID CREDENTIALS"
    def register(self):
        self.manager.current = "Register"


class LandingScreen(Screen, BoxLayout):
    def land_to_login(self):
        self.manager.current = "login page"

class RegisterScreen(Screen, BoxLayout, GridLayout):
    def register_to_login(self, new_username, new_password, reenter_new_password):
        if new_username in user_login or new_password != reenter_new_password or not self.contain_num(new_password) or not self.special_char(new_password) or not self.lower_case(new_password) or not self.upper_case(new_password):
            self.ids.error.text = "ERROR"
            self.ids.error.font_size = 50
        else:
            user_login[new_username] = new_password
            print(user_login)
            self.manager.current = "login page"


    def contain_num(self, new_password):
        for char in new_password:
            if char in "0123456789":
                return True
        return False

    def special_char(self, new_password):
        for char in new_password:
            if char in "!@#$%^&*":
                return True
        return False
    def lower_case(self, new_password):
        for char in new_password:
            if char in "abcdefghijklmnopqrstuvwxyz":
                return True
        return False
    def upper_case(self, new_password):
        for char in new_password:
            if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                return True
        return False




user_login = {"username":"password"}

LoginPageApp().run()
