class game_begin:
    def __init__(self, random, app):
        self.random = random
        self.app = app
        self.pin_colors = ['white', 'green', 'blue', 'red', 'yellow', 'black']      
        self.set_the_real_colors()
        self.app.build_1st_row()
    def set_the_real_colors(self):
        self.real_color1 = self.random.choice(self.pin_colors)
        self.real_color2 = self.random.choice(self.pin_colors)
        self.real_color3 = self.random.choice(self.pin_colors)
        self.real_color4 = self.random.choice(self.pin_colors)
        self.correct_respond = [self.real_color1, self.real_color2, self.real_color3, self.real_color4]

class game_events:
    def __init__(self, app, gui_events, game_begin, random):
        self.app = app
        self.gui_events = gui_events
        self.game_begin = game_begin
        self.random = random
        self.button1_color_number = 4
        self.button2_color_number = 4
        self.button3_color_number = 4
        self.button4_color_number = 4
        self.correct_respond = game_begin.correct_respond
        # print(self.correct_respond)
        self.real_color1 = game_begin.real_color1
        self.real_color2 = game_begin.real_color2
        self.real_color3 = game_begin.real_color3
        self.real_color4 = game_begin.real_color4
        self.button1_color = 'white'
        self.button2_color = 'white'
        self.button3_color = 'white'
        self.button4_color = 'white'
        self.try_level = 1
        self.set_command()

    def what_button_1(self): # whate level we should do on it
        if self.try_level == 1:
            return self.app.guess_button1_1
        elif self.try_level == 2:
            return self.app.guess_button1_2
        elif self.try_level == 3:
            return self.app.guess_button1_3
        elif self.try_level == 4:
            return self.app.guess_button1_4
        elif self.try_level == 5:
            return self.app.guess_button1_5
        elif self.try_level == 6:
            return self.app.guess_button1_6
        elif self.try_level == 7:
            return self.app.guess_button1_7
        elif self.try_level == 8:
            return self.app.guess_button1_8
        elif self.try_level == 9:
            return self.app.guess_button1_9
        elif self.try_level == 10:
            return self.app.guess_button1_10
    def what_button_2(self): # whate level we should do on it
        if self.try_level == 1:
            return self.app.guess_button2_1
        elif self.try_level == 2:
            return self.app.guess_button2_2
        elif self.try_level == 3:
            return self.app.guess_button2_3
        elif self.try_level == 4:
            return self.app.guess_button2_4
        elif self.try_level == 5:
            return self.app.guess_button2_5
        elif self.try_level == 6:
            return self.app.guess_button2_6
        elif self.try_level == 7:
            return self.app.guess_button2_7
        elif self.try_level == 8:
            return self.app.guess_button2_8
        elif self.try_level == 9:
            return self.app.guess_button2_9
        elif self.try_level == 10:
            return self.app.guess_button2_10
    def what_button_3(self): # whate level we should do on it
        if self.try_level == 1:
            return self.app.guess_button3_1
        elif self.try_level == 2:
            return self.app.guess_button3_2
        elif self.try_level == 3:
            return self.app.guess_button3_3
        elif self.try_level == 4:
            return self.app.guess_button3_4
        elif self.try_level == 5:
            return self.app.guess_button3_5
        elif self.try_level == 6:
            return self.app.guess_button3_6
        elif self.try_level == 7:
            return self.app.guess_button3_7
        elif self.try_level == 8:
            return self.app.guess_button3_8
        elif self.try_level == 9:
            return self.app.guess_button3_9
        elif self.try_level == 10:
            return self.app.guess_button3_10
    def what_button_4(self): # whate level we should do on it
        if self.try_level == 1:
            return self.app.guess_button4_1
        elif self.try_level == 2:
            return self.app.guess_button4_2
        elif self.try_level == 3:
            return self.app.guess_button4_3
        elif self.try_level == 4:
            return self.app.guess_button4_4
        elif self.try_level == 5:
            return self.app.guess_button4_5
        elif self.try_level == 6:
            return self.app.guess_button4_6
        elif self.try_level == 7:
            return self.app.guess_button4_7
        elif self.try_level == 8:
            return self.app.guess_button4_8
        elif self.try_level == 9:
            return self.app.guess_button4_9
        elif self.try_level == 10:
            return self.app.guess_button4_10
    def change_color_button1(self):
        if self.button1_color_number == 5: # make a var for color
            self.gui_events.change_to_white(self.what_button_1())
            self.button1_color_number -= 1
            self.button1_color = 'white'
        elif self.button1_color_number == 4:
            self.gui_events.change_to_green(self.what_button_1())
            self.button1_color_number -= 1
            self.button1_color = 'green'
        elif self.button1_color_number == 3:
            self.gui_events.change_to_blue(self.what_button_1())
            self.button1_color_number -= 1
            self.button1_color = 'blue'
        elif self.button1_color_number == 2:
            self.gui_events.change_to_red(self.what_button_1())
            self.button1_color_number -= 1
            self.button1_color = 'red'
        elif self.button1_color_number == 1:
            self.gui_events.change_to_yellow(self.what_button_1())
            self.button1_color_number -= 1
            self.button1_color = 'yellow'
        elif self.button1_color_number == 0:
            self.gui_events.change_to_black(self.what_button_1())
            self.button1_color_number = 5
            self.button1_color = 'black'
    def change_color_button2(self):
        if self.button2_color_number == 5: # make a var for color
            self.gui_events.change_to_white(self.what_button_2())
            self.button2_color_number -= 1
            self.button2_color = 'white'
        elif self.button2_color_number == 4:
            self.gui_events.change_to_green(self.what_button_2())
            self.button2_color_number -= 1
            self.button2_color = 'green'
        elif self.button2_color_number == 3:
            self.gui_events.change_to_blue(self.what_button_2())
            self.button2_color_number -= 1
            self.button2_color = 'blue'
        elif self.button2_color_number == 2:
            self.gui_events.change_to_red(self.what_button_2())
            self.button2_color_number -= 1
            self.button2_color = 'red'
        elif self.button2_color_number == 1:
            self.gui_events.change_to_yellow(self.what_button_2())
            self.button2_color_number -= 1
            self.button2_color = 'yellow'
        elif self.button2_color_number == 0:
            self.gui_events.change_to_black(self.what_button_2())
            self.button2_color_number = 5
            self.button2_color = 'black'
    def change_color_button3(self):
        if self.button3_color_number == 5: # make a var for color
            self.gui_events.change_to_white(self.what_button_3())
            self.button3_color_number -= 1
            self.button3_color = 'white'
        elif self.button3_color_number == 4:
            self.gui_events.change_to_green(self.what_button_3())
            self.button3_color_number -= 1
            self.button3_color = 'green'
        elif self.button3_color_number == 3:
            self.gui_events.change_to_blue(self.what_button_3())
            self.button3_color_number -= 1
            self.button3_color = 'blue'
        elif self.button3_color_number == 2:
            self.gui_events.change_to_red(self.what_button_3())
            self.button3_color_number -= 1
            self.button3_color = 'red'
        elif self.button3_color_number == 1:
            self.gui_events.change_to_yellow(self.what_button_3())
            self.button3_color_number -= 1
            self.button3_color = 'yellow'
        elif self.button3_color_number == 0:
            self.gui_events.change_to_black(self.what_button_3())
            self.button3_color_number = 5
            self.button3_color = 'black'
    def change_color_button4(self):
        if self.button4_color_number == 5: # make a var for color
            self.gui_events.change_to_white(self.what_button_4())
            self.button4_color_number -= 1
            self.button4_color = 'white'
        elif self.button4_color_number == 4:
            self.gui_events.change_to_green(self.what_button_4())
            self.button4_color_number -= 1
            self.button4_color = 'green'
        elif self.button4_color_number == 3:
            self.gui_events.change_to_blue(self.what_button_4())
            self.button4_color_number -= 1
            self.button4_color = 'blue'
        elif self.button4_color_number == 2:
            self.gui_events.change_to_red(self.what_button_4())
            self.button4_color_number -= 1
            self.button4_color = 'red'
        elif self.button4_color_number == 1:
            self.gui_events.change_to_yellow(self.what_button_4())
            self.button4_color_number -= 1
            self.button4_color = 'yellow'
        elif self.button4_color_number == 0:
            self.gui_events.change_to_black(self.what_button_4())
            self.button4_color_number = 5
            self.button4_color = 'black'
    def black_and_white(self):
        correct_respond1 = [self.real_color1, self.real_color2, self.real_color3, self.real_color4]
        self.resulte_list = []
        guess_list = [self.button1_color, self.button2_color, self.button3_color, self.button4_color]
        if True:
            if self.button1_color == self.correct_respond[0]:
                self.resulte_list.append('#000000')
                correct_respond1.remove(self.button1_color)
                guess_list.remove(self.button1_color)
            if self.button2_color == self.correct_respond[1]:
                self.resulte_list.append('#000000')
                correct_respond1.remove(self.button2_color)
                guess_list.remove(self.button2_color)
            if self.button3_color == self.correct_respond[2]:
                self.resulte_list.append('#000000')
                correct_respond1.remove(self.button3_color)
                guess_list.remove(self.button3_color)
            if self.button4_color == self.correct_respond[3]:
                self.resulte_list.append('#000000')
                correct_respond1.remove(self.button4_color)
                guess_list.remove(self.button4_color)
            if self.button1_color in correct_respond1 and self.button1_color in guess_list:
                self.resulte_list.append('#ffffff')
                correct_respond1.remove(self.button1_color)
                guess_list.remove(self.button1_color)
            if self.button2_color in correct_respond1 and self.button2_color in guess_list:
                self.resulte_list.append('#ffffff')
                correct_respond1.remove(self.button2_color)
                guess_list.remove(self.button2_color)
            if self.button3_color in correct_respond1 and self.button3_color in guess_list:
                self.resulte_list.append('#ffffff')
                correct_respond1.remove(self.button3_color)
                guess_list.remove(self.button3_color)
            if self.button4_color in correct_respond1 and self.button4_color in guess_list:
                self.resulte_list.append('#ffffff')
                correct_respond1.remove(self.button4_color)
                guess_list.remove(self.button4_color)
    def set_command(self):
        self.app.guess_button1_1['command'] = self.change_color_button1
        self.app.guess_button2_1['command'] = self.change_color_button2
        self.app.guess_button3_1['command'] = self.change_color_button3
        self.app.guess_button4_1['command'] = self.change_color_button4
        self.app.guess_button1_2['command'] = self.change_color_button1
        self.app.guess_button2_2['command'] = self.change_color_button2
        self.app.guess_button3_2['command'] = self.change_color_button3
        self.app.guess_button4_2['command'] = self.change_color_button4
        self.app.guess_button1_3['command'] = self.change_color_button1
        self.app.guess_button2_3['command'] = self.change_color_button2
        self.app.guess_button3_3['command'] = self.change_color_button3
        self.app.guess_button4_3['command'] = self.change_color_button4
        self.app.guess_button1_4['command'] = self.change_color_button1
        self.app.guess_button2_4['command'] = self.change_color_button2
        self.app.guess_button3_4['command'] = self.change_color_button3
        self.app.guess_button4_4['command'] = self.change_color_button4
        self.app.guess_button1_5['command'] = self.change_color_button1
        self.app.guess_button2_5['command'] = self.change_color_button2
        self.app.guess_button3_5['command'] = self.change_color_button3
        self.app.guess_button4_5['command'] = self.change_color_button4
        self.app.guess_button1_6['command'] = self.change_color_button1
        self.app.guess_button2_6['command'] = self.change_color_button2
        self.app.guess_button3_6['command'] = self.change_color_button3
        self.app.guess_button4_6['command'] = self.change_color_button4
        self.app.guess_button1_7['command'] = self.change_color_button1
        self.app.guess_button2_7['command'] = self.change_color_button2
        self.app.guess_button3_7['command'] = self.change_color_button3
        self.app.guess_button4_7['command'] = self.change_color_button4
        self.app.guess_button1_8['command'] = self.change_color_button1
        self.app.guess_button2_8['command'] = self.change_color_button2
        self.app.guess_button3_8['command'] = self.change_color_button3
        self.app.guess_button4_8['command'] = self.change_color_button4
        self.app.guess_button1_9['command'] = self.change_color_button1
        self.app.guess_button2_9['command'] = self.change_color_button2
        self.app.guess_button3_9['command'] = self.change_color_button3
        self.app.guess_button4_9['command'] = self.change_color_button4
        self.app.guess_button1_10['command'] = self.change_color_button1
        self.app.guess_button2_10['command'] = self.change_color_button2
        self.app.guess_button3_10['command'] = self.change_color_button3
        self.app.guess_button4_10['command'] = self.change_color_button4
        self.app.try_button['command'] = self.try_command
    def resulte_of_try(self):
        while len(self.resulte_list) < 4:
            self.resulte_list.append('#ffbf80')


    def what_resulte_label_11(self):
        if self.try_level == 1:
            return self.app.resulte_label_1_11
        elif self.try_level == 2:
            return self.app.resulte_label_2_11
        elif self.try_level == 3:
            return self.app.resulte_label_3_11
        elif self.try_level == 4:
            return self.app.resulte_label_4_11
        elif self.try_level == 5:
            return self.app.resulte_label_5_11
        elif self.try_level == 6:
            return self.app.resulte_label_6_11
        elif self.try_level == 7:
            return self.app.resulte_label_7_11
        elif self.try_level == 8:
            return self.app.resulte_label_8_11
        elif self.try_level == 9:
            return self.app.resulte_label_9_11
        elif self.try_level == 10:
            return self.app.resulte_label_10_11
    def what_resulte_label_12(self):
        if self.try_level == 1:
            return self.app.resulte_label_1_12
        elif self.try_level == 2:
            return self.app.resulte_label_2_12
        elif self.try_level == 3:
            return self.app.resulte_label_3_12
        elif self.try_level == 4:
            return self.app.resulte_label_4_12
        elif self.try_level == 5:
            return self.app.resulte_label_5_12
        elif self.try_level == 6:
            return self.app.resulte_label_6_12
        elif self.try_level == 7:
            return self.app.resulte_label_7_12
        elif self.try_level == 8:
            return self.app.resulte_label_8_12
        elif self.try_level == 9:
            return self.app.resulte_label_9_12
        elif self.try_level == 10:
            return self.app.resulte_label_10_12
    def what_resulte_label_21(self):
        if self.try_level == 1:
            return self.app.resulte_label_1_21
        elif self.try_level == 2:
            return self.app.resulte_label_2_21
        elif self.try_level == 3:
            return self.app.resulte_label_3_21
        elif self.try_level == 4:
            return self.app.resulte_label_4_21
        elif self.try_level == 5:
            return self.app.resulte_label_5_21
        elif self.try_level == 6:
            return self.app.resulte_label_6_21
        elif self.try_level == 7:
            return self.app.resulte_label_7_21
        elif self.try_level == 8:
            return self.app.resulte_label_8_21
        elif self.try_level == 9:
            return self.app.resulte_label_9_21
        elif self.try_level == 10:
            return self.app.resulte_label_10_21
    def what_resulte_label_22(self):
        if self.try_level == 1:
            return self.app.resulte_label_1_22
        elif self.try_level == 2:
            return self.app.resulte_label_2_22
        elif self.try_level == 3:
            return self.app.resulte_label_3_22
        elif self.try_level == 4:
            return self.app.resulte_label_4_22
        elif self.try_level == 5:
            return self.app.resulte_label_5_22
        elif self.try_level == 6:
            return self.app.resulte_label_6_22
        elif self.try_level == 7:
            return self.app.resulte_label_7_22
        elif self.try_level == 8:
            return self.app.resulte_label_8_22
        elif self.try_level == 9:
            return self.app.resulte_label_9_22
        elif self.try_level == 10:
            return self.app.resulte_label_10_22
    def do_resulte(self):
        self.what_resulte_label_11()['bg'] = self.resulte_list[0]
        self.what_resulte_label_12()['bg'] = self.resulte_list[1]
        self.what_resulte_label_21()['bg'] = self.resulte_list[2]
        self.what_resulte_label_22()['bg'] = self.resulte_list[3]
    def change_states(self):
        if self.try_level == 2:
            self.app.guess_button1_1['state'] = 'disabled'
            self.app.guess_button2_1['state'] = 'disabled'
            self.app.guess_button3_1['state'] = 'disabled'
            self.app.guess_button4_1['state'] = 'disabled'
            self.app.guess_button1_2['state'] = 'normal'
            self.app.guess_button2_2['state'] = 'normal'
            self.app.guess_button3_2['state'] = 'normal'
            self.app.guess_button4_2['state'] = 'normal'
        elif self.try_level == 3:
            self.app.guess_button1_2['state'] = 'disabled'
            self.app.guess_button2_2['state'] = 'disabled'
            self.app.guess_button3_2['state'] = 'disabled'
            self.app.guess_button4_2['state'] = 'disabled'
            self.app.guess_button1_3['state'] = 'normal'
            self.app.guess_button2_3['state'] = 'normal'
            self.app.guess_button3_3['state'] = 'normal'
            self.app.guess_button4_3['state'] = 'normal'
        elif self.try_level == 4:
            self.app.guess_button1_3['state'] = 'disabled'
            self.app.guess_button2_3['state'] = 'disabled'
            self.app.guess_button3_3['state'] = 'disabled'
            self.app.guess_button4_3['state'] = 'disabled'
            self.app.guess_button1_4['state'] = 'normal'
            self.app.guess_button2_4['state'] = 'normal'
            self.app.guess_button3_4['state'] = 'normal'
            self.app.guess_button4_4['state'] = 'normal'
        elif self.try_level == 5:
            self.app.guess_button1_4['state'] = 'disabled'
            self.app.guess_button2_4['state'] = 'disabled'
            self.app.guess_button3_4['state'] = 'disabled'
            self.app.guess_button4_4['state'] = 'disabled'
            self.app.guess_button1_5['state'] = 'normal'
            self.app.guess_button2_5['state'] = 'normal'
            self.app.guess_button3_5['state'] = 'normal'
            self.app.guess_button4_5['state'] = 'normal'       
        elif self.try_level == 6:
            self.app.guess_button1_5['state'] = 'disabled'
            self.app.guess_button2_5['state'] = 'disabled'
            self.app.guess_button3_5['state'] = 'disabled'
            self.app.guess_button4_5['state'] = 'disabled'
            self.app.guess_button1_6['state'] = 'normal'
            self.app.guess_button2_6['state'] = 'normal'
            self.app.guess_button3_6['state'] = 'normal'
            self.app.guess_button4_6['state'] = 'normal'       
        elif self.try_level == 7:
            self.app.guess_button1_6['state'] = 'disabled'
            self.app.guess_button2_6['state'] = 'disabled'
            self.app.guess_button3_6['state'] = 'disabled'
            self.app.guess_button4_6['state'] = 'disabled'
            self.app.guess_button1_7['state'] = 'normal'
            self.app.guess_button2_7['state'] = 'normal'
            self.app.guess_button3_7['state'] = 'normal'
            self.app.guess_button4_7['state'] = 'normal'       
        elif self.try_level == 8:
            self.app.guess_button1_7['state'] = 'disabled'
            self.app.guess_button2_7['state'] = 'disabled'
            self.app.guess_button3_7['state'] = 'disabled'
            self.app.guess_button4_7['state'] = 'disabled'
            self.app.guess_button1_8['state'] = 'normal'
            self.app.guess_button2_8['state'] = 'normal'
            self.app.guess_button3_8['state'] = 'normal'
            self.app.guess_button4_8['state'] = 'normal'       
        elif self.try_level == 9:
            self.app.guess_button1_8['state'] = 'disabled'
            self.app.guess_button2_8['state'] = 'disabled'
            self.app.guess_button3_8['state'] = 'disabled'
            self.app.guess_button4_8['state'] = 'disabled'
            self.app.guess_button1_9['state'] = 'normal'
            self.app.guess_button2_9['state'] = 'normal'
            self.app.guess_button3_9['state'] = 'normal'
            self.app.guess_button4_9['state'] = 'normal'       
        elif self.try_level == 10:
            self.app.guess_button1_9['state'] = 'disabled'
            self.app.guess_button2_9['state'] = 'disabled'
            self.app.guess_button3_9['state'] = 'disabled'
            self.app.guess_button4_9['state'] = 'disabled'
            self.app.guess_button1_10['state'] = 'normal'
            self.app.guess_button2_10['state'] = 'normal'
            self.app.guess_button3_10['state'] = 'normal'
            self.app.guess_button4_10['state'] = 'normal'       
    def lose_or_win(self):
        if self.resulte_list.count('#000000') == 4:
            self.gui_events.winner()
            # restart the game
            self.try_level = 1
            self.game_begin.__init__(self.random, self.app)
            self.__init__(self.app, self.gui_events, self.game_begin, self.random)
            return
        elif self.try_level == 11:
            self.gui_events.loser()
            self.game_begin.__init__(self.random, self.app)
            self.__init__(self.app, self.gui_events, self.game_begin, self.random)
            return

    def try_command(self):
        self.black_and_white()
        self.resulte_of_try()
        self.do_resulte()
        self.try_level += 1
        self.lose_or_win()
        self.change_states()
        self.button1_color = 'white'
        self.button2_color = 'white'
        self.button3_color = 'white'
        self.button4_color = 'white'
        self.button1_color_number = 4
        self.button2_color_number = 4
        self.button3_color_number = 4
        self.button4_color_number = 4
        self.correct_respond = [self.real_color1, self.real_color2, self.real_color3, self.real_color4]
def main():
    import tkinter as tk
    from tkinter import messagebox as msbox
    import GUI.gui as app_gui
    import random
    
    app = app_gui.app(tk)

    start = game_begin(random, app)
    gui_events = app_gui.gui_events(app, msbox)
    Game_events = game_events(app, gui_events, start, random)
    app.surface.mainloop()
if __name__ == '__main__':main()