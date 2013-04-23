
'''
this is the  view for our application.

This handles the bit the user can see.
'''
import tkinter as tk

class appView(tk.Frame):
    def __init__(self,  radops, master = None):
        self.createBits(radops)
        self.pack()
    
    def mkinputFm(self, textb ="Enter salary here"):
        self.inputFm = tk.Frame(self)
        self.inLbl = tk.Label(self, master = iputFm, Text = "Salary")
        self.inLbl.pack()
        
        self.inTb = tk.Text(self, master = iputFm)
        self.inTb[text] = textb
        self.inTb.pack()
        
        self.goBtn = tk.Button(self, master = iputFm)
        self.goBtn[text] = "Calculate Tax"
        self.goBtn[command] = super.goBtnPressed(inTB.text())
        self.goBtn.pack()
        self.inputFm.pack(cnf)
        
    def mkInFreqFm(self, radops):
        self.inFreqFm = tk.Frame(self, master = super)
        self.inFreqFm.pack()
        for a,b in radops:
            self.radbtn = tk.Radiobutton(self, master= inFreqFm)
            self.radbtn[Text] =a 
            self.radbtn[Variable] = b
            self.radbtn.pack()
    
    def createBits(self, radops):
        self.mkinputFm()
        self.mkinFreqFm(radops)
        self.outputFm = tk.Frame(self)
        self.outFreqFm = tk.Frame(self)
        
        self.inFreqFm.pack(side = "right")
        self.outputFm.pack(side = "bottom")
        self.outFreqFm.pack(side = "right")    

radops = [("annual",1), ("fortnightly",26)]
appViewer = appView(radops)
