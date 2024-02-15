import tkinter as ttk
from tkinter import filedialog

import VideoManipulations as vm
from Logger import Logger


class GUI():
    def __init__(self):
        self.log = Logger()

        self.root = ttk.Tk(className=" Video Selection Tool")
        self.root.geometry("800x300")
        self.root.config(bg="lightgrey")
        
        self.selectionGUI()

    def selectionGUI(self):
        print("Selection")

        self.base_frm = ttk.Frame(self.root)
        ttk.Button(self.base_frm,text="Merge Clips",width=20,height=8,command=self.mergeGUI).pack(side="left",ipadx=10,ipady=10)
        ttk.Button(self.base_frm,text="Cut from Clip",width=20,height=8,command=self.cutGUI).pack(side="left",ipadx=10,ipady=10)

        try:
            self.merge_frm.destroy()
        except:
            ""
        
        self.base_frm.pack()
        self.root.mainloop()


#===========MERGE GUI============

    def mergeGUI(self):
        print("Merge Clips")

        self.merge_frm = ttk.Frame(self.root)

        self.import_path_t = ()
        frm1 = ttk.LabelFrame(self.merge_frm,text="Import")
        ttk.Button(frm1,text="Select Import Files:",command=self.GetFiles).grid(row=0,column=0)
        frm1.grid(row=0,column=0,sticky="W")


        self.export_path = ""
        self.export_display = ttk.StringVar()
        self.export_display.set("not selected")
        frm2 = ttk.LabelFrame(self.merge_frm,text="Export")
        ttk.Button(frm2,text="Save as:",command=self.SaveFile).grid(row=0,column=0)
        ttk.Label(frm2,textvariable = self.export_display).grid(row=0,column=1)
        frm2.grid(row=1,column=0)
        

        frm3 = ttk.LabelFrame(self.merge_frm,text="Render quality:")
        resolutions = ["default res.","480p"]
        self.resolution_display = ttk.StringVar()
        self.resolution_display.set("default res.")
        ttk.OptionMenu(frm3, self.resolution_display, *resolutions).grid(row=0,column=0,sticky="S")
        ttk.Button(frm3,text="Run Merge",command = self.RunMerge).grid(row=0,column=1,sticky="ES")
        frm3.grid(row=2,column=1)
    

        frm4 = ttk.LabelFrame(self.merge_frm,text="Render quality:")
        ttk.Button(frm4,text="Back",command = self.selectionGUI).grid(row=0,column=1,sticky="ES")
        frm4.grid(row=2,column=0)
    

        self.base_frm.destroy()
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
        self.export_display.set(self.export_path)
        print(self.export_path)

    def RunMerge(self):
        

        if len(self.import_path_t)==0:
            self.Popup("No import file was selected")
            return
        
        import_path_l = list(self.import_path_t)  
        merged_clips = vm.mergeClips(import_path_l)

        if len(self.export_path)==0:
            self.Popup("No export file was selected")
            return
        
        res = self.resolution_display.get()
        if res == "480p":
            vm.changeRes(merged_clips,(854,480))
        
        vm.exportClip(merged_clips,self.export_path)
        
        self.Popup("Finished merging clips")
        return

    
    def ProgressBar(self):
        popup = ttk.Toplevel(self.root)
        popup.geometry("250x60")
        popup.title("Processing...")

        progress_bar_display = ttk.StringVar()
        progress_bar_display.set(str(self.log.percentage))
        ttk.Label(popup,text=progress_bar_display).pack()
        

    def Popup(self,message:str):
        popup = ttk.Toplevel(self.root)
        popup.geometry("250x60")
        popup.title(message)
        ttk.Label(popup,text=message).pack()
        ttk.Button(popup,text="Ok",command=popup.destroy,width=10).pack()


 
#===========CUT GUI================
    def cutGUI(self):

        print("Cut from Clip")

        
    

        


if __name__ == "__main__":

    gui = GUI()
    