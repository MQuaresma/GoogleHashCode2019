import fileinput
import re

def maximize_interest(slideshow, images):
    for i in range(1, len(slideshow)-2):
        prev = slideshow[i-1][0]
        c = slideshow[i][0]
        nxt = slideshow[i+1][0]
        nxt_nxt = slideshow[i+2][0]
        before_in = interest(images[prev][1], images[c][1]) + interest(images[nxt][1], images[nxt_nxt][1])
        after_in = interest(images[prev][1], images[nxt][1]) + interest(images[c][1], images[nxt_nxt][1])
        if (after_in - before_in)>0:
            slideshow[i] = nxt
            slideshow[i+1] = c
    return slideshow


def createSlideShow(images):
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


def write_slideshow(slideshow):
    slideshow_s = [' '.join([str(img) for img in imgs]) for imgs in slideshow]
    print(str(len(slideshow_s)) + '\n' + '\n'.join(slideshow_s))


def read_imgs():
    images = []

    for line in fileinput.input():
        params = re.split(r'\s+', line)
        images.append((params[0],params[2:-1]))

    images = images[1:]
    return images

images = read_imgs()
slideshow = createSlideShow(images)
slideshow_opt = maximize_interest(slideshow, images)
write_slideshow(slideshow_opt)
