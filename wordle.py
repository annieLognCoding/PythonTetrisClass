#wordle
from tkinter import *
import tkinter.messagebox as msgbox
import random
def fill_word():
    global counter
    if len(entry.get()) != 5:
        return
    elif counter < len(ltrs):
        d = dict()
        d.update(word_dict)
        word = entry.get()
        cl = list()
        for i,lbl in enumerate(ltrs[counter]):
            if word[i] == answer[i]: #and d[word[i]] > 0:
                lbl.config(text = word[i].upper(), bg= "light green") 
                cl.append(i)
                d[word[i]] -= 1
            else:
                lbl.config(text = word[i].upper(), bg= "dark grey")
                
        for i,lbl in enumerate(ltrs[counter]):
            if word[i] in answer and d[word[i]] > 0:
                lbl.config(text = word[i].upper(), bg= "light yellow")
                d[word[i]] -= 1
            elif i not in cl:
                lbl.config(text = word[i].upper(), bg= "dark grey") 
              
        counter += 1
        
        if entry.get() == answer:
            if msgbox.askyesno(message="you won! continue?"):
                btn.config(text = "replay", command= reset)
            else:
                root.destroy()
        elif counter == len(ltrs):
            msgbox.showinfo(message="The answer was "+ answer)
            btn.config(text = "replay", command= reset)
            

def setup(answers):
    
    answer = random.choice(answers)
    word_dict = dict()
    for i in answer:
        if i in word_dict.keys():
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    return answer, word_dict
        

def reset():
    global counter
    counter = 0
    global answer
    answer = random.choice(answers)
    global word_dict
    word_dict = dict()
    for i in answer:
        if i in word_dict.keys():
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    for option in ltrs:
        for label in option:
            label.config(bg = "light grey", text = "")
    btn.config(text = "submit", command = fill_word)

root = Tk()
root.title("Wordle")
root. geometry("600x800")
word_frame = Frame(root)
word_frame.pack()


ltrs = list()

#first Labels
ltrs1 = list()
lbl1_1 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl1_1.grid(row =0, column = 0)
lbl1_2 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl1_2.grid(row =0, column = 1)
lbl1_3 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl1_3.grid(row =0, column = 2)
lbl1_4 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl1_4.grid(row =0, column = 3)
lbl1_5 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl1_5.grid(row =0, column = 4)
ltrs1.append(lbl1_1)
ltrs1.append(lbl1_2)
ltrs1.append(lbl1_3)
ltrs1.append(lbl1_4)
ltrs1.append(lbl1_5)
ltrs.append(ltrs1)



#second Labels
ltrs2 = list()
lbl2_1 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl2_1.grid(row =1, column = 0)
lbl2_2 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl2_2.grid(row =1, column = 1)
lbl2_3 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl2_3.grid(row =1, column = 2)
lbl2_4 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl2_4.grid(row =1, column = 3)
lbl2_5 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl2_5.grid(row =1, column = 4)
ltrs2.append(lbl2_1)
ltrs2.append(lbl2_2)
ltrs2.append(lbl2_3)
ltrs2.append(lbl2_4)
ltrs2.append(lbl2_5)
ltrs.append(ltrs2)


#third Labels
ltrs3 = list()
lbl3_1 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl3_1.grid(row =2, column = 0)
lbl3_2 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl3_2.grid(row =2, column = 1)
lbl3_3 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl3_3.grid(row =2, column = 2)
lbl3_4 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl3_4.grid(row =2, column = 3)
lbl3_5 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl3_5.grid(row =2, column = 4)
ltrs3.append(lbl3_1)
ltrs3.append(lbl3_2)
ltrs3.append(lbl3_3)
ltrs3.append(lbl3_4)
ltrs3.append(lbl3_5)
ltrs.append(ltrs3)


#forth Labels
ltrs4 = list()
lbl4_1 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl4_1.grid(row =3, column = 0)
lbl4_2 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl4_2.grid(row =3, column = 1)
lbl4_3 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl4_3.grid(row =3, column = 2)
lbl4_4 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl4_4.grid(row =3, column = 3)
lbl4_5 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl4_5.grid(row =3, column = 4)
ltrs4.append(lbl4_1)
ltrs4.append(lbl4_2)
ltrs4.append(lbl4_3)
ltrs4.append(lbl4_4)
ltrs4.append(lbl4_5)
ltrs.append(ltrs4)


#fifth Labels
ltrs5=list()
lbl5_1 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl5_1.grid(row =4, column = 0)
lbl5_2 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl5_2.grid(row =4, column = 1)
lbl5_3 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl5_3.grid(row =4, column = 2)
lbl5_4 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl5_4.grid(row =4, column = 3)
lbl5_5 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl5_5.grid(row =4, column = 4)
ltrs5.append(lbl5_1)
ltrs5.append(lbl5_2)
ltrs5.append(lbl5_3)
ltrs5.append(lbl5_4)
ltrs5.append(lbl5_5)
ltrs.append(ltrs5)


#sixth Labels
ltrs6 = list()
lbl6_1 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl6_1.grid(row =5, column = 0)
lbl6_2 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl6_2.grid(row =5, column = 1)
lbl6_3 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl6_3.grid(row =5, column = 2)
lbl6_4 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl6_4.grid(row =5, column = 3)
lbl6_5 = Label(word_frame, relief="ridge", font = "Times 60", width = 2, height = 1, text = "", bg = "light gray")
lbl6_5.grid(row =5, column = 4)
ltrs6.append(lbl6_1)
ltrs6.append(lbl6_2)
ltrs6.append(lbl6_3)
ltrs6.append(lbl6_4)
ltrs6.append(lbl6_5)
ltrs.append(ltrs6)


ui_frame = Frame(root)
ui_frame.pack()

counter = 0

with open("words.txt")as f:
    answers = [i for i in f. read().split() if len(i) == 5 and '\'' not in i]
answer, word_dict = setup(answers)


entry = Entry(ui_frame)
btn = Button(ui_frame, text = "submit", command = fill_word)
entry.pack()
btn.pack()

root.mainloop()