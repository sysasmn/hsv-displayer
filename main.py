from Tkinter import *
from hsv import *
#from bar import *

root = Tk()
root.geometry("500x500") 



class Application:
    def __init__(self, master):
            self.master = master
            master.title("HSV colour representation")
                            
            self.label = Label(master, text="HSV colour representation")
            self.label.pack()
           
           #we display colours in this button
            self.colour_button = Button(master, bg = "#000", activebackground="#000", width=20, height=10)
            self.colour_button.pack()

            self.hue_scale = Scale(master, from_=0, to=360, length=200, orient=HORIZONTAL, command=self.foo, label="Hue")
            self.hue_scale.pack()
            #command=self.foo() returns the error that foo takes exactly 1 arg 2 given
            #i think command of a scale passes that value to the scale

            self.sat_scale = Scale(master, from_=0, to=1, resolution=0.01, length=200, orient=HORIZONTAL, command=self.foo, label="Saturation")
            self.sat_scale.pack()

            self.val_scale = Scale(master, from_=0, to=1, resolution=0.01, length=200, orient=HORIZONTAL, command=self.foo,label="Value")
            self.val_scale.pack()
            
            #labels are displayed with these. Maybe I should anchor them so they don't change position when the size changes
            self.hsv_label = Label(master, justify=LEFT,text="HSV:")
            self.hsv_label.pack()

            self.rgb_label = Label(master, text="RGB:")

            self.rgb_label.pack()

            self.hex_label = Label(master, text="Hex:")
            self.hex_label.pack()

            self.close_button = Button(master, text="Close", command=master.quit)
            self.close_button.pack()

    #functions in the class need to pass that instance of the class when they run. Thats what the self argument is
    def foo(self, scaleval):
    #calculates hex rgb from hsv taken from scales and updates labels. also displays the colour    
    #scaleval is the value given by scale that calls it. it's simpler if we dont use it. 
        hue = self.hue_scale.get()
        sat = self.sat_scale.get()
        val = self.val_scale.get()

        hexstring  = hsvtohex(hue,sat,val)
        rgb = hsvtorgb(hue,sat,val)
        
        hsv_label_string="HSV: ("+str(hue)+", "+str(sat)+", "+str(val)+")"
        rgb_label_string="RGB: (" + str(int(rgb[0])) + ", " + str(int(rgb[1])) + ", " + str(int(rgb[2]))+")"
        
        self.hsv_label.configure(text=hsv_label_string)
        self.rgb_label.configure(text=rgb_label_string)
        self.hex_label.configure(text="Hex: " + str(hexstring))

        self.colour_button.configure(bg = hexstring)
        self.colour_button.configure(activebackground = hexstring)

my_gui = Application(root)

root.mainloop()
