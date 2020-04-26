import tkinter.filedialog as filedialog
import tkinter.font as font
import tkinter as tk
from tkinter import ttk 
import os
import utils as util
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from re import search
import PIL
from PIL import ImageTk as a
from PIL import Image

inputPath = ''# Global variable to store inputPath
outputPath = ''# Global variable to store outputPath
mode = '0'
filter = '0'
master = tk.Tk()
master.title("Primitive")

def help():
    messagebox.showinfo("Help!", "To begin first press the browse button under the picture path. Choose a photo that is of .jpg/png/gif type. Next find a output path. Ex. C:/Users/Desktop/output.jpg. In the primitive program, there are several different options to chose from. You can choose how transparent you want the picture to appear by changing the value in Alpha. You can rotate the image by changing the degrees in the rotation slot. You can apply a filter by selecting from the drop down menu. Once you are satisfied with the options presented, press the begin button and see your results.")

def input():
    input_path = tk.filedialog.askopenfilename()
    global inputPath
    
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'
    # Checks to see if input file is correct file type
    if util.checkOutPath(input_path) == True:
        inputPath = input_path
    else:
        messagebox.showinfo("Error", "Wrong File Type")
    
def output():
    path = tk.filedialog.askdirectory()
    global outputPath
    
    output_entry.delete(1, tk.END)  # Remove current text in entry
    output_entry.insert(0, path)  # Insert the 'path'
    # Checks to see if output path contans file extension    
    outputPath = path
        
def displayImage():
    global outputPath
    print("THIS Is IDSPLAY " + outputPath)
    #creates a new window to display preview
    img = util.previewImage(outputPath)
    newwin = tk.Toplevel(master)
    newwin.title("Preview")
    newwin.title('New Window')
    newwin.geometry("500x500")
    newwin.resizable(0, 0)

    display = Label(newwin, text="Preview")


    l=tk.Label(newwin,image=img)
    l.image = img
    display.pack()
    l.pack(pady=5)
    
def getUrlImage():
    global inputPath
    global outputPath
    url = imageURL.get()
    ext = util.getExtension(url)#gets the extendsion of the URL
    outExt = util.getExtension(outputPath)# gets the extension of the output
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
    mode = selectedMode.get()
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
    # TODO:
    # Get Filter, Brightness, and Rotation 
    global filter
    global mode
    global outputPath
    try:
        alphaInput = alphaEntry.get()
        angleInput = angleEntry.get().replace('\u00B0','')
        brightnessInput = str(brightnessSlider.get())
        numShapesInput = numberOfShapesEntry.get()
        numWorkers = workerEntry.get()
        outputPath = outputPath + "/" + filenameEntry.get() + selectedExtension.get()
        print("This is outputPath " + outputPath)
        print("This is inputPath " + inputPath)
        os.system("go run main.go -f %s -a %s -i %s -o %s -n %s -j %s -m %s" %(filter, alphaInput,inputPath,outputPath, numShapesInput, numWorkers, mode))
        
        return
            
    except OSError as e:
        raise e
    
def start():
    if inputPath != '' and outputPath != '':
        makePhoto()
        displayImage()
    else:
        messagebox.showinfo("Error", "No Output/Input File!")
		

def help():
	messagebox.showinfo("Help!", "To begin first press the browse button under the picture path. Choose a photo that is of .jpg/png/gif type. Next find a output path. Ex. C:/Users/Desktop/output.jpg. In the primitive program, there are several different options to chose from. You can choose how transparent you want the picture to appear by changing the value in Alpha. You can rotate the image by changing the degrees in the rotation slot. You can apply a filter by selecting from the drop down menu. Once you are satisfied with the options presented, press the begin button and see your results.")

# mode options
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

#filter options
FILTERS = [
"None",
"Gray Scale",
"Sepia",
"Negative"
]

#file extension options
EXTENSIONS = [
".png",
".jpg",
".svg",
".gif"
]

############################## frame setup ###############################
input_frame = tk.Frame(master)
input_frame.pack(side=tk.TOP)
primitive_frame = tk.Frame(master)
primitive_frame.pack(side=tk.TOP)

output_frame = tk.Frame(master)
output_frame.pack(side=tk.TOP)


################################### font ##################################
headerFont = font.Font(size=20)


############################# help button #################################
help_button = tk.Button(input_frame, text = "Help!", command = help)
help_button.grid(row=0, column= 2 )


############################ input image frame #############################
inputImageLabel = tk.Label(input_frame, text="Input Image")
inputImageLabel['font'] = headerFont

inputPathLabel = tk.Label(input_frame, text="Picture Path:")
input_entry = tk.Entry(input_frame, width=40)
browse1 = tk.Button(input_frame, text="Browse", command=input)

inputUrlLabel = tk.Label(input_frame, text="Picture URL:")
imageURL = tk.Entry(input_frame, width=40)
imageButton = tk.Button(input_frame, text="Download Image", command=getUrlImage)
 
#insert into grid
inputImageLabel.grid(row=0, column=1)
inputPathLabel.grid(row=1, column=0, padx = 10, pady = 20)
input_entry.grid(row=1, column=1)
browse1.grid(row=1, column=2)
inputUrlLabel.grid(row=2, column=0)
imageURL.grid(row=2, column=1)
imageButton.grid(row=2, column=2, padx = 10, pady = 20)


######################## primitive arguments frame ########################
modeLabel = tk.Label(primitive_frame, text="Mode:")
mode_OpMenu_width = len(max(MODES,key=len))#length of largest item in MODES
selectedMode = StringVar(master)
selectedMode.set(MODES[0])
modeOptions = OptionMenu(primitive_frame,selectedMode,'Combo',*MODES)#minor change for option menu fill
modeOptions.config(width=mode_OpMenu_width)#set width to length of largest item
selectedMode.trace("w", getModeOption)

numberOfShapesLabel = tk.Label(primitive_frame, text="Number of Shapes:")
numberOfShapesEntry = tk.Entry(primitive_frame, width=10)
numberOfShapesEntry.insert(0, "100")
 
alphaLabel = tk.Label(primitive_frame, text="Alpha:")
alphaEntry = tk.Entry(primitive_frame, width=10)
alphaEntry.insert(0, "128")

workerLabel = tk.Label(primitive_frame, text="Number of Workers:")
workerEntry = tk.Entry(primitive_frame, width=10)
workerEntry.insert(0, "0")

filterLabel = tk.Label(primitive_frame, text="Filter:")
filt_OpMenu_width = len(max(FILTERS,key=len))#length of largest item in FILTERS
selectedFilter = StringVar(master)
selectedFilter.set(FILTERS[0])
filterOptions = OptionMenu(primitive_frame,selectedFilter,'None',*FILTERS)#minor change for option menu fill
filterOptions.config(width=filt_OpMenu_width)#set width to length of largest item
selectedFilter.trace("w", getFilterOption)
 
brightnessLabel = tk.Label(primitive_frame, text="Brightness:")
brightnessSlider = tk.Scale(primitive_frame, from_=-100, to=100, orient=HORIZONTAL)

#TODO: implement saturation slider

#TODO: implement blur function
 
angleLabel = tk.Label(primitive_frame, text="Rotate:")
angleEntry = tk.Entry(primitive_frame,width=10)
angleEntry.insert(0, "0\u00B0")

#insert into grid
modeLabel.grid(row=0, column=0)
modeOptions.grid(row=0, column=1)
numberOfShapesLabel.grid(row=1, column=0)
numberOfShapesEntry.grid(row=1, column=1)
alphaLabel.grid(row=2, column=0)
alphaEntry.grid(row=2, column=1)
workerLabel.grid(row=3, column=1)
workerEntry.grid(row=3, column=2, padx = 10, pady = 20)
filterLabel.grid(row=0, column=3)
filterOptions.grid(row=0,column=4)
brightnessLabel.grid(row=1, column=3)
brightnessSlider.grid(row=1, column=4)
angleLabel.grid(row=2, column=3)
angleEntry.grid(row=2, column=4)


############################ output image frame #############################
outputImageLabel = tk.Label(output_frame, text="Output Image")
outputImageLabel['font'] = headerFont

#TODO: implement file name
filenameLabel = tk.Label(output_frame, text="Filename:")
filenameEntry = tk.Entry(output_frame, width=40)

pathLabel = tk.Label(output_frame, text="Path:")
output_entry = tk.Entry(output_frame, width=40)
browse2 = tk.Button(output_frame, text="Browse", command=output)


extensionLabel = tk.Label(output_frame, text="Extension:")
extension_OpMenu_width = len(max(EXTENSIONS,key=len))#length of largest item in EXTENSIONS
selectedExtension = StringVar(master)
selectedExtension.set(EXTENSIONS[0])
extensionOptions = OptionMenu(output_frame,selectedExtension,'.png',*EXTENSIONS)#minor change for option menu fill
extensionOptions.config(width=extension_OpMenu_width)#set width to length of largest item



begin_button = tk.Button(output_frame, text='Begin!',command=start)
begin_button['font'] = headerFont

#insert into grid
outputImageLabel.grid(row=0, column=1, padx = 10, pady = 20)
filenameLabel.grid(row=1, column=0)
filenameEntry.grid(row=1, column=1)

output_entry.grid(row=2, column=1)
browse2.grid(row=2, column=3, padx = 10)
extensionLabel.grid(row=3, column=0)
extensionOptions.grid(row=3, column=1)

pathLabel.grid(row=2, column=0)
begin_button.grid(row=4, columnspan=4, padx = 10, pady = 10)


master.mainloop()

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
