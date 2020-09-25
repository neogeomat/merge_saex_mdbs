from Tkinter import *
from tkMessageBox import showerror

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.pack()

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create buttons that do nothing"""

        #create label for sheet
        self.Sheet=Label(self, text="Enter path to the main folder",width=30)
        self.Sheet.grid(row=0, column=0,sticky=E+W+N+S)

        #create entry.
        self.sheetentry1= Entry(self,width=30)
        self.sheetentry1.grid(row=0, column =1, sticky=E+W+N+S)        
    
        
        #create calculate button
        self.button4=Button(self, text="Process", command=self.parcelIDcreator, width=30)
        self.button4.grid(row=1, column=1, sticky=E+W+N+S)

    def parcelIDcreator (self):   
        import tkMessageBox
        import arcpy
        import glob
        from arcpy import env
        path = self.sheetentry1.get()
        #print(path)
        list = glob.glob(path+"\**\*.mdb")
        list.append(glob.glob(path+"\*.mdb"))
        merged = "D:\\LIS_SYSTEM\\LIS_Spatial_Data\\merged.mdb\\"
        layers = ["Parcel","Segments","Construction","Parcel_History"]
        print(list)
        for i in list:
            env.workspace = i
            print (env.workspace)

            #Setting input and output
            inFeatures = ["Parcel"]

            for l in layers:
                arcpy.Append_management(l, merged + l, "NO_TEST", "", "")

        tkMessageBox.showinfo(title="Merge Saex Mdb files", message="Done")
            
root = Tk()
root.title("Merge Saex Mdb files")
myapp = App(root)
myapp.mainloop()




