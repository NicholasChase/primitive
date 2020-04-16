import tkinter.filedialog as filedialog
import tkinter as tk
import os
import utils as util
from tkinter import messagebox
from tkinter import *
from re import search

inputPath = ''# Global variable to store inputPath
outputPath = ''# Global variable to store outputPath
filter = '0'
master = tk.Tk()
master.title("Primitive")
root = Tk()

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
        
def getFilterOption(*args):
    global filter
    filter = selectedFilter.get()
    if filter == 'Gray Scale':
        filter = '1'
    elif filter == 'Sepia':
        filter = '2'
    elif filter == 'Negative':
        filter = '3'
    elif filter == 'None':
        filter = '0'#default
    print(filter)
    return
    
    
def getModeOption(*args):
    global mode
    mode = selectedFilter.get()
    if mode == 'Combo':
        mode = '0'
    elif mode == 'Triangle':
        mode = '1'
    elif mode == 'Rectangle':
        mode = '2'
    elif mode == 'Ellipse':
        mode = '3'
    elif mode == 'Circle':
        mode = '4'
    elif mode == 'Rotated Rectangle':
        mode = '5'
    elif mode == 'Beziers':
        mode = '6'
    elif mode == 'Rotated Ellipse':
        mode = '7'
    elif mode == 'Polygon':
        mode = '8'
    return

def makePhoto():
    global filter
    global mode
    try:
        alphaInput = alphaEntry.get()
        angleInput = angleEntry.get().replace('\u00B0','')

        brightnessInput = str(brightnessSlider.get())

        os.system("primitive -f %s -a %s -i %s -o %s -n 100 -rot %s -b %s -m %s" %(filter,alphaInput,inputPath,outputPath,angleInput,brightnessInput, mode))

        return
            
    except OSError as e:
        raise e
	
def start():
    if inputPath != '' and outputPath != '':
        makePhoto()
    else:
        messagebox.showinfo("Error", "No Output/Input File!")
		

def help():
	messagebox.showinfo("Help!", "To begin first press the browse button under the picture path. Choose a photo that is of .jpg/png/gif type. Next find a output path. Ex. C:/Users/Desktop/output.jpg. In the primitive program, there are several different options to chose from. You can choose how transparent you want the picture to appear by changing the value in Alpha. You can rotate the image by changing the degrees in the rotation slot. You can apply a filter by selecting from the drop down menu. Once you are satisfied with the options presented, press the begin button and see your results.")

top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

	
top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)	
	
	

input_path = tk.Label(top_frame, text="Picture path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)

output_path = tk.Label(top_frame, text="Output Path:")
output_entry = tk.Entry(top_frame, text="", width=40)
browse2 = tk.Button(top_frame, text="Browse", command=output)

#output_path = tk.Label(root, text="Output Path:")
#output_path.grid(row=0, column=2)


# mode option
modeLabel = tk.Label(top_frame, text="Mode")
MODES = [
"Combo",
"Triangle",
"Rectangle",
"Ellipse",
"Circle",
"Rotated Rectangle",
"Beziers",
"Rotated Ellipse",
"Polygon"
]
selectedMode = StringVar(master)
selectedMode.set(MODES[1])
modeOptions = OptionMenu(top_frame,selectedMode, "Combo", "Triangle", "Rectangle", "Ellipse", "Circle", "Rotated Rectangle", "Beziers", "Rotated Ellipse", "Polygon")
selectedMode.trace("w", getModeOption)

# alpha label and input 
alphaLabel = tk.Label(top_frame, text="Alpha:")
alphaEntry = tk.Entry(top_frame,width=40)
alphaEntry.insert(0, "128")

#rotate option
angleLabel = tk.Label(top_frame, text="Rotate:")
angleEntry = tk.Entry(top_frame,width=40)
angleEntry.insert(0, "0\u00B0")


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
filterOptions = OptionMenu(top_frame,selectedFilter, "None", "Gray Scale", "Sepia", "Negative")
selectedFilter.trace("w", getFilterOption)

brightnessLabel = tk.Label(top_frame, text="Brightness:")
brightnessSlider = Scale(top_frame, from_=-100, to=100, orient=HORIZONTAL)




#URL Label, Path, and Button
imageLabel = tk.Label(bottom_frame, text="URL To Image")
imageURL = tk.Entry(bottom_frame, text="",width=40)
imageButton = tk.Button(bottom_frame, text="Download Image:", command=getUrlImage)


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

modeLabel.pack(pady=5)
modeOptions.pack(pady=5)

alphaLabel.pack(pady=5)
alphaEntry.pack(pady=5)

angleLabel.pack(pady=5)
angleEntry.pack(pady=5)

filterLabel.pack(pady=5)
filterOptions.pack(pady=5)

brightnessLabel.pack(pady=5)
brightnessSlider.pack(pady=5)

#URL Labels and Buttons
imageLabel.pack(pady=5)
imageURL.pack(pady=5)
imageButton.pack(pady=5)

help_button = tk.Button(bottom_frame, text = "Help!", command = help)


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

