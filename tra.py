import Tkinter
from PIL import Image, ImageTk,ImageDraw

'''
  from the image using tk and image
'''
def image_tk():
 im_fna = Image.open("2.jpg")
 im_fna.save("k.gif")
 im_fna = im_fna.resize((400,400))
 root = Tkinter.Tk()
 tkim_fna = ImageTk.PhotoImage(im_fna)
 Tkinter.Label(root, image=tkim_fna).pack()
 root.mainloop()



'''show the image but enter all path'''
def image_show(imagepath):
    im = Image.open(imagepath)
    im.show()


'''
    save imag as more then tecnology
'''
def save_as(pathimg):
    im = Image.open(pathimg)
    im.save("n1.gif")
    im.save("n2.png")
    im.save("n3.pdf")




'''this function make the draw the image in dimension'''
def drawtheimag():
    im = Image.open("C:\\Users\\safwat\\PycharmProjects\\bioformatics\\2.jpg")
    draw = ImageDraw.Draw(im)
    data_string = "1 1 1 3 4 9 27 45 89 89 32 51 69 92 11 11 80 43"
    data_array = data_string.split(" ")
    x_coord = 20
    for i in data_array:
        x_coord = x_coord + 25
        y_coord = 300 - int(i)
        draw.line((x_coord, 300) + (x_coord, y_coord), width=4, fill=000)
    im.save("C:\\Users\\safwat\\PycharmProjects\\bioformatics\\22.jpg")



'''
     read image from file and conver it
'''
def red_and_convert():
    import sys, os, re
    filelist = os.listdir("C:\\Users\\safwat\\PycharmProjects\\bioformatics\\image")
    os.chdir("C:\\Users\\safwat\\PycharmProjects\\bioformatics\\image")
    for file in filelist:
        if re.search('\.db', file):
            continue
        im = Image.open(file).convert("L")
        newfile = "C:\\Users\\safwat\\PycharmProjects\\bioformatics\\bwimage\\" + file[0:-3] + ".jpg"
        newfile = str(newfile)
        im.save(newfile)