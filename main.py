import tkinter as tk
from tkinter import filedialog
import ffmpeg
import eyed3

root = tk.Tk()

videoFsLable = tk.Label(text="")
imageFsLable = tk.Label(text="")

def UploadVideo(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    videoFsLable.configure(text=f"{filename}")
    
def UploadImage(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    imageFsLable.configure(text=f"{filename}")

def convert(event=None):
    print("Starting Convert")
    outputName = videoFsLable.cget("text").replace(videoFsLable.cget("text").split('.')[-1], '') + "mp3"
    stream = ffmpeg.input(videoFsLable.cget("text"))
    audio = stream.audio
    stream = ffmpeg.output(audio, outputName)
    ffmpeg.run(stream)
    print("Done")
    audiofile = eyed3.load(outputName)
    if (audiofile.tag == None):
        audiofile.initTag()
    imageFileName = imageFsLable.cget("text")
    imageFileType = imageFileName.split('.')[-1].lower()
    audiofile.tag.images.set(2, open(imageFileName,'rb').read(), f'image/{imageFileType}')
    audiofile.tag.images.set(3, open(imageFileName,'rb').read(), f'image/{imageFileType}')
    audiofile.tag.images.set(6, open(imageFileName,'rb').read(), f'image/{imageFileType}')
    audiofile.tag.save()



videoLable = tk.Label(text="Video")

imageLable = tk.Label(text="Image")

videoLable.grid(column=0, row=0)
videoButton = tk.Button(root, text='Open', command=UploadVideo)
videoButton.grid(column=1, row=0)
videoFsLable.grid(column=2, row=0)

imageLable.grid(column=0, row=1)
ImageButton = tk.Button(root, text='Open', command=UploadImage)
ImageButton.grid(column=1, row=1)
imageFsLable.grid(column=2, row=1)

submitBtn = tk.Button(root, text='Convert', command=convert)
submitBtn.grid(column=0, row=2)




root.mainloop()
