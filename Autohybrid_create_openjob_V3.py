# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:37:41 2021

last change on  Mai 04 2022

@author: aumuemic,Lichu
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
        
        ### finding tags ###
        partNumber = 0
        xPos = list();
        yPos = list();
        for parts in self.root.findall('parts'):
            for part in parts.findall('part'):
                parameter = part.find('./parameter').text
                for translation in part.findall('translation'):
                    for x in translation.findall('x'):
                        x = translation.find('x').text
                        partNumber = partNumber + 1
                         ### count parts in job ###
        
        print('Anzahl der Teile: '+str(partNumber))

        self.xPos =list(range(partNumber))
        self.yPos =list(range(partNumber))

        for i in range(partNumber):
            self.xPos[i] = content[i*7+3].rstrip('\n')
            self.yPos[i] = content[i*7+5].rstrip('\n')

        print('The coordinates will be replaced with:\n')
        print(self.xPos)
        print(self.yPos)
        print('\n')
        # print(str(content[3].rstrip('\n'))) # rstrip() cut charakters from right side

        for i in range(partNumber):
            
            a = 1   
            for x in self.root.iter('x'):
                # print(x)
                # print(x.text)
                if a==(4.*i+1):
                    x.text = str(self.xPos[i])
                a = a + 1 

            a = 1
            for y in self.root.iter('y'):
                # print(y)
                # print(y.text)
                if a==(4.*i+1):
                    y.text = str(self.yPos[i])
                a = a + 1 
              

        path = 'C:/Users/wanglich/Desktop/new.openjob'
        self.tree.write(path) # set path and filename

        print('Neues dokument ist speichert unter',path)
        
        self.result_file.close()
  

if __name__ == "__main__":
    app = App()
    app.mainloop()
    