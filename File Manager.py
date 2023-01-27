from tkinter import *
#from PIL import ImageTk, Image
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

# Major functions of file manager

# open a file box window 
# when we want to select a file
def open_window():
    read=easygui.fileopenbox()
    return read

# open file function
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('Confirmation', "File Not Found!")

# copy file function
def copy_file():
    source1 = open_window()
    destination1=filedialog.askdirectory()
    shutil.copy(source1,destination1)
    mb.showinfo('Confirmation', "File Copied !")

# delete file function
def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)             
    else:
        mb.showinfo('Confirmation', "File Not Found !")

# rename file function
def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension=os.path.splitext(chosenFile)[1]
    print("Enter New Name For The Chosen File")
    newName=input()
    path = os.path.join(path1, newName+extension)
    print(path)
    os.rename(chosenFile,path) 
    mb.showinfo('Confirmation', "File Renamed !")

# move file function
def move_file():
    source = open_window()
    destination =filedialog.askdirectory()
    if(source==destination):
        mb.showinfo('Confirmation', "Source And Destination Are Same")
    else:
        shutil.move(source, destination)  
        mb.showinfo('Confirmation', "File Moved !")

# function to make a new folder
def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter Name Of New Folder")
    newFolder=input()
    path = os.path.join(newFolderPath, newFolder)  
    os.mkdir(path)
    mb.showinfo('Confirmation', "Folder Created !")

# function to remove a folder
def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    mb.showinfo('Confirmation', "Folder Deleted !")

# function to list all the files in folder
def list_files():
    folderList = filedialog.askdirectory()
    sortlist=sorted(os.listdir(folderList))       
    i=0
    print("Files In ", folderList, "Folder Are:")
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1
    

#Creating the UI of our file manager

root = Tk()

# creating label and buttons to perform operations
Label(root, text="File Manager", font=("Helvetica", 16), fg="blue").grid(row = 5, column = 2)

Button(root, text = "Open A File", command = open_file).grid(row=15, column =2)

Button(root, text = "Copy A File", command = copy_file).grid(row = 25, column = 2)

Button(root, text = "Delete A File", command = delete_file).grid(row = 35, column = 2)

Button(root, text = "Rename A File", command = rename_file).grid(row = 45, column = 2)

Button(root, text = "Move A File", command = move_file).grid(row = 55, column =2)

Button(root, text = "Make A Folder", command = make_folder).grid(row = 75, column = 2)

Button(root, text = "Remove A Folder", command = remove_folder).grid(row = 65, column =2)

Button(root, text = "List All Files In Directory", command = list_files).grid(row = 85,column = 2)



root.mainloop()
