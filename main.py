import fileinput
import re

images = []

def createSlideShow():
    slideshow = []
    lastV = -1
    
    for i in range(0, len(images)):
        if images[i][0] == 'H':
            slideshow.append([i])
        else:
            if lastV != -1:
                slideshow.append([lastV, i])
                lastV = -1
            else:
                lastV = i
    
    return slideshow

for line in fileinput.input():
    params = re.split(r'\s+', line)
    images.append((params[0],params[2:-1]))

images = images[1:]

slideshow = createSlideShow()
slideshow_s = [' '.join([str(img) for img in imgs]) for imgs in slideshow]

print(str(len(slideshow_s)) + '\n' + '\n'.join(slideshow_s))