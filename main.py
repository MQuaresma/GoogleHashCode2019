#!/usr/bin/env python3

from random import randint, uniform
from math import exp
import fileinput
import re

def interest(tags1, tags2):
    commons = 0
    s1 = 0
    s2 = 0

    for t1 in tags1:
        flag = False
        s1 += 1
        for t2 in tags2:
            if t1==t2:
                flag = True
                break
        if flag:
            commons += 1

    s1 -= commons
    s2 = len(tags2) - commons

    return min([s1,s2,commons])

def maximize_interest(slideshow, images):
    T=1
    if len(slideshow)>3:
        j=0
        while j<10000:
            for i in range(1, len(slideshow)-2):
                prev = slideshow[i-1][1]
                c = slideshow[i][1]
                nxt = slideshow[i+1][1]
                nxt_nxt = slideshow[i+2][1]
                before_in = interest(prev, c) + interest(nxt, nxt_nxt)
                after_in = interest(prev, nxt) + interest(c, nxt_nxt)
                delta = after_in - before_in
                if (delta>0) or (T>= 0.000001 and exp(delta/T)>=uniform(0,1)):
                    prev = slideshow[i]
                    slideshow[i] = slideshow[i+1]
                    slideshow[i+1] = prev
                    if delta != 0:
                        j=0
                else:
                    j += 1
            T = 0.999*T
    return slideshow

def findV(images, ind):
    min = 1000
    i_min = -1
    for i in range(0, len(images)):
        if images[i][0] == 'V':
            intersect_value = len(list(set(images[ind][1]) & set(images[i][1])))
            if intersect_value == 0:
                i_min = i
                break  
            if intersect_value < min: 
                min = intersect_value
                i_min = i

    return i_min

def createSlideShow(images):
    slideshow = []
    
    for i in range(0, len(images)):
        if images[i][0] == 'H':
            slideshow.append([[i], images[i][1]])
        elif images[i][0] == 'V':
            images[i][0] = 'N'
            v = findV(images,i)
            if v != -1:
                images[v][0] = 'N'
                slideshow.append([[v, i], list(set(images[v][1] + images[i][1]))])
                
    return slideshow


def write_slideshow(slideshow):
    slideshow_s = [' '.join([str(img) for img in imgs[0]]) for imgs in slideshow]
    print(str(len(slideshow_s)) + '\n' + '\n'.join(slideshow_s))


def read_imgs():
    images = []

    for line in fileinput.input():
        params = re.split(r'\s+', line)
        images.append([params[0],params[2:-1]])

    images = images[1:]
    return images

images = read_imgs()
slideshow = createSlideShow(images)
slideshow_opt = maximize_interest(slideshow, images)
write_slideshow(slideshow_opt)
