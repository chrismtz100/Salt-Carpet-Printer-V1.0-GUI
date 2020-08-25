from guizero import App, Text, TextBox, PushButton, Box, Window, Picture, MenuBar
from tkinter.filedialog import askopenfilename #helps read files
import subprocess
import os
import sys
import shutil

app = App(title="Salt Printer UI V1.0", width=800, height=480)

# ~~~~~~~~~~ Execution Functions ~~~~~~~~~~~~ #
#(DONE)
def import_file():
    allowedExt=["ngc", "txt"]
    allowedExtPic=["jpg", "png", "jpeg"]

    filename = askopenfilename() #show an "Open" dialog box and return the path to the selected file. Gives file path
    if filename is "": #If no file is selected, do nothing and break the function
        import_file_window.show()
        return
    
    fileext = grab_file_ext(filename) #Checks what file extension it is
    file_og_path.value = filename

    if fileext in allowedExt: #Opens only if txt or ngc
        file_name.value = "Filename: " + grab_file_name(filename)
        file_path.value = "Location: " + filename
        file_status.value = "Status: Ready"
        file_view.value = filename
        import_file_window.show()
    
    elif fileext in allowedExtPic: #Opens only if jpg, png, and jpeg files and tries to convert them
        file_name.value = "Filename: " + grab_file_name(filename)
        file_path.value = "Location: " + filename
        file_status.value = "Status: Not Ready. Must convert file first"
        file_view.value = filename
        import_file_window.show()
        convert_file_option_window.show()

    else: #The file extension is not available
        file_name.value = "Filename: " + grab_file_name(filename)
        file_path.value = "Invalid file extension [" + grab_file_ext(filename) + "]." + " Supported files are [.ngc] [.jpeg] [.jpg] [.png] [.txt]"
        file_status.value = "Status: Not Ready"
        file_view.value = "nofile.png"
        import_file_window.show()
    

def download_file():
    print(file_status.value)
    if (file_status.value == "Status: Ready") | (file_status.value == "Status: Not Ready. Must convert file first"):
        print("Downloading...")

        #print(file_og_path.value)
        #file_og_path.value = file_og_path.value.replace("/", "\\\\")
        #print(file_og_path.value)
        print (grab_file_name(file_og_path))
        file_destination = "C:/Users/Christian/Documents/_School/CMPE 4371 - Sr Design 1/Salt Printer V1.0 GUI/downloads/" + grab_file_name(file_og_path)
        print(file_destination)
        shutil.move(file_og_path.value, file_destination)
        #shutil.move(file_og_path,"C:\\Users\\Christian\\Documents\\_School\\CMPE 4371 - Sr Design 1\\Salt Printer V1.0 GUI\\downloads")
        print("Downloaded Successful")

    else:
        print("Cannot print this file")

#(DONE)
def clear_file():
    file_name.value = "Filename: - - - "
    file_path.value = "Location: - - -"
    file_status.value = "Status: - - -"
    file_view.value = "nofile.png"

#(DONE)
def grab_file_name(file_path_temp): #Grabs file name
    if '/' in file_path_temp:
        name = file_path_temp.split('/')
    elif '\\' in file_path_temp:
        name = file_path_temp.split('\\')
    return (name[-1])

#(DONE)
def grab_file_ext(file_path_temp): #Grabs file extension
    ext = file_path_temp.split('.')
    return (ext[-1])

def convert2ngc(file_name_temp):
    print("Convert File to NGC was pressed")
    convert_file_option_window.hide()
    file_name_temp.value = "FILE WAS CONVERTED"
    #if user says yes: 
            #convert2ngc(file_path)
            #file_path.value
            #file_path.value = os.path.join('C:\\Users\\Christian\\Documents', file_name)
            #file_status.value = "Status: Ready"
            #file_view.value = file_name
        #if user says no: #remove file path, name, etc.
            #do nothing

# ~~~~~~~~ Button Functions ~~~~~~~~~~~ #
#(DONE) (Maybe)
def cancel_stop(): #Cancels or Stops job (might separate these two)
    print("Cancel Button was pressed")
    clear_file()
    cancel_stop_window.hide()

#(DONE)
def help_assistance(): #Help Assistance shows what each buttons does.
    print("Help Button was pressed")
    help_window.show()

def pause(): #Pauses machine parts and software
    print("Pause Button was pressed")


def print_job(): #Prints the file in the machine queue
    print("Print Button was pressed")

#(DONE)
def power_off(): #Turns off machine
    print("Power Off Button was pressed")
    app.destroy()

#(DONE)
def close_windows(): #This function closes any window by closing any window its on. 
    print("Closed all windows")
    import_file_window.hide()
    cancel_stop_window.hide()
    help_window.hide()
    pause_window.hide()
    print_window.hide()
    about_us_window.hide()

    
# ~~~~~~~~~~~ Windows are initialized below this line ~~~~~~~~~~~ #
import_file_window = Window(app, title="Import/File Window", width=800, height=480) #Import/File window here to app
import_file_window.hide()

convert_file_option_window = Window(import_file_window, title="Convert Image to NGC Option", width=800, height=480)
convert_file_option_window.hide()

cancel_stop_window = Window(app, title="Cancel/Stop Window", width=400, height=240) #Cancel window here to app
cancel_stop_window.hide()

help_window = Window(app, title="Help Window", width=800, height=480) #Help window here to app
help_window.hide()

pause_window = Window(app, title="Pause Window", width=400, height=240) #Pause window here to app
pause_window.hide()

print_window = Window(app, title="Print Window", width=400, height=240) #Print window here to app
print_window.hide()

about_us_window = Window(app, title="About Us",width=800, height=480) #About Us window here to app
about_us_window.hide()
# ~~~~~~~~~~~ Button Groups ~~~~~~~~~~~#
main_menu_group1 = Box(app, align="top") #First Level of Main Menu GUI. Contains Import/File & Help Button
spacer_box = Box(app, width="fill",  height="50",align="top")
main_menu_labels = Box(app, width="fill", align="top")
main_menu_group2 = Box(app, width="fill", align="top") #Second Level of Main Menu GUI. Contains Cancel & Pause Button
main_menu_group3 = Box(app, width="fill", align="bottom") #Bottom of the Main Menu GUI. Contains Home Button and Power Off.

import_file_buttom1 = Box(import_file_window, width="fill", align="bottom") #Bottom of the Import File Window GUI. Contains Home Button and Power Off.
import_file_bottom2 = Box(import_file_window, width="fill", align="bottom")
import_file_right = Box(import_file_window, height="fill", align="right")

cancel_top = Box(cancel_stop_window, width="fill", height="fill", align="top")
cancel_bottom = Box(cancel_stop_window, width="fill", align="bottom") #Bottom of the Cancel Window GUI. Contains Home Button and Power Off.

help_bottom = Box(help_window, width="fill", align="bottom") #Bottom of the Help Window GUI. Contains Home Button and Power Off.

pause_top = Box(pause_window, width="fill", height="fill", align="top")
pause_buttom = Box(pause_window, width="fill", align="bottom") #Bottom of the Pause Window GUI. Contains Home Button and Power Off.

print_bottom = Box(print_window, width="fill", align="bottom") #Bottom of the Print Window GUI. Contains Home Button and Power Off.
about_us_bottom = Box(about_us_window, width="fill", align="bottom") #Bottom of the Print Window GUI. Contains Home Button and Power Off.

# ~~~~~~~~~~~ App and Other Window Buttons ~~~~~~~~~~~~ #
import_button = PushButton(import_file_bottom2, command=import_file, align="left", text="Import File") #Import Button
about_button = PushButton(main_menu_group3, command=about_us_window.show, align="left", text="About Us") #About Us Button
convert_button = PushButton(import_file_bottom2, command=convert2ngc, align="left", text="Convert File") #Convert Button 
remove_file_button = PushButton(import_file_bottom2, command=clear_file, align="left", text="Remove File") #Remove File Button
download_file_button = PushButton(import_file_bottom2, command=download_file, align="left", text="Download File") #Download File Button

cancel_yes_button = PushButton(cancel_top, command=cancel_stop, width="fill", height="fill", align="left", text="Yes")
cancel_no_button = PushButton(cancel_top, command=cancel_stop_window.hide, width="fill", height="fill", align="right", text="No")
convert_yes_button = PushButton(convert_file_option_window, command=convert2ngc, align="left", text="Yes", width="fill")
convert_no_button = PushButton(convert_file_option_window, command=convert_file_option_window.hide, align="right", text="No", width="fill")
pause_yes_button = PushButton(pause_top, command=pause, width="fill", height="fill", align="left", text="Yes")
pause_no_button = PushButton(pause_top, command=pause_window.hide, width="fill", height="fill", align="right", text="No")

power_off_button = PushButton(import_file_buttom1, command=power_off, align="right", text="POWER OFF") #PowerOff Button - Import File 
power_off_button = PushButton(cancel_bottom, command=power_off, align="right", text="POWER OFF") #PowerOff Button - Cancel
power_off_button = PushButton(help_bottom, command=power_off, align="right", text="POWER OFF") #PowerOff Button Help
power_off_button = PushButton(pause_buttom, command=power_off, align="right", text="POWER OFF") #PowerOff Button - Pause
power_off_button = PushButton(print_bottom, command=power_off, align="right", text="POWER OFF") #PowerOff Button - Print
power_off_button = PushButton(about_us_bottom, command=power_off, align="right", text="POWER OFF") #PowerOff Button - About Us

home_button = PushButton(import_file_buttom1, command=close_windows, align="left", text="Close Import/File Window") #Home Button - Import
home_button = PushButton(cancel_bottom, command=close_windows, align="left", text="Close Cancel/Stop Window") #Home Cancel
home_button = PushButton(help_bottom, command=close_windows, align="left", text="Close Help Window")
home_button = PushButton(pause_buttom, command=close_windows, align="left", text="Close Pause Window")
home_button = PushButton(print_bottom, command=close_windows, align="left", text="Close Print Window")
home_button = PushButton(about_us_bottom, command=close_windows, align="left", text="Close About Us Window")
# ~~~~~~~~~~~ Main Buttons in Main Menu ~~~~~~~~~~~~ #
spacer_msg = Text(main_menu_group2, text="      ", align="left")
import_menu_button = PushButton(main_menu_group2, command=import_file_window.show, align="left", image="import.png") #Import/File Button
spacer_msg = Text(main_menu_group2, text="     ", align="left")


print_menu_button = PushButton(main_menu_group2, command=print_window.show, align="left", image="print.png") #Print Button
spacer_msg = Text(main_menu_group2, text="     ", align="left")

cancel_menu_button = PushButton(main_menu_group2, command=cancel_stop_window.show, align="left", image="cancel.png") #Cancel/Stop Button
spacer_msg = Text(main_menu_group2, text="     ", align="left")

help_menu_button = PushButton(main_menu_group2, command=help_assistance, align="left", image="help.png") #Help Button
spacer_msg = Text(main_menu_group2, text="     ", align="left")

power_off_button = PushButton(main_menu_group2, command=power_off, align="left", image="power.png") #PowerOff Button - Main Menu
spacer_msg = Text(main_menu_group2, text="     ", align="left")
# ~~~~~~~~~~~~ Pictures ~~~~~~~~~~~~~ #
#salt_printer_logo = Picture(main_menu_group3, image="salt.png", width=50, height=50, align="bottom")
#salt_printer_logo = Picture(import_file_buttom1, image="salt.png", width=50, height=50, align="bottom")
#salt_printer_logo = Picture(cancel_bottom, image="salt.png", width=50, height=50, align="bottom")
#salt_printer_logo = Picture(help_bottom, image="salt.png", width=50, height=50, align="bottom")
#salt_printer_logo = Picture(pause_buttom, image="salt.png", width=50, height=50, align="bottom")
#salt_printer_logo = Picture(print_bottom, image="salt.png", width=50, height=50, align="bottom")
#salt_printer_logo = Picture(about_us_bottom, image="salt.png", width=50, height=50, align="bottom")

file_view = Picture(import_file_window, image="nofile.png", width=200, height=300, align="right") #This is the file

title = Picture(main_menu_group1, image="title-2d.png")
# ~~~~~~~~~~~ Messages on Screen/Window ~~~~~~~~~~~ #  
about_us_msg = Text(about_us_window, text="Hello User, \n This Salt Printer is Version 1.0. \n It was developed in the UTRGV Fabrication Lab. \n Under the direction of Donna Mason Sweigart, this Salt Printer \n could not have been created by Alissa Flores, \n Elliud, Roberto Rivas, Vilma, and Christian A. Martinez.")
convert_file_msg = Text(convert_file_option_window, align="top", text="Do you want to convert \n this file to NGC?")
cancel_file_msg = Text(cancel_stop_window, text="Do you want to cancel \n this current file/job?")
help_msg = Text(help_window, text="IMPORT: Imports a file from the Raspberry Pi and queues only one job at a time. \n \n CANCEL/STOP: Cancels queued job or Stop current printing job.\n \n HELP: Displays a list of instructions of each button.\n \n PAUSE: Pauses current printing job and can resume current job as well.\n \n PRINT: Grabs queued file and prints the file in salt.")
pause_msg = Text(pause_window, text="Do you want to pause \n this current job?")
no_job_msg = Text(print_window, align="top", text="There are no jobs ready")

file_name = Text(import_file_window, text="File Name: - - -", align="top") #this is the file name
file_path = Text(import_file_window, text="File Path: - - -", align="top") #this is a file path
file_status = Text(import_file_window, text="Status: - - -", align="top") #this is the status of the file 
file_og_path = Text(import_file_window, text="", align="top")

import_label = Text(main_menu_labels, text="          Import", align="left", size=16)
print_label = Text(main_menu_labels, text="                Print", align="left", size=16)
cancel_label = Text(main_menu_labels, text="               Cancel", align="left", size=16)
help_label = Text(main_menu_labels, text="                Help", align="left", size=16)
power_label = Text(main_menu_labels, text="             Shutdown", align="left", size=16)

# ~~~~~~~~~~~~ Menu Bar ~~~~~~~~~~~~~~~~ #
# menubar_home = MenuBar(app,
#                   toplevel=["File", "Help"],
#                   options=[
#                       [ ["Import File", import_file], ["Clear File", clear_file], ["Power Off", power_off] ],
#                       [ ["Manual", help_assistance]]
#                   ])

# menubar_import = MenuBar(import_file_window,
#                   toplevel=["File", "Help"],
#                   options=[
#                       [ ["Import File", import_file], ["Clear File", clear_file], ["Power Off", power_off] ],
#                       [ ["Manual", help_assistance]]
#                   ])

# menubar_convert_file = MenuBar(convert_file_option_window,
#                   toplevel=["File", "Help"],
#                   options=[
#                       [ ["Import File", import_file], ["Clear File", clear_file], ["Power Off", power_off] ],
#                       [ ["Manual", help_assistance]]
#                   ])

# menubar_cancel = MenuBar(cancel_stop_window,
#                   toplevel=["File", "Help"],
#                   options=[
#                       [ ["Import File", import_file], ["Clear File", clear_file], ["Power Off", power_off] ],
#                       [ ["Manual", help_assistance]]
#                   ])

# menubar_help = MenuBar(help_window,
#                   toplevel=["File", "Help"],
#                   options=[
#                       [ ["Import File", import_file], ["Clear File", clear_file], ["Power Off", power_off] ],
#                       [ ["Manual", help_assistance]]
#                   ])

# menubar_pause = MenuBar(pause_window,
#                   toplevel=["File", "Help"],
#                   options=[
#                       [ ["Import File", import_file], ["Clear File", clear_file], ["Power Off", power_off] ],
#                       [ ["Manual", help_assistance]]
#                   ])

# menubar_print = MenuBar(print_window,
#                   toplevel=["File", "Help"],
#                   options=[
#                       [ ["Import File", import_file], ["Clear File", clear_file], ["Power Off", power_off] ],
#                       [ ["Manual", help_assistance]]
#                   ])

# menubar_about_us = MenuBar(about_us_window,
#                   toplevel=["File", "Help"],
#                   options=[
#                       [ ["Import File", import_file], ["Clear File", clear_file], ["Power Off", power_off] ],
#                       [ ["Manual", help_assistance]]
#                   ])

# ~~~~~~~~~~~~  Variables  ~~~~~~~~~~~~~~~~ #


# ~~~~~~~~~~~~ App Display ~~~~~~~~~~~~~~~~ #
app.display()