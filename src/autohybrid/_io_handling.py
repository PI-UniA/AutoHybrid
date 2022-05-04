        
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