from PIL import Image
import os
import glob
import random
import decimal
import json



def get_concat_v_blank(im1, im2, color=(255, 255, 255)):
    w = random.randint(15, 20)
    h = random.randint(-10, -5)
    z = random.randint(30,40)
    j= random.randint(-20,-10)
    dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height), color)
    # dst = add_margin(dst,30,30,30,30,(0,0,0))
    dst.paste(im1, (0, 0))
    im2 = add_margin(im2, j, 0, h, 0, (255, 255, 255))
    dst = add_margin(dst, w, 0, 0, 0, (255, 255, 255))
    dst.paste(im2, (0, im1.height))
    return dst









def get_concat_v_cut_center(im1, im2):
    dst = Image.new('RGB', (min(im1.width, im2.width), im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, ((im1.width - im2.width) // 2, im1.height))
    return dst



def get_concat_v_multi_resize(im_list, resample=Image.BICUBIC):
    min_width = min(im.width for im in im_list)
    im_list_resize = [im.resize((min_width, int(im.height * min_width / im.width)),resample=resample)
                      for im in im_list]
    total_height = sum(im.height for im in im_list_resize)
    dst = Image.new('RGB', (min_width, total_height))
    pos_y = 0
    for im in im_list_resize:
        dst.paste(im, (0, pos_y))
        pos_y += im.height
    return dst


def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def get_concat_v_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:

        _im = get_concat_v_blank(_im, im)
    return _im


def get_concat_v_cut(im1, im2):
    dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result



def concatenate(dir):
    directory = dir
    img_names = os.listdir(directory)
    #img_names.sort()
    
    img_names.sort(key=lambda x: int(x[:-4]))
    #print(img_names)
    lis=[]
    for filename in img_names:
        if filename.endswith(".jpg") or filename.endswith(".png"):
            #print(os.path.join(directory, filename))
            lis.append(Image.open(os.path.join(directory,filename)))
            print(filename)
    
    return lis

