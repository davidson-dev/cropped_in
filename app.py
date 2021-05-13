from tkinter import *
from tkinter import filedialog
from PIL import Image

#  dialog window to select the image
root = Tk()
root.title("Cropped_in")
root.filename = filedialog.askopenfilename(initialdir="/your_image_folder_directory",
                                           title="Cropped_in - Choose an image",
                                           filetypes=(("jpg files", "*.jpg"), ("png files", "*.png")))

# image path to open
filepath = root.filename
img = Image.open(filepath)
new_size = img.resize((1584, 396))
new_size.show()
new_size.save("cropped_image.jpg")
root.mainloop()

