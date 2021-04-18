from PIL import Image
import os

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst





def get_concat_h_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def get_concat_h_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_h_blank(_im, im)
    return _im

#get_concat_h_multi_blank([im1, im2, im1]).save('data/dst/pillow_concat_h_multi_blank.jpg')

def get_concat_v_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def get_concat_v_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_v_cut(_im, im)
    return _im

def get_concat_v_cut_center(im1, im2):
    dst = Image.new('RGB', (min(im1.width, im2.width), im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, ((im1.width - im2.width) // 2, im1.height))
    return dst

def get_concat_v_cut(im1, im2):
    dst = Image.new('RGB', (min(im1.width, im2.width), im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst



def get_concat_h_multi_resize(im_list, resample=Image.BICUBIC):
    min_height = min(im.height for im in im_list)
    im_list_resize = [im.resize((int(im.width * min_height / im.height), min_height),resample=resample)
                      for im in im_list]
    total_width = sum(im.width for im in im_list_resize)
    dst = Image.new('RGB', (total_width, min_height))
    pos_x = 0
    for im in im_list_resize:
        dst.paste(im, (pos_x, 0))
        pos_x += im.width
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


#def main():
    #im_list = []
    #im1 = Image.open('/tmp/0')

project_dir = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(project_dir, 'pic/')


output= os.path.join(project_dir, 'new_pic/')
def modify():
    # change dir
        os.chdir(input)
        # iterative
        for image_name in os.listdir(os.getcwd()):
            print(image_name)
            im = Image.open(os.path.join(input, image_name))
            im.thumbnail((768, 128))
            im.save(os.path.join(output, image_name))

def concatenate():
    directory = r'pic/'
    img_names = os.listdir(directory)
    #img_names.sort()
    print(type(img_names))
    img_names.sort(key=lambda x: int(x[:-4]))
    lis=[]
    for filename in img_names:
        if filename.endswith(".jpg") or filename.endswith(".png"):
            #print(os.path.join(directory, filename))
            lis.append(Image.open(os.path.join(directory,filename)))
            print(filename)
    
    return lis

# Todo(qiang): This is no program this code is strictly for debuggin the functions defined here 
if __name__ == "__main__":
    #modify()
    lis=[]
    lis = concatenate()

    #get_concat_v_multi_resize(lis).save('new_pic/mult_h_no_resize.png')
    get_concat_v_multi_blank(lis).save('new_pic/multi_blank.png')
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
