import tkinter as tk
import admission as adm
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry('1200x800')
window.resizable(height=False, width=False)
window.title("University Probability Predictor")

# Colours
COLOUR1 = "#9500ff"
COLOUR2 = "#4dc6ff"

# Creating the frames
frame1 = tk.Frame(window, width=500, height=800, bg=COLOUR1, highlightbackground="black", highlightthickness=10)
frame2 = tk.Frame(window, width=700, height=110, bg=COLOUR2, highlightbackground="black", highlightthickness=10)
frame3 = tk.Frame(window, width=700, height=690, bg="#f6c2ff", highlightbackground="black", highlightthickness=10)

# Placing the frames
frame1.grid(row=0, column=0, rowspan=2)
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=1)
frame1.grid_propagate(False)
frame2.grid_propagate(False)
frame3.grid_propagate(False)

# Adding Labels
firstName_var = tk.StringVar()
firstName = tk.Label(frame1, text="First Name : ", font=('calibre', 15, 'bold'), bg=COLOUR1)
firstName.grid(row=0, column=0, padx=25, pady=20)
firstName_entry = tk.Entry(frame1, textvariable=firstName_var, font=('calibre', 15, 'normal'))
firstName_entry.grid(row=0, column=1, padx=7, pady=20)

lastName_var = tk.StringVar()
lastName = tk.Label(frame1, text="Last Name : ", font=('calibre', 15, 'bold'), bg=COLOUR1)
lastName.grid(row=1, column=0, padx=25, pady=20)
lastName_entry = tk.Entry(frame1, textvariable=lastName_var, font=('calibre', 15, 'normal'))
lastName_entry.grid(row=1, column=1, padx=7, pady=20)

greScore_var = tk.IntVar()
greScore = tk.Label(frame1, text="GRE SCORE : ", font=('calibre', 15, 'bold'), bg=COLOUR1)
greScore.grid(row=2, column=0, padx=25, pady=20)
greScore_entry = tk.Entry(frame1, textvariable=greScore_var, font=('calibre', 15, 'normal'))
greScore_entry.grid(row=2, column=1, padx=7, pady=20)

toeflScore_var = tk.IntVar()
toeflScore = tk.Label(frame1, text="TOEFL Score : ", font=('calibre', 15, 'bold'), bg=COLOUR1)
toeflScore.grid(row=3, column=0, padx=25, pady=20)
toeflScore_entry = tk.Entry(frame1, textvariable=toeflScore_var, font=('calibre', 15, 'normal'))
toeflScore_entry.grid(row=3, column=1, padx=7, pady=20)

uniRating_var = tk.IntVar()
uniRating = tk.Label(frame1, text="University Rating : ", font=('calibre', 15, 'bold'), bg=COLOUR1)
uniRating.grid(row=4, column=0, padx=25, pady=20)
uniRating_entry = tk.Entry(frame1, textvariable=uniRating_var, font=('calibre', 15, 'normal'))
uniRating_entry.grid(row=4, column=1, padx=7, pady=20)

cgpa_var = tk.IntVar()
cgpa = tk.Label(frame1, text="CGPA : ", font=('calibre', 15, 'bold'), bg=COLOUR1)
cgpa.grid(row=5, column=0, padx=25, pady=20)
cgpa_entry = tk.Entry(frame1, textvariable=cgpa_var, font=('calibre', 15, 'normal'))
cgpa_entry.grid(row=5, column=1, padx=7, pady=20)

sop_var = tk.IntVar()
sop = tk.Label(frame1, text="SOP Rating : ", font=('calibre', 15, 'bold'), bg=COLOUR1)
sop.grid(row=6, column=0, padx=25, pady=20)
sop_entry = tk.Entry(frame1, textvariable=sop_var, font=('calibre', 15, 'normal'))
sop_entry.grid(row=6, column=1, padx=7, pady=20)

lor_var = tk.IntVar()
lor = tk.Label(frame1, text="LOR Rating : ", font=('calibre', 15, 'bold'), bg=COLOUR1)
lor.grid(row=7, column=0, padx=25, pady=20)
lor_entry = tk.Entry(frame1, textvariable=lor_var, font=('calibre', 15, 'normal'))
lor_entry.grid(row=7, column=1, padx=7, pady=20)

research_var = tk.IntVar()
research = tk.Label(frame1, text="Research : ", font=('calibre', 15, 'bold'), bg=COLOUR1)
research.grid(row=8, column=0, padx=25, pady=20)
research_entry = tk.Entry(frame1, textvariable=research_var, font=('calibre', 15, 'normal'))
research_entry.grid(row=8, column=1, padx=7, pady=20)

l1 = tk.Label(frame2, text="The chances of you getting this university is : ", font=('calibre', 15, 'bold'),
              bg=COLOUR2)
l1.grid(row=0, column=0, padx=15, pady=10)


def getInfo():
    gre = float(greScore_entry.get())
    toefl = float(toeflScore_entry.get())
    uRating = float(uniRating_entry.get())
    cg = float(cgpa_entry.get())
    sp = float(sop_entry.get())
    lr = float(lor_entry.get())
    rsh = float(research_entry.get())
    percent = round(adm.model.predict([[gre, toefl, uRating, sp, lr, cg, rsh]])[0] * 100, 3)
    p = percent
    if percent < 0:
        percent = 0
    elif percent > 100:
        percent = 100
    percent = str(percent) + "%"
    l2 = tk.Label(frame2, text=percent, font=('calibre', 15, 'bold'), bg=COLOUR2)
    l2.grid(row=0, column=1, padx=15, pady=10)
    return p

b1 = tk.Button(frame2, text="Update", command=getInfo, font=('calibre', 10, 'bold'))
b1.grid(column=0, row=2)

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def plot():
    fig = Figure(figsize=(6.8, 6.7))
    if clicked.get() != "SELECT OPTIONS":
        pass
    LabelClicked = clicked.get()
    if LabelClicked == "GRE - University Rating":
        x = adm.df_copy["GRE"].loc[(adm.df_copy['University Rating'] == float(uniRating_entry.get()))]
        y = adm.df_copy["Probability"].loc[(adm.df_copy['University Rating'] == float(uniRating_entry.get()))] * 100
        plot1 = fig.add_subplot(111)
        plot1.scatter(x, y)
        plot1.text(int(greScore_entry.get()),getInfo(),str("YOU"))
        plot1.set_facecolor('#00ff7b')
        plot1.set_xlabel("GRE Scores")
        plot1.set_ylabel("Probability(in %)")
        plot1.set_title('Probability Distribution')
    elif LabelClicked == "TOEFL - University Rating":
        x = adm.df_copy["TOEFL"].loc[(adm.df_copy['University Rating'] == float(uniRating_entry.get()))]
        y = adm.df_copy["Probability"].loc[(adm.df_copy['University Rating'] == float(uniRating_entry.get()))] * 100
        plot1 = fig.add_subplot(111)
        plot1.scatter(x, y)
        plot1.text(int(toeflScore_entry.get()), getInfo(), str("YOU"))
        plot1.set_facecolor('#00ff7b')
        plot1.set_xlabel("TOEFL Scores")
        plot1.set_ylabel("Probability(in %)")
        plot1.set_title('Probability Distribution')
    elif LabelClicked == "CGPA":
        x = adm.df_copy["CGPA"]
        y = adm.df_copy["Probability"] * 100
        plot1 = fig.add_subplot(111)
        plot1.scatter(x, y)
        plot1.text(float(cgpa_entry.get()), getInfo(), str("YOU"))
        plot1.set_facecolor('#00ff7b')
        plot1.set_xlabel("CGPA")
        plot1.set_ylabel("Probability(in %)")
        plot1.set_title('Probability Distribution')
    canvas = FigureCanvasTkAgg(fig, frame3)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=1)
    # canvas.get_tk_widget().grid(row=1, column=1)


options = [
    "GRE - University Rating",
    "TOEFL - University Rating",
    "CGPA",
]
clicked = tk.StringVar()
clicked.set("SELECT OPTIONS")
menu = tk.OptionMenu(frame1, clicked, *options)
menu.config(font=('calibre', 10, 'bold'))
menu.grid(row=9, column=0, padx=7, pady=20)

plotButton = tk.Button(frame1, text="Plot", command=plot, font=('calibre', 10, 'bold'))
plotButton.grid(row=9, column=1, padx=7, pady=20)

#image
img = Image.open("logo.png")
img = img.resize((70,70))
test = ImageTk.PhotoImage(img)
labelImage = tk.Label(frame1,image = test,bg = COLOUR1)
labelImage.grid(row=10,column=0)

labelText = tk.Label(frame1,text="University\nProbability\nPredictor",bg = COLOUR1, font=('calibre', 15, 'bold'))
labelText.grid(row=10,column=1)


window.mainloop()
