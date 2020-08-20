import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from colorama import init, Fore, Back, Style
from kivy.uix.popup import Popup
from kivy.core.image import Image
from kivy.core.audio import SoundLoader
init()

red = [1, 0, 0, 1]  
green = [0, 1, 0, 1]  
blue = [0, 0, 1, 1]  
purple = [1, 0, 1, 1]
white = [255, 255, 255, 1]
black = [0,0,0,1]
grey = [120,120,120,1]

class MyGrid(GridLayout):

    def __init__(self, **kwargs):

        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.orbbutton = Button(size_hint =(.8, .4), text ="Opening Range Breakout", background_normal = '2.jpg', font_size = 40)
        self.orbbutton.bind(on_press = self.orbgrid)
        self.add_widget(self.orbbutton)

        self.modorbbutton = Button(size_hint =(.8, .4), text ="Modified Opening Range Breakout", background_normal = '2.jpg', font_size = 40)
        self.modorbbutton.bind(on_press = self.modorbgrid)
        self.add_widget(self.modorbbutton)

    def orbgrid(self, instance, **kwargs):
        layout = GridLayout(cols = 1)
        layout1 = GridLayout(cols = 2)
        texture = Image('2.jpg').texture
        self.sound = SoundLoader.load("myalert.wav")
        self.sound.play()
        label_balance = Button(text = 'Balance', background_color = black, font_size = (self.size[0]/15))
        self.balance_input = TextInput(multiline=False, font_size = (self.height/7), halign = "center")
        layout1.add_widget(label_balance)
        layout1.add_widget(self.balance_input)
        label_high = Button(text = 'High', background_color = black, font_size = (self.size[0]/15))
        self.high1 = TextInput(multiline=False, font_size = (self.height/7), halign = "center")
        layout1.add_widget(label_high)
        layout1.add_widget(self.high1)
        label_low = Button(text = 'Low', background_color = black, font_size = (self.size[0]/15))
        self.low1 = TextInput(multiline=False, font_size = (self.height/7), halign = "center")
        layout1.add_widget(label_low)
        layout1.add_widget(self.low1)
        layout.add_widget(layout1)
        submit_button = Button(text ="Submit", background_color = blue, font_size = 30, height = (self.size[0]/10), size_hint_y=None, width=(self.size[0]/15))
        submit_button.bind(on_press = self.orbsubmit)
        layout.add_widget(submit_button)
        back_button = Button(size_hint_y=None, width=(self.size[0]/15), text = '<<<', height = (self.size[0]/10), background_color = black, font_size = 50)
        layout.add_widget(back_button)
        popup = Popup(title ="Opening Range Breakout", content = layout)   
        popup.open()
        back_button.bind(on_press = popup.dismiss)

    def orbsubmit(self, instance):
        balance = int(self.balance_input.text)
        risk = float(0.02)
        high = float(self.high1.text)
        low = float(self.low1.text)
        stoploss = round((high + low)/2, 2)
        target_buy = high + (high - low)
        target_sell = low - (high - low)
        quantity = round((2 * risk * balance)/(target_buy - high))
        turnover = quantity*(high+target_buy)
        brokerage = 40
        stt = round(turnover * 0.000125, 0)
        exchangetxn = round(turnover * 0.0000325, 2)
        clearingcharge = 0
        gst = round((brokerage + exchangetxn) * 0.18, 2)
        sebi = round(turnover/1000000, 2)
        charges = round(brokerage + stt + exchangetxn + clearingcharge + gst + sebi, 2)
        newcharg = charges/quantity
        finaltargetbuy = round(target_buy+newcharg, 2)
        finaltargetsell = round(target_sell-newcharg, 2)
        finalstoplossbuy = round(stoploss+newcharg, 2)
        finalstoplosssell = round(stoploss-newcharg, 2)
        q_str = '    Quantity - ' + str(quantity)
        high_breaks = '***If high breaks***\n     Target - ' + \
            str(finaltargetbuy) + '\n     Stoploss - ' + str(finalstoplossbuy)
        low_breaks = '***If low breaks***\n     Target - ' + \
            str(finaltargetsell) + '\n     Stoploss - ' + str(finalstoplosssell)
        submitlayout1 = GridLayout(cols = 1)
        label_submit1 = Button(text =  q_str + '\n' + high_breaks + '\n' + low_breaks, background_color = black, font_size=35)
        submitlayout1.add_widget(label_submit1)
        submitback1 = Button(size_hint =(.8, .4), text = 'Back', background_color = blue, font_size = 20)
        submitlayout1.add_widget(submitback1)
        submitnotify = Button(size_hint =(.8, .4), text = 'Notify Me', background_color = blue, font_size = 20)
        submitnotify.bind(on_press = self.show_notification)
        submitlayout1.add_widget(submitnotify)
        popupsubmit1 = Popup(title = 'Output', content = submitlayout1)
        popupsubmit1.open()
        submitback1.bind(on_press = popupsubmit1.dismiss)

    def show_notification(self, instance):
        self.sound = SoundLoader.load("myalert.wav")
        self.sound.play()

    def modorbgrid(self, instance, **kwargs):
        layout = GridLayout(cols = 1)
        layout1 = GridLayout(cols = 2)
        texture = Image('2.jpg').texture
        label_balance = Button(text = 'Balance', background_color = black, font_size = (self.size[0]/15))
        self.balance_input = TextInput(multiline=False, font_size = (self.height/7), halign = "center")
        layout1.add_widget(label_balance)
        layout1.add_widget(self.balance_input)
        label_high = Button(text = 'High', background_color = black, font_size = (self.size[0]/15))
        self.high1 = TextInput(multiline=False, font_size = (self.height/7), halign = "center")
        layout1.add_widget(label_high)
        layout1.add_widget(self.high1)
        label_low = Button(text = 'Low', background_color = black, font_size = (self.size[0]/15))
        self.low1 = TextInput(multiline=False, font_size = (self.height/7), halign = "center")
        layout1.add_widget(label_low)
        layout1.add_widget(self.low1)
        layout.add_widget(layout1)
        submit_button = Button(text ="Submit", background_color = blue, font_size = 30,height = (self.size[0]/10), size_hint_y=None, width=20)
        submit_button.bind(on_press = self.modorbsubmit)
        layout.add_widget(submit_button)
        back_button = Button(size_hint_y=None, width=20, text = '<<<', height = (self.size[0]/10), background_color = black, font_size = 50)
        layout.add_widget(back_button)
        popup = Popup(title ="Modified Opening Range Breakout", content = layout)   
        popup.open()
        back_button.bind(on_press = popup.dismiss)

    def modorbsubmit(self, instance):
        high = float(self.high1.text)
        buy_price = float(high + 0.05)
        low = float(self.low1.text)
        sell_price = float(low - 0.05)
        low_s = str(int(low))
        list1 = []
        list1.append(str(low))
        balance = int(self.balance_input.text)
        riskinput = 2
        target = balance * 0.05
        if len(low_s) == 2 :
            target_points = '0.' + low_s[0]
        elif len(low_s) == 3:
            target_points = low_s[0]
        elif len(low_s) == 4:
            target_points = low_s[0] + '0'
        elif len(low_s) == 5:
            target_points = low_s[0] + low_s[1] + '0'
        quantity = int(target / float(target_points))
        finaltargetbuy = (high + float(target_points))
        finaltargetsell = (low - float(target_points))
        q_str = '    Quantity - ' + str(quantity) + '\nBuy Trigger Price - ' + str(high) + '\nBuy Price - ' + str(buy_price) +'\nSell Trigger Price - ' + str(low) + '\nSell Price - ' + str(sell_price)
        high_breaks = '***If high breaks***\n     Target - ' + \
            str(finaltargetbuy) + '\n     Stoploss - ' + str(low)
        low_breaks = '***If low breaks***\n     Target - ' + \
            str(finaltargetsell) + '\n     Stoploss - ' + str(high)
        submitlayout1 = GridLayout(cols = 1)
        label_submit1 = Button(text =  q_str + '\n' + high_breaks + '\n' + low_breaks, background_color = black , font_size=50)
        submitlayout1.add_widget(label_submit1)
        submitback1 = Button(size_hint =(.8, .4), text = 'Back', background_color = blue, font_size = 30)
        submitlayout1.add_widget(submitback1)
        popupsubmit1 = Popup(title = 'Output', content = submitlayout1, font_size = 50)
        popupsubmit1.open()
        submitback1.bind(on_press = popupsubmit1.dismiss)

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()