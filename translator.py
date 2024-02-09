from tkinter import*
#ttk is a module to styler tkinter widgets (like CSS), like making box, font, background color etc
from tkinter import ttk

from googletrans import Translator, LANGUAGES


root = Tk()
root.geometry("1050x320")

#Prevents resizing the box
root.resizable(0,0)


#This is for an icon on window, I need to add after 
#root.iconbitmap('')

#Background color
root["bg"] = 'skyblue'

#Window Name
root.title("Language Translator")

#Title on actual window
Label(root,text="Language Translator", font = "Arial 20 bold").pack()


#fg = text color, bg = background color
Label(root,text="Enter Text: ", font = "arial 13 bold", fg= "white", bg = "black").place(x=165, y= 90)


#Input box, for user to enter text for translation
input_original_text = Entry(root, width = "40")
input_original_text.place(x=30,y=130,height=100 )
input_original_text.get()


#output label
Label(root, text = "Translated Text", font = "arial 13 bold", fg= "white", bg = "black").place(x= 800, y = 90)


#Output box place with text
output_text = Text(root, font = "arial 10", height=9, fg="white", wrap = WORD, padx = 5, pady=5, width=50)

output_text.place(x=700,y=125)


#Imports all the languages from our googletrans module
languages = list(LANGUAGES.values())

#Creates scroll down box, with the values being our languages from google module.
dest_lang = ttk.Combobox(root,values=languages, width=22)
dest_lang.place(x=440, y = 180)

#Automatic Text on the scroll bar to choose language
dest_lang.set("Select Language")


#Now we need function to translate text
def Translate():

    try:
        translator = Translator()
        translated = translator.translate(text=input_original_text.get(), dest = dest_lang.get())
        output_text.delete(1.0, END)
        output_text.insert(END, translated.text)

    except Exception as e:
        output_text.delete(1.0, END)
        output_text.insert(END, f"Error: {str(e)}")



#Button won't work without command=
translated_button = Button(root, text="Translate", font = 'arial 12 bold', pady = 5, command=Translate, bg="red", activebackground="white")

translated_button.place(x=510,y=135)

root.mainloop()