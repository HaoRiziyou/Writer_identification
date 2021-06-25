from PIL import Image
import os
import glob
import random
import decimal
import json

"""
add margin success
"""

def make_tuple():
    img_list = []
    txt_list = []
    res = []
    #files = os.listdir('/home/mq/Pictures/grouting/real_db/txt_7/')

    # for filename in glob.glob('/home/mq/Pictures/grouting/real_db/txt_7/*.png'):  # assuming
    #     #print(filename)
    #     im = Image.open(filename)
    #     img_list.append(im)


    # for filename in glob.glob('/home/mq/Pictures/grouting/real_db/txt_7/*.json'):  # assuming
    #
    #     #print(filename)
    #     txt = json.load(open(filename))
    #     txt_list.append(txt)
    my_tuple=()
    file1 = glob.glob('/home/qiang/Writer_identification/data/real_db/txt_7/*.png')
    file2 = glob.glob('/home/qiang/Writer_identification/data/real_db/txt_7/*.json')
    for x in range(len(file1)):
        for y in range(len(file2)):
            if(os.path.basename(file1[x])[:-4] == os.path.basename(file2[y])[:-5]):
                my_tuple=(file1[x],file2[y])
                res.append(my_tuple)
    # print(res[0][0])
    # print(res[1][0])
    for filename in res:
        im = Image.open(filename[0])
        img_list.append(im)
        txt = json.load(open(filename[1]))
        txt_list.append(txt)
        print(filename[0],filename[1])

    #print(img_list,txt_list)


    #return my_tuple

    return img_list,txt_list








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

    #directory = "/home/qiang/Writer_identification/data/real_db/txt_7/"
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



# if __name__ == "__main__":
#     #modify()
#     img_list=[]
#     #lis = concatenate()
#     my_tuple = make_tuple()
#     dou=[]
#     for k in range(len(my_tuple[0])):
#         res = []
#         for n in range(len(my_tuple[1][k]["captions"])):
#             textline = my_tuple[0][k].crop(my_tuple[1][k]['rectangles_ltrb'][n])
#             caption = my_tuple[1][k]['captions'][n]
#             caption = caption[caption.find("@") + 1:]
#             res.append((textline, caption))
#             # textline.show()
#             # print(n)
#         dou.append((k, res))
#
#     for count, img in enumerate((dou[1][1])):
#         img_list.append(dou[1][1][count][0])
#         #dou[1][1][count][0].show()



    #get_concat_v_multi_resize(lis).save('new_pic/mult_h_no_resize.png')
    #get_concat_v_multi_blank(img_list).save('/home/mq/PycharmProjects/pythonProject1/new_pic/align.png')
    #get_concat_h_multi_resize(lis).save('pic_new/mult_h.png')
    #im1=Image.open('pic/test/0.png')
    #im2=Image.open('pic/test/1.png')
    #im3=Image.open('pic/test/2.png')
    #im4=Image.open('new_pic/mult_h.png')
    #im4=Image.open('pic/test/3.png')
    #im5=Image.open('pic/test/4.png')
    #im6=Image.open('pic/test/5.png')
    #get_concat_v_multi_resize([im1,im2,im3,im1,im4,im3]).save('new_pic/sample.png')
    #get_concat_h_multi_blank:([im1,im2,im3,im4,im5,im6]).save('new_pic/mult_blank.png')
