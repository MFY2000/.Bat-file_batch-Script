from PIL import ImageTk, Image

class ImagePicker:
    def __init__(self, imagePath, width = 100, height = 100):
        imageReference = Image.open(imagePath)
        newImage = imageReference.resize((width, height))
        self.image = ImageTk.PhotoImage(newImage)
