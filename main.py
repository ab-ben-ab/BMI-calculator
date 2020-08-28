from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
# bmi 
import bmi as bm
import bmi_pre_20 as pbm   
import inch_bmi as inbm
import pr_20_inch_bmi as inchpbm  

class bMi(BoxLayout):

    # text values for errors and result
    tailored_text = ""
    error_text = "[color=000330]Make sure all boxes are filled[/color]"
    value_error_text = "[color=000330]Make sure to input digits only[/color]"
    error_max_characters = "[color=000330]Character limit is 3, unless you are not human in which case my bad[/color]"

    def calculate(self, age, weight, height):
        try:
            if age == "" or weight == "" or height == "":
                self.throwerr(self.error_text)                                         # empty fields error
            elif float(weight) < 25 or float(height) < 40:                             
                self.snackbar = Snackbar(text="Weight or height too low")
                self.snackbar.show()                                                   # low number input error
            elif len(age) > 3 or len(weight) > 3 or len(height) > 3:
                self.throwerr(self.error_max_characters)                               # max characters exceeded error         
            
            # calculate for male who's pre 20
            elif int(age) < 21 and self.ids.male.state == "down":
                Bmi_male = pbm.male(height, weight)
                weight_target_bmi_male = pbm.suggest_weight()
                bmi_male_range = pbm.healthy_range()
                self.tailored_text = f"""[color=000330]{weight_target_bmi_male}[/color],[color=000330] {bmi_male_range} \n What does this mean? BMI, [color=ff00FF]or Body Mass Index[/color] is a value derived from the mass and height of a person. \nYour results come from comparing your bmi with the following categories:[/color]
                \n[color=ff00FF]underweight[/color][color=000330]:[/color] [color=000330]less than[/color] [color=ff00FF]18.5[/color] 
                \n[color=ff00FF]normal[/color][color=000330]:[/color] [color=ff00FF]18.5 - 25[/color]
                \n[color=ff00FF]overweight[/color][color=000330]:[/color] [color=ff00FF]25 - 30[/color]
                \n[color=ff00FF]obese[/color][color=000330]:[/color] [color=000330]more than[/color] [color=ff00FF]30[/color] """
                self.show_result()

            # calculate for female who's pre 20
            elif int(age) < 21 and self.ids.female.state == "down":
                Bmi_female = pbm.female(height, weight)
                female_range = pbm.healthy_range()
                weight_target_bmi_female = pbm.suggest_weight()
                self.tailored_text = f"""[color=000330]{weight_target_bmi_female}[/color],[color=000330] {female_range} \n What does this mean? BMI, [color=ff00FF]or Body Mass Index[/color] is a value derived from the mass and height of a person. \nYour results come from comparing your bmi with the following categories:[/color]
                \n[color=ff00FF]underweight[/color][color=000330]:[/color] [color=000330]less than[/color] [color=ff00FF]18.5[/color] 
                \n[color=ff00FF]normal[/color][color=000330]:[/color] [color=ff00FF]18.5 - 25[/color]
                \n[color=ff00FF]overweight[/color][color=000330]:[/color] [color=ff00FF]25 - 30[/color]
                \n[color=ff00FF]obese[/color][color=000330]:[/color] [color=000330]more than[/color] [color=ff00FF]30[/color] """
                self.show_result()
            
            # calculate for male or female who's over 20
            else:
                Bmi_any = bm.main(height, weight)
                weight_target_any_bmi = bm.suggest_weight()
                any_range = bm.healthy_range()
                self.tailored_text = f"""[color=000330]{weight_target_any_bmi}[/color],[color=000330] {any_range} \n What does this mean? BMI, [color=ff00FF]or Body Mass Index[/color] is a value derived from the mass and height of a person. \nYour results come from comparing your bmi with the following categories:[/color]
                \n[color=ff00FF]underweight[/color][color=000330]:[/color] [color=000330]less than[/color] [color=ff00FF]18.5[/color] 
                \n[color=ff00FF]normal[/color][color=000330]:[/color] [color=ff00FF]18.5 - 25[/color]
                \n[color=ff00FF]overweight[/color][color=000330]:[/color] [color=ff00FF]25 - 30[/color]
                \n[color=ff00FF]obese[/color][color=000330]:[/color] [color=000330]more than[/color] [color=ff00FF]30[/color] """
                self.show_result()
                
        except ValueError:
            self.throwerr(self.value_error_text)
            
    
    # changing to inch and calculating
    def calculate_in(self, age, weight, height):
        try:
            if age == "" or weight == "" or height == "":                               # empty input error
                self.throwerr(self.error_text)
                
            elif float(weight) < 20 or float(height) < 20:
                self.snackbar = Snackbar(text="Weight or height too low")
                self.snackbar.show()                                                    # number input too low error
                
            elif len(age) > 3 or len(weight) > 3 or len(height) > 4:
                self.throwerr(self.error_max_characters)                                # chars limit exceeded error
            
            # calculate for male who's under 20 in inch 
            elif int(age) < 21 and self.ids.inmale.state == "down":
                Bmi_male = inchpbm.male(height, weight)
                bmi_male_range = inchpbm.healthy_range()
                weight_target_bmi_male = inchpbm.suggest_weight()
                self.tailored_text = f"""[color=000330]{weight_target_bmi_male}[/color],[color=000330] {bmi_male_range} \n What does this mean? BMI, or [color=00b596]Body Mass Index[/color] is a value derived from the mass and height of a person. \nYour results come from comparing your bmi with the following categories:[/color]
                \n[color=00b596]underweight[/color][color=000330]:[/color] [color=000330]less than[/color] [color=00b596]18.5[/color] 
                \n[color=00b596]normal[/color][color=000330]:[/color] [color=00b596]18.5 - 25[/color]
                \n[color=00b596]overweight[/color][color=000330]:[/color] [color=00b596]25 - 30[/color]
                \n[color=00b596]obese[/color][color=000330]:[/color] [color=000330]more than[/color] [color=00b596]30[/color] """

                self.show_result()

            # calculate for female who's under 20 in inch
            elif int(age) < 21 and self.ids.infemale.state == "down":
                Bmi_female = inchpbm.female(height, weight)
                female_range = inchpbm.healthy_range()
                weight_target_bmi_female = inchpbm.suggest_weight()
                self.tailored_text = f"""[color=000330]{weight_target_bmi_female}[/color],[color=000330] {female_range} \n What does this mean? BMI, or [color=00b596]Body Mass Index[/color] is a value derived from the mass and height of a person. \nYour results come from comparing your bmi with the following categories:[/color]
                \n[color=00b596]underweight[/color][color=000330]:[/color] [color=000330]less than[/color] [color=00b596]18.5[/color] 
                \n[color=00b596]normal[/color][color=000330]:[/color] [color=00b596]18.5 - 25[/color]
                \n[color=00b596]overweight[/color][color=000330]:[/color] [color=00b596]25 - 30[/color]
                \n[color=00b596]obese[/color][color=000330]:[/color] [color=000330]more than[/color] [color=00b596]30[/color] """
                
                self.show_result()
            
            # calculate for male or female who's over 20 in inch
            else:
                Bmi_any_inch = inbm.main(height, weight)
                weight_target_any_bmi_inch = inbm.suggest_weight()
                any_range = inbm.healthy_range()
                self.tailored_text = f"""[color=000330]{weight_target_any_bmi_inch}[/color],[color=000330] {any_range} \n What does this mean? BMI, or [color=00b596]Body Mass Index[/color] is a value derived from the mass and height of a person. \nYour results come from comparing your bmi with the following categories:[/color]
                \n[color=00b596]underweight[/color][color=000330]:[/color] [color=000330]less than[/color] [color=00b596]18.5[/color] 
                \n[color=00b596]normal[/color][color=000330]:[/color] [color=00b596]18.5 - 25[/color]
                \n[color=00b596]overweight[/color][color=000330]:[/color] [color=00b596]25 - 30[/color]
                \n[color=00b596]obese[/color][color=000330]:[/color] [color=000330]more than[/color] [color=00b596]30[/color] """
                
                self.show_result()
                
        except ValueError:
            self.throwerr(self.value_error_text)

    # dialog box for the result   
    def show_result(self):                          
        self.dialog = MDDialog(
        text=self.tailored_text,
        buttons = [
            MDFlatButton(text= "Clear",
            on_release=self.clear),
            MDFlatButton(text="Ok",
            on_release= self.dialog_dismiss)
        ],
        title="Your results:",
        size_hint=(1, 4),
        )
        self.dialog.open()

    # dialog box for errors
    def throwerr(self, err_text):               
        self.dialog = MDDialog(
            text = err_text,
            buttons = [
                MDFlatButton(text="Ok",
                on_press= self.dialog_dismiss)
            ],
            title="Error",
            radius = [20, 7, 20, 7],
            size_hint=(0.7, 1),
            )
        self.dialog.open()


    def dialog_dismiss(self, instance):
        self.dialog.dismiss()

    # clearing inputs
    def clear(self, instance):
        self.ids.age.text = ""
        self.ids.textinheight.text = ""
        self.ids.textinweight.text = ""
        self.ids.inage.text = ""
        self.ids.inheight.text = ""
        self.ids.inweight.text = ""
        
        self.snackbar = Snackbar(text="  Cleared!")
        self.snackbar.show()

        
class bmapp(MDApp):
    def on_start(self):                                         
        Clock.schedule_once(self.intro, .2)
        # scheduling the intro dialog box

    def intro(self, args):
        self.dialog = MDDialog(
            text="[color=000330]This app calculates your [color=ff00FF]BMI[/color] (body mass index) and gives weight suggestions based on your results, to change to your preferred measurement system press the [color=ff00FF]menu[/color] [color=000330]button[/color], [color=ff00FF]This app is not a perfect metric for your health, for any serious inquiries check with a certified professional[/color] [color=000330]and love yourself bitch :)[/color]",
            title="Thank you for using this app",
            buttons = [MDFlatButton(
                text = "Ok",
                on_release=self.dismiss                                             
                )],
            radius = [20, 7, 20, 7],
            size_hint=(0.7, 1))
        self.dialog.open()

        
    def dismiss(self, instance):
        self.dialog.dismiss()

        
    def build(self):
        return bMi()

bmapp().run()