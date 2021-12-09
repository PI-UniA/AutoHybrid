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