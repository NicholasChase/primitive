import tkinter.filedialog as filedialog
import tkinter as tk
import os
import utils as util
from tkinter import messagebox
from tkinter import *
from re import search

inputPath = ''# Global variable to store inputPath
outputPath = ''# Global variable to store outputPath
master = tk.Tk()
master.title("Primitive")

def input():
    input_path = tk.filedialog.askopenfilename()
    global inputPath
    
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'
    # Checks to see if input file is correct file type
    if search("png", input_path):
        inputPath = input_path
    elif search("jpg", input_path):
        inputPath = input_path
    elif search("svg", input_path):
        inputPath = input_path
    elif search("gif", input_path):
        inputPath = input_path
    else:
        messagebox.showinfo("Error", "Wrong File Type")
    
	
def output():
    path = tk.filedialog.askdirectory()
    global outputPath
    
    output_entry.delete(1, tk.END)  # Remove current text in entry
    output_entry.insert(0, path)  # Insert the 'path'
    # Checks to see if output path contans file extension
    if search("png", path):
        outputPath = path
    elif search("jpg", path):
        outputPath = path
    elif search("svg", path):
        outputPath = path
    elif search("gif", path):
        outputPath = path
    else:
        messagebox.showinfo("Error", "No Output Name/File Extension")
    
def getUrlImage():
    global inputPath
    global outputPath
    url = imageURL.get()
    ext = util.getExtension(url)#gets the extendsion of the URL
    outExt = util.getExtension(outputPath)# gets the extension of the output path cause that where the new image file will be named
    
    #makes sure that the file trying to be downloaded is the same extension of user input
    #also makes sure that there are extensions and URL
    if imageURL == '':
        messagebox.showinfo("Error", "No URL to Image !")
        return
    elif ext == '':
        messagebox.showinfo("Error", "Please Have an Extension")
        return
    elif ext != outExt:
        messagebox.showinfo("Error", "Extensions Don't Match")
        return
    else:
        print("Here")
        util.getImage(url, outputPath)
        inputPath = outputPath
        


def makePhoto():
    # Todo Figure out a way to take in user input from buttons/input boxes and
    # Not have to have if statements for every possibility but for now because 
    # Of time constraints and limited knowledge on tkinter if statements will 
    # be sufficent
    try:
        alphaInput = alphaNum.get()
        if alphaInput == '':
            os.system("primitive -i %s -o %s -n 100" %(inputPath,outputPath))
            print("false")
            return
        else:
            os.system("primitive -a %s -i %s -o %s -n 100 -f 2" %(alphaInput,inputPath,outputPath))
            return
            
    except OSError as e:
        raise e
	
def start():
    if inputPath != '' and outputPath != '':
        makePhoto()
    else:
        messagebox.showinfo("Error", "No Output/Input File!")

top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

	
top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)	
	
	

input_path = tk.Label(top_frame, text="Picture path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)

output_path = tk.Label(bottom_frame, text="Output Path:")
output_entry = tk.Entry(bottom_frame, text="", width=40)
browse2 = tk.Button(bottom_frame, text="Browse", command=output)

# alpha label and input 
alphaLabel = tk.Label(top_frame, text="Alpha:")
alphaNum = tk.Entry(top_frame,width=40)



#filter option dropdown
filterLabel = tk.Label(top_frame, text="Filter:")
FILTERS = [
"None",
"Gray Scale",
"Sepia",
"Negative"
]
selectedFilter = StringVar(master)
selectedFilter.set(FILTERS[0])
filterOptions = OptionMenu(master,selectedFilter, "None", "Gray Scale", "Sepia", "Negative")

#URL Label, Path, and Button
imageLabel = tk.Label(bottom_frame, text="URL To Image")
imageURL = tk.Entry(bottom_frame, text="",width=40)
imageButton = tk.Button(bottom_frame, text="Download Image:", command=getUrlImage)

help_button = tk.Button(bottom_frame, text = "Help!")
begin_button = tk.Button(bottom_frame, text='Begin!',command=start) #beginButton	

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)
	
input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)

alphaLabel.pack(pady=5)
alphaNum.pack(pady=5)

filterLabel.pack(pady=5)
filterOptions.pack(pady=5)

#URL Labels and Buttons
imageLabel.pack(pady=5)
imageURL.pack(pady=5)
imageButton.pack(pady=5)


begin_button.pack(pady=20, fill=tk.X)
help_button.pack(pady=5)
master.mainloop()

#def window():
#       Creates window for the program

#TODO Req 1.0
#def helpButton()
#   Creates a help button

#TODO 1.1
#def export()
#   allow the user to export their finished
#   picture to the location of their choice 
#TODO 1.2
#def difficulty()
#   allows the user to select the number of geometric shapes to form
#   the image

#TODO 1.3
#def geometricShapes()
#   allows the user to select what geometric shape to form
#   the image

#TODO 1.4
#def display()
#   Shows the final form of the image

#TODO Req 1.5
#def file()
    #allows the user to select the photo they want
    #import easygui
    #file = easygui.fileopenbox()

