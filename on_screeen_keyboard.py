from tkinter import *
import tkinter.scrolledtext as scrolledtext
''' my name is yogesh singh , bca 2nd year student ,,, if you like this project then please follow me on github
and , comment your feed back also ///'''

root = Tk()
root.title("On Screen Keyboard")
root.resizable(0,0)

def select(value):
	if value=="<-":
		txt = text.get(1.0,END)
		val = len(txt)
		text.delete(1.0,END)
		text.insert(1.0,txt[:val-2])
	elif value=="Space":
		text.insert(END," ")
	elif value == "Tab":
		text.insert(END,"	")
	else:
		text.insert(END,value)

# Root Widgets......
text = scrolledtext.ScrolledText(root,width=120,height=5,wrap=WORD,padx=10,pady=10,borderwidth=5,relief=RIDGE)
text.grid(row=1,columnspan=16)

buttons = ['q','w','e','r','t','y','u','i','o','p','<-','7','8','9','-'
,'a','s','d','f','g','h','j','k','l','[',']','4','5','6','+'
,'z','x','c','v','b','n','m',',','.','Tab','0','1','2','3','/',
'Space']
varrow = 2
varcolumn = 0

for button in buttons:
	command = lambda x=button:select(x)
	if button !='Space':
		Button(root,text=button,width=5,bg='black',fg='white',activebackground="white",activeforeground='black',
			relief='raised',padx=8,pady=4,bd=6,command=command).grid(row=varrow,column=varcolumn)
	if button =='Space':
		Button(root,text=button,width=5,bg='black',fg='white',activebackground="white",activeforeground='black',
			relief='raised',padx=180,pady=4,bd=6,command=command).grid(row=6,columnspan=16)

	varcolumn+=1
	if varcolumn > 14 and varrow==2:
		varcolumn=0
		varrow+=1
	if varcolumn > 14 and varrow ==3:
		varcolumn=0
		varrow+=1

root.mainloop()