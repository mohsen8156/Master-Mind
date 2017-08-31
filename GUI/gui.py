class app:
    def __init__(self, tk):
        self.tk = tk # to use tk in calss
        self.build_surface()
    def build_surface(self):
        self.surface = self.tk.Tk()
        # set the min size and max size
        self.surface.minsize(width=402, height=800)
        self.surface.maxsize(width=402, height=800)
        self.surface.title('Good Think')
        self.surface.tk_setPalette(background='#ffbf80', foreground='black',activeBackground='#ffbf80')




    def build_1st_row(self):
        self.try_button = self.tk.Button(self.surface, bg='#ffbf80', width=10, height=4, relief='flat', text='try the anserw') # 1. set the command to try anserw  2. set the w/
        self.real_label1 = self.tk.Label(self.surface, bg='#c4ff4d', bitmap='question', width=75, height=75) # 1. set the color with random in main.py 2. set the w/h
        self.real_label2 = self.tk.Label(self.surface, bg='#c4ff4d', bitmap='question', width=75, height=75) # 1. set the color with random in main.py 2. set the w/h
        self.real_label3 = self.tk.Label(self.surface, bg='#c4ff4d', bitmap='question', width=75, height=75) # 1. set the color with random in main.py 2. set the w/h
        self.real_label4 = self.tk.Label(self.surface, bg='#c4ff4d', bitmap='question', width=75, height=75) # 1. set the color with random in main.py 2. set the w/h
        # make a var : real color 1,2,3,4
        self.try_button.grid(row=1, column=1)
        self.real_label1.grid(row=1, column=2)
        self.real_label2.grid(row=1, column=3)
        self.real_label3.grid(row=1, column=4)
        self.real_label4.grid(row=1, column=5)
        self.build_other_rows()
    def build_other_rows(self):
    	# ---------------------
    	# 10th guess row
        self.resulte_frame10 = self.tk.Frame(self.surface, bg='#ffffff', width=11) # 1. being a frame for show resultes 2. set the w/h
        self.guess_button1_10 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button2_10 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button3_10 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button4_10 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.resulte_label_10_11 = self.tk.Label(self.resulte_frame10, bg='#e67300', width=5, height=2)# set w/h
        self.resulte_label_10_12 = self.tk.Label(self.resulte_frame10, bg='#b300b3', width=5, height=2)
        self.resulte_label_10_21 = self.tk.Label(self.resulte_frame10, bg='#b300b3', width=5, height=2)
        self.resulte_label_10_22 = self.tk.Label(self.resulte_frame10, bg='#e67300', width=5, height=2)
        self.resulte_frame9 = self.tk.Frame(self.surface, bg='#ffffff', width=11) # 1. being a frame for show resultes 2. set the w/h
        self.guess_button1_9 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button2_9 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button3_9 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button4_9 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.resulte_label_9_11 = self.tk.Label(self.resulte_frame9, bg='#e67300', width=5, height=2)# set w/h
        self.resulte_label_9_12 = self.tk.Label(self.resulte_frame9, bg='#b300b3', width=5, height=2)
        self.resulte_label_9_21 = self.tk.Label(self.resulte_frame9, bg='#b300b3', width=5, height=2)
        self.resulte_label_9_22 = self.tk.Label(self.resulte_frame9, bg='#e67300', width=5, height=2)
        self.resulte_frame8 = self.tk.Frame(self.surface, bg='#ffffff', width=11) # 1. being a frame for show resultes 2. set the w/h
        self.guess_button1_8 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button2_8 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button3_8 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button4_8 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.resulte_label_8_11 = self.tk.Label(self.resulte_frame8, bg='#e67300', width=5, height=2)# set w/h
        self.resulte_label_8_12 = self.tk.Label(self.resulte_frame8, bg='#b300b3', width=5, height=2)
        self.resulte_label_8_21 = self.tk.Label(self.resulte_frame8, bg='#b300b3', width=5, height=2)
        self.resulte_label_8_22 = self.tk.Label(self.resulte_frame8, bg='#e67300', width=5, height=2)
        self.resulte_frame7 = self.tk.Frame(self.surface, bg='#ffffff', width=11) # 1. being a frame for show resultes 2. set the w/h
        self.guess_button1_7 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button2_7 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button3_7 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button4_7 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.resulte_label_7_11 = self.tk.Label(self.resulte_frame7, bg='#e67300', width=5, height=2)# set w/h
        self.resulte_label_7_12 = self.tk.Label(self.resulte_frame7, bg='#b300b3', width=5, height=2)
        self.resulte_label_7_21 = self.tk.Label(self.resulte_frame7, bg='#b300b3', width=5, height=2)
        self.resulte_label_7_22 = self.tk.Label(self.resulte_frame7, bg='#e67300', width=5, height=2)
        self.resulte_frame6 = self.tk.Frame(self.surface, bg='#ffffff', width=11) # 1. being a frame for show resultes 2. set the w/h
        self.guess_button1_6 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button2_6 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button3_6 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button4_6 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.resulte_label_6_11 = self.tk.Label(self.resulte_frame6, bg='#e67300', width=5, height=2)# set w/h
        self.resulte_label_6_12 = self.tk.Label(self.resulte_frame6, bg='#b300b3', width=5, height=2)
        self.resulte_label_6_21 = self.tk.Label(self.resulte_frame6, bg='#b300b3', width=5, height=2)
        self.resulte_label_6_22 = self.tk.Label(self.resulte_frame6, bg='#e67300', width=5, height=2)
        self.resulte_frame5 = self.tk.Frame(self.surface, bg='#ffffff', width=11) # 1. being a frame for show resultes 2. set the w/h
        self.guess_button1_5 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button2_5 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button3_5 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button4_5 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.resulte_label_5_11 = self.tk.Label(self.resulte_frame5, bg='#e67300', width=5, height=2)# 1. set w/h 2. can be arc
        self.resulte_label_5_12 = self.tk.Label(self.resulte_frame5, bg='#b300b3', width=5, height=2)
        self.resulte_label_5_21 = self.tk.Label(self.resulte_frame5, bg='#b300b3', width=5, height=2)
        self.resulte_label_5_22 = self.tk.Label(self.resulte_frame5, bg='#e67300', width=5, height=2)
        self.resulte_frame4 = self.tk.Frame(self.surface, bg='#ffffff', width=11) # 1. being a frame for show resultes 2. set the w/h
        self.guess_button1_4 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button2_4 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button3_4 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button4_4 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.resulte_label_4_11 = self.tk.Label(self.resulte_frame4, bg='#e67300', width=5, height=2)# set w/h
        self.resulte_label_4_12 = self.tk.Label(self.resulte_frame4, bg='#b300b3', width=5, height=2)
        self.resulte_label_4_21 = self.tk.Label(self.resulte_frame4, bg='#b300b3', width=5, height=2)
        self.resulte_label_4_22 = self.tk.Label(self.resulte_frame4, bg='#e67300', width=5, height=2)
        self.resulte_frame3 = self.tk.Frame(self.surface, bg='#ffffff', width=11) # 1. being a frame for show resultes 2. set the w/h
        self.guess_button1_3 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button2_3 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button3_3 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button4_3 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.resulte_label_3_11 = self.tk.Label(self.resulte_frame3, bg='#e67300', width=5, height=2)
        self.resulte_label_3_12 = self.tk.Label(self.resulte_frame3, bg='#b300b3', width=5, height=2)
        self.resulte_label_3_21 = self.tk.Label(self.resulte_frame3, bg='#b300b3', width=5, height=2)
        self.resulte_label_3_22 = self.tk.Label(self.resulte_frame3, bg='#e67300', width=5, height=2)
        self.resulte_frame2 = self.tk.Frame(self.surface, bg='#ffffff', width=11) # 1. being a frame for show resultes 2. set the w/h
        self.guess_button1_2 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button2_2 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button3_2 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button4_2 = self.tk.Button(self.surface, bg='#ffffff', state='disabled', width=10, height=4) # 1. command for change color 2. set the w/h
        self.resulte_label_2_11 = self.tk.Label(self.resulte_frame2, bg='#e67300', width=5, height=2)# set w/h
        self.resulte_label_2_12 = self.tk.Label(self.resulte_frame2, bg='#b300b3', width=5, height=2)
        self.resulte_label_2_21 = self.tk.Label(self.resulte_frame2, bg='#b300b3', width=5, height=2)
        self.resulte_label_2_22 = self.tk.Label(self.resulte_frame2, bg='#e67300', width=5, height=2)
        self.resulte_frame1 = self.tk.Frame(self.surface, bg='#ffffff', width=11) # 1. being a frame for show resultes 2. set the w/h
        self.guess_button1_1 = self.tk.Button(self.surface, bg='#ffffff', state='normal', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button2_1 = self.tk.Button(self.surface, bg='#ffffff', state='normal', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button3_1 = self.tk.Button(self.surface, bg='#ffffff', state='normal', width=10, height=4) # 1. command for change color 2. set the w/h
        self.guess_button4_1 = self.tk.Button(self.surface, bg='#ffffff', state='normal', width=10, height=4) # 1. command for change color 2. set the w/h
        self.resulte_label_1_11 = self.tk.Label(self.resulte_frame1, bg='#e67300', width=5, height=2)# set w/h
        self.resulte_label_1_12 = self.tk.Label(self.resulte_frame1, bg='#b300b3', width=5, height=2)
        self.resulte_label_1_21 = self.tk.Label(self.resulte_frame1, bg='#b300b3', width=5, height=2)
        self.resulte_label_1_22 = self.tk.Label(self.resulte_frame1, bg='#e67300', width=5, height=2)
        self.resulte_frame10.grid(row=2, column=1)
        self.guess_button1_10.grid(row=2, column=2)
        self.guess_button2_10.grid(row=2, column=3)
        self.guess_button3_10.grid(row=2, column=4)
        self.guess_button4_10.grid(row=2, column=5)
        self.resulte_label_10_11.grid(row=1, column=1)
        self.resulte_label_10_12.grid(row=1, column=2)
        self.resulte_label_10_21.grid(row=2, column=1)
        self.resulte_label_10_22.grid(row=2, column=2)
        # --------------------------------------------
        # 9th guess row

        self.resulte_frame9.grid(row=3, column=1)
        self.guess_button1_9.grid(row=3, column=2)
        self.guess_button2_9.grid(row=3, column=3)
        self.guess_button3_9.grid(row=3, column=4)
        self.guess_button4_9.grid(row=3, column=5)
        self.resulte_label_9_11.grid(row=1, column=1)
        self.resulte_label_9_12.grid(row=1, column=2)
        self.resulte_label_9_21.grid(row=2, column=1)
        self.resulte_label_9_22.grid(row=2, column=2)
        # --------------------------------------------
        # 8th guess row

        self.resulte_frame8.grid(row=4, column=1)
        self.guess_button1_8.grid(row=4, column=2)
        self.guess_button2_8.grid(row=4, column=3)
        self.guess_button3_8.grid(row=4, column=4)
        self.guess_button4_8.grid(row=4, column=5)
        self.resulte_label_8_11.grid(row=1, column=1)
        self.resulte_label_8_12.grid(row=1, column=2)
        self.resulte_label_8_21.grid(row=2, column=1)
        self.resulte_label_8_22.grid(row=2, column=2)
        # --------------------------------------------
        # 7th guess row

        self.resulte_frame7.grid(row=5, column=1)
        self.guess_button1_7.grid(row=5, column=2)
        self.guess_button2_7.grid(row=5, column=3)
        self.guess_button3_7.grid(row=5, column=4)
        self.guess_button4_7.grid(row=5, column=5)
        self.resulte_label_7_11.grid(row=1, column=1)
        self.resulte_label_7_12.grid(row=1, column=2)
        self.resulte_label_7_21.grid(row=2, column=1)
        self.resulte_label_7_22.grid(row=2, column=2)
        # --------------------------------------------
        # 6th guess row

        self.resulte_frame6.grid(row=6, column=1)
        self.guess_button1_6.grid(row=6, column=2)
        self.guess_button2_6.grid(row=6, column=3)
        self.guess_button3_6.grid(row=6, column=4)
        self.guess_button4_6.grid(row=6, column=5)
        self.resulte_label_6_11.grid(row=1, column=1)
        self.resulte_label_6_12.grid(row=1, column=2)
        self.resulte_label_6_21.grid(row=2, column=1)
        self.resulte_label_6_22.grid(row=2, column=2)
        # --------------------------------------------
        # 5th guess row

        self.resulte_frame5.grid(row=7, column=1)
        self.guess_button1_5.grid(row=7, column=2)
        self.guess_button2_5.grid(row=7, column=3)
        self.guess_button3_5.grid(row=7, column=4)
        self.guess_button4_5.grid(row=7, column=5)
        self.resulte_label_5_11.grid(row=1, column=1)
        self.resulte_label_5_12.grid(row=1, column=2)
        self.resulte_label_5_21.grid(row=2, column=1)
        self.resulte_label_5_22.grid(row=2, column=2)
        # --------------------------------------------
        # 4th guess row

        self.resulte_frame4.grid(row=8, column=1)
        self.guess_button1_4.grid(row=8, column=2)
        self.guess_button2_4.grid(row=8, column=3)
        self.guess_button3_4.grid(row=8, column=4)
        self.guess_button4_4.grid(row=8, column=5)
        self.resulte_label_4_11.grid(row=1, column=1)
        self.resulte_label_4_12.grid(row=1, column=2)
        self.resulte_label_4_21.grid(row=2, column=1)
        self.resulte_label_4_22.grid(row=2, column=2)
        # --------------------------------------------
        # 3rd guess row
        self.resulte_frame3.grid(row=9, column=1)
        self.guess_button1_3.grid(row=9, column=2)
        self.guess_button2_3.grid(row=9, column=3)
        self.guess_button3_3.grid(row=9, column=4)
        self.guess_button4_3.grid(row=9, column=5)
        self.resulte_label_3_11.grid(row=1, column=1)
        self.resulte_label_3_12.grid(row=1, column=2)
        self.resulte_label_3_21.grid(row=2, column=1)
        self.resulte_label_3_22.grid(row=2, column=2)
        # --------------------------------------------
        # 2nd guess row

        self.resulte_frame2.grid(row=10, column=1)
        self.guess_button1_2.grid(row=10, column=2)
        self.guess_button2_2.grid(row=10, column=3)
        self.guess_button3_2.grid(row=10, column=4)
        self.guess_button4_2.grid(row=10, column=5)
        self.resulte_label_2_11.grid(row=1, column=1)
        self.resulte_label_2_12.grid(row=1, column=2)
        self.resulte_label_2_21.grid(row=2, column=1)
        self.resulte_label_2_22.grid(row=2, column=2)
        # --------------------------------------------
        # 1st guess row

        self.resulte_frame1.grid(row=11, column=1)
        self.guess_button1_1.grid(row=11, column=2)
        self.guess_button2_1.grid(row=11, column=3)
        self.guess_button3_1.grid(row=11, column=4)
        self.guess_button4_1.grid(row=11, column=5)
        self.resulte_label_1_11.grid(row=1, column=1)
        self.resulte_label_1_12.grid(row=1, column=2)
        self.resulte_label_1_21.grid(row=2, column=1)
        self.resulte_label_1_22.grid(row=2, column=2)


    # make show for other frame
class gui_events:
    def __init__(self, app, msbox):
        self.app = app
        self.msbox = msbox
    def change_states(self, button1, button2, button3, button4): # execute when the try is clicked , used in part of a eunc in main.py
        button1['state'] = 'disabled' # these will be corrct
        button2['state'] = 'disabled'
        button3['state'] = 'disabled'
        button4['state'] = 'disabled'
    def change_to_white(self, button):
        button['bg'] = '#ffffff'
    def change_to_green(self, button):
        button['bg'] = '#33ff33'
    def change_to_blue(self, button):
        button['bg'] = '#00a3cc'
    def change_to_red(self, button):
        button['bg'] = '#ff3333'
    def change_to_yellow(self, button):
        button['bg'] = '#ffff33'
    def change_to_black(self, button):
        button['bg'] = '#000000'
    def winner(self):
        self.msbox.showinfo('winner!','you win!\ntry one more time!')
    def loser(self):
        self.msbox.showinfo('loser!',"you lose!\ndon't worry. you can try again!")