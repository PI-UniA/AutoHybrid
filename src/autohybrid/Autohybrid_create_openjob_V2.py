# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:37:41 2021

last change on We Jul 29 2021

@author: aumuemic
"""


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from xml.etree import cElementTree as ET


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My Autohybrid-App - Create a new job')
        self.geometry('380x280')

        # label
        self.label = ttk.Label(self, text='Autohybrid-app for updating positions')
        self.label.pack()
        
        # button
        self.button = tk.Button(self, text='About')
        self.button['command'] = self.button_clicked
        self.button.pack()
        
        # label 
        self.label = ttk.Label(self, text='1. Select result-file for new xy-coordinates')
        self.label.pack()
        
        self.open_button = tk.Button(self, text='Open a File', command=self.select_file)
        self.open_button.pack(side="top")
        
        # label 
        self.label = ttk.Label(self, text='2. Load the reference openjob-file')
        self.label.pack()
        
        # Referencejob-button 
        self.xy_button = tk.Button(self)
        self.xy_button["text"] = "Open Reference \n openjob-file"
        self.xy_button["command"] = self.select_openjob
        self.xy_button.pack(side="top")
        
        # label 
        self.label = ttk.Label(self, text='3. Save file as new.openjob with new coordinates')
        self.label.pack()
        
        # xy-button 
        self.xy_button = tk.Button(self)
        self.xy_button["text"] = "Export \n openjob-file"
        self.xy_button["command"] = self.save_openjob
        self.xy_button.pack(side="top")
        
        # label 
        self.label = ttk.Label(self, text='')
        self.label.pack()
        
        #quit-button
        self.quit = tk.Button(self, text="Quit", fg="red", command=self.destroy)
        self.quit.pack(side="top")

    def button_clicked(self):
        showinfo(title='Information',
                 message='Autohybrid-App for updating new Positions for Parts on a buildung-plattfom for an EOS-machine.')
        
    def xy_out(self):
        
        content = self.result_file.readlines()

        # print(str(content[3].rstrip('\n'))) # rstrip() cut characters from right side
        # Part 1
        self.xPosP1 = content[3].rstrip('\n')
        self.yPosP1 = content[5].rstrip('\n')
        # Part 2
        self.xPosP2 = content[10].rstrip('\n')
        self.yPosP2 = content[12].rstrip('\n')
        
        print("x-Position of first Part: "+self.xPosP1)
        print("y-Position of first Part: "+self.yPosP1)
        
        print("x-Position of second Part: "+self.xPosP2)
        print("y-Position of second Part: "+self.yPosP2)
        
    def select_file(self):
        filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
        )

        filename = fd.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)

        showinfo(title='Selected File', message=filename)
        
        self.result_file = open(filename, "rt")
        
    def select_openjob(self):
        filetypes = (
        ('text files', '*.openjob'),
        ('All files', '*.*')
        )

        filename = fd.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)

        showinfo(title='Selected File', message=filename)
        
        self.job_file = filename
        print(self.job_file)
        
    def save_openjob(self):
        self.tree = ET.parse(self.job_file)
        self.root = self.tree.getroot()
        
        content = self.result_file.readlines()

        # print(str(content[3].rstrip('\n'))) # rstrip() cut charakters from right side
        # Part 1
        self.xPosP1 = content[3].rstrip('\n')
        self.yPosP1 = content[5].rstrip('\n')
        # Part 2
        self.xPosP2 = content[10].rstrip('\n')
        self.yPosP2 = content[12].rstrip('\n')
        # Part 3
        self.xPosP3 = content[17].rstrip('\n')
        self.yPosP3 = content[19].rstrip('\n')
        # Part 4
        self.xPosP4 = content[24].rstrip('\n')
        self.yPosP4 = content[26].rstrip('\n')
        # Part 5
        self.xPosP5 = content[31].rstrip('\n')
        self.yPosP5 = content[33].rstrip('\n')
        
        partNumber = 0

        ### finding tags ###
        
        for parts in self.root.findall('parts'):
            for part in parts.findall('part'):
                parameter = part.find('./parameter').text
                print(parameter)
                for translation in part.findall('translation'):
                    for x in translation.findall('x'):
                        x = translation.find('x').text
                        print(x)
                        partNumber = partNumber + 1
                         ### count parts in job ###
                        print('Anzahl der Teile: '+str(partNumber))
                        
        ### modify the x and y positions of the parts ###
                        
        if(partNumber == 1):
            i = 1
            for x in self.root.iter('x'):   
                if(i == 1):
                    x.text = str(self.xPosP1)
                i = i+1
            j = 1        
            for y in self.root.iter('y'):
                if(j == 1):
                    y.text = str(self.yPosP1)
                j = j+1
        elif(partNumber == 2):
            i = 1
            for x in self.root.iter('x'):
                if(i == 1):
                    x.text = str(self.xPosP1)
                elif(i == 5):
                    x.text = str(self.xPosP2)
                i = i+1 
            j = 1     
            for y in self.root.iter('y'):
                if(j == 1):
                    y.text = str(self.yPosP1)
                elif(j == 5):
                    y.text = str(self.yPosP2)
                j = j+1
        elif(partNumber == 3):
            i = 1
            for x in self.root.iter('x'):
                if(i == 1):
                    x.text = str(self.xPosP1)
                elif(i == 5):
                    x.text = str(self.xPosP2)
                elif(i == 9):
                    x.text = str(self.xPosP3)
                i = i+1 
            j = 1     
            for y in self.root.iter('y'):
                if(j == 1):
                    y.text = str(self.yPosP1)
                elif(j == 5):
                    y.text = str(self.yPosP2)
                elif(j == 9):
                    y.text = str(self.yPosP3)
                j = j+1
        elif(partNumber == 4):
            i = 1
            for x in self.root.iter('x'):
                if(i == 1):
                    x.text = str(self.xPosP1)
                elif(i == 5):
                    x.text = str(self.xPosP2)
                elif(i == 9):
                    x.text = str(self.xPosP3)
                elif(i == 13):
                    x.text = str(self.xPosP4)
                i = i+1 
            j = 1     
            for y in self.root.iter('y'):
                if(j == 1):
                    y.text = str(self.yPosP1)
                elif(j == 5):
                    y.text = str(self.yPosP2)
                elif(j == 9):
                    y.text = str(self.yPosP3)
                elif(j == 13):
                    y.text = str(self.yPosP4)
                j = j+1
        elif(partNumber == 5):
            i = 1
            for x in self.root.iter('x'):
                if(i == 1):
                    x.text = str(self.xPosP1)
                elif(i == 5):
                    x.text = str(self.xPosP2)
                elif(i == 9):
                    x.text = str(self.xPosP3)
                elif(i == 13):
                    x.text = str(self.xPosP4)
                elif(i == 17):
                    x.text = str(self.xPosP5)
                i = i+1 
            j = 1     
            for y in self.root.iter('y'):
                if(j == 1):
                    y.text = str(self.yPosP1)
                elif(j == 5):
                    y.text = str(self.yPosP2)
                elif(j == 9):
                    y.text = str(self.yPosP3)
                elif(j == 13):
                    y.text = str(self.yPosP4)
                elif(j == 17):
                    y.text = str(self.yPosP5)
                j = j+1
                   
        ### write new job ###

        self.tree.write('C:/Users/aumuemic/Desktop/new.openjob') # set path and filename
        
        self.result_file.close()
  

if __name__ == "__main__":
    app = App()
    app.mainloop()
    