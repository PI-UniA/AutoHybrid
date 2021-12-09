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