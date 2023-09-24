from tkinter import *
root= Tk()
root.title("Heart_Diagnose_Report")
root.geometry('600x600')
root.configure(background="salmon")

question1_radioButton = StringVar(value="0")

Question1 = Label(root, text="Do you experience shortness of breath during routine activities?", bg="salmon", fg="white")
Question1.place(relx=0.5, rely=0.2, anchor=CENTER)
question1_r1 = RadioButton(root,text="yes", variable=question1_radioButton, value="yes", bg="salmon")
question1_r1.place(relx=0.5, rely=0.25, anchor=CENTER)
question2_r2 = RadioButton(root,text="no", variable=question1_radioButton, value="no", bg="salmon")
question2_r2.place(relx=0.5, rely=0.25, anchor=CENTER)

question2_radioButton =StringVar(value="0")
Question2 = Label(root, text="Do you have swelling in the foot/ankles/legs (shoes feel tighter) or abdomen?", bg="salmon", fg="white")
Question2.place(relx=0.5, rely=0.2, anchor=CENTER)
question1_r1 = RadioButton(root,text="yes", variable=question1_radioButton, value="yes", bg="salmon")
question1_r1.place(relx=0.5, rely=0.25, anchor=CENTER)
question2_r2 = RadioButton(root,text="no", variable=question1_radioButton, value="no", bg="salmon")
question2_r2.place(relx=0.5, rely=0.25, anchor=CENTER)

question3_radioButton =StringVar(value="0")
Question3 = Label(root, text="De you feel any of these symptoms - confusion, disorientation or loss of memory?", bg="salmon", fg="white")
Question3.place(relx=0.5, rely=0.2, anchor=CENTER)
question1_r1 = RadioButton(root,text="yes", variable=question1_radioButton, value="yes", bg="salmon")
question1_r1.place(relx=0.5, rely=0.25, anchor=CENTER)
question2_r2 = RadioButton(root,text="no", variable=question1_radioButton, value="no", bg="salmon")
question2_r2.place(relx=0.5, rely=0.25, anchor=CENTER)

question4_radioButton =StringVar(value="0")
Question4 = Label(root, text="Do you experience shortness of breath while at rest/lying down?", bg="salmon", fg="white")
Question4.place(relx=0.5, rely=0.2, anchor=CENTER)
question1_r1 = RadioButton(root,text="yes", variable=question1_radioButton, value="yes", bg="salmon")
question1_r1.place(relx=0.5, rely=0.25, anchor=CENTER)
question2_r2 = RadioButton(root,text="no", variable=question1_radioButton, value="no", bg="salmon")
question2_r2.place(relx=0.5, rely=0.25, anchor=CENTER)

question5_radioButton =StringVar(value="0")
Question5 = Label(root, text="Do you experience persistent wheezing/ coughing that produces white or pink blood tinged mucus?", bg="salmon", fg="white")
Question5.place(relx=0.5, rely=0.2, anchor=CENTER)
question1_r1 = RadioButton(root,text="yes", variable=question1_radioButton, value="yes", bg="salmon")
question1_r1.place(relx=0.5, rely=0.25, anchor=CENTER)
question2_r2 = RadioButton(root,text="no", variable=question1_radioButton, value="no", bg="salmon")
question2_r2.place(relx=0.5, rely=0.25, anchor=CENTER)

def heart_diagnostic_score():
	score= 0 
	if question1_radioButton.get() == "yes":
		score = score + 10
		print(score)
	if question2_radioButton.get() == "yes":
		score = score +10
		print(score)
	if question3_radioButton.get() == "yes":
		score = score + 10
		print(score)
	if question4_radioButton.get() == "yes":
		score = score +10
		print(score)
	if question5_radioButton.get() == "yes":
		score = score +10
		print(score)

	if score <= 10:
		messagebox.showinfo("Report", "You don't need to visit a doctor.")
	elif score > 10 and score<= 30:
		messagebox.showinfo("Report", "You might perhaps have to visit a doctor")
	else: 
		messagebox.showinfo("Report", "I strongly advice you to visit a doctor")

btn = Button(root, text="click me", command=heart_diagnostic_score)
btn.place(relx=0.5, rely=0.95, anchor=CENTER)

root.mainloop()