import os
import shutil

path = "C:/Users/Acer/Downloads/PDF_2009_ITIL_V3_Foundation_Complete - Upload to TEAMS FILE.pdf"
root, extension = os.path.splitext(os)
print("the root elements are ", root)
print("The extension is ", extension)
from_dir = "C:/Users/Acer/Downloads"
list_of_files = os.listdir(from_dir)
print(list_of_files)
