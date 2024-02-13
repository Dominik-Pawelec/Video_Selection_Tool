import tkinter as ttk
from tkinter import filedialog


def GetFile():
    return filedialog.askopenfilename()

def GetDirectory():
    return filedialog.askdirectory()

def GetFiles():
    return filedialog.askopenfiles()

def SaveFile():
    return filedialog.asksaveasfilename()




class GUI():
    def __init__(self):

        self.root = ttk.Tk(className=" Video Selection Tool")
        self.root.geometry("800x300")
        self.root.config(bg="lightgrey")

        self.base_frm = ttk.Frame(self.root)
        ttk.Button(self.base_frm,text="Merge Clips",width=20,height=8,command=self.mergeGUI).pack(side="left",ipadx=10,ipady=10)
        ttk.Button(self.base_frm,text="Cut from Clip",width=20,height=8,command=self.cutGUI).pack(side="left",ipadx=10,ipady=10)
        self.base_frm.pack()
        self.root.mainloop()

    def mergeGUI(self):
        print("Merge Clips")

        self.merge_frm = ttk.Frame(self.root)

        self.import_path_t = ()
        frm1 = ttk.LabelFrame(self.merge_frm,text="Import")
        ttk.Button(frm1,text="Select Import Files:",command=self.GetFiles).grid(row=0,column=0)
        frm1.grid(row=0,column=0)


        self.export_path = ""
        self.export_display = ttk.StringVar()
        self.export_display.set("not selected")
        frm2 = ttk.LabelFrame(self.merge_frm,text="Export")
        ttk.Button(frm2,text="Save as:",command=self.SaveFile).grid(row=0,column=0)
        ttk.Label(frm2,textvariable = self.export_display).grid(row=0,column=1)
        frm2.grid(row=1,column=0)
        

        frm3 = ttk.LabelFrame(self.merge_frm,text="Run")
        ttk.Button(frm3,text="Merge Clips",command = self.Run_Merge).grid(sticky="S")
        frm3.grid(row=2,column=1)
    
    
        self.base_frm.pack_forget()
        self.merge_frm.pack()
        self.root.mainloop()
    
    def GetFiles(self):
        self.import_path_t = filedialog.askopenfilenames(filetypes=[("mp4",".mp4")])
        print(self.import_path_t)

    def SaveFile(self):
        save_file = filedialog.asksaveasfilename(filetypes=[("mp4",".mp4")])
        if save_file==None or save_file=="":
            return
        self.export_path = save_file
        print(self.export_path)
        self.export_display.set(self.export_path)
    
    def Run_Merge(self):
        print("ok")
        
        

        


        

    def cutGUI(self):
        print("Cut from Clip")

        
    

        


if __name__ == "__main__":
    
    gui = GUI()
    