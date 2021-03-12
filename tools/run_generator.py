#!/usr/bin/env python3

import argparse
import os

from PIL import Image

import numpy as np
import matplotlib.pyplot as plt

from pipeline.skeletonization import Skeletonizer
from pipeline.sampling import sample_to_penpositions
from pipeline.graves import GravesWriter
from pipeline.align import align
from pipeline.render_skeleton import render_skeleton
from pipeline.pen_style_transfer import PenStyleTransfer

from datastructures.PenPosition import plotPenPositions




def main():

    parser = argparse.ArgumentParser(description='run the generator to genrate the synthesis data')
    parser.add_argument('--text-in', help='The input text', required=True)
    parser.add_argument('--text-out', help='The output text', required=True)
    #parser.add_argument('-output',help = "output dir")
    parser.add_argument('input', help='The input file')
    #parser.add_argument('-skeleton',default='pix2pix',help="skeleton")
    args = parser.parse_args()
    print(args)

    inputImg = Image.open(args.input)

    with Skeletonizer() as skeletonizer:
        skeletonBlurImg = skeletonizer.skeletonize_blurred(inputImg)
        skeletonImg = skeletonizer.skeletonize_sharp(skeletonBlurImg)

    penPositions = sample_to_penpositions(skeletonImg)

    with GravesWriter() as writer:
        newPenPositions = writer.write(args.text_out, args.text_in, penPositions)

    newPenPositions = align(newPenPositions, penPositions)

    newSkeletonBlurImg, newSkeletonImg = render_skeleton(newPenPositions, inputImg.size)

    with PenStyleTransfer() as penStyleTransfer:
        outputImg = penStyleTransfer.transferStyle(newSkeletonBlurImg, inputImg)

    print("Done. Displaying results ...")

    plt.figure('Full Pipeline', figsize=(16, 9))
    plt.subplot(3, 2, 1)
    plt.imshow(inputImg)
    plt.subplot(3, 2, 3)
    plt.imshow(skeletonBlurImg)
    plt.subplot(3, 2, 5)
    plt.imshow(skeletonImg, cmap='binary', vmax=10)
    plotPenPositions(penPositions)
    plt.subplot(3, 2, 6)
    plt.imshow(newSkeletonImg, cmap='binary', vmax=256*10)
    plotPenPositions(newPenPositions)
    plt.subplot(3, 2, 4)
    plt.imshow(newSkeletonBlurImg)
    plt.subplot(3, 2, 2)
    plt.imshow(outputImg)
    plt.show()
    
    print("save progress")
    #outputImg.save(args.output,'tif')


if __name__ == "__main__":
    main()
    
    
# #!/usr/bin/env python3
# import fargv

# params = {
    # "anInt": 1,
    # "aFloat": 0.1,
    # "aBoolean": False,
    # "aString": "Hello",
    # "aStringReference": "{aString} World",
    # "anIntWithHelp": [2, "This would be the help"],
    # "aChoice": [("choice1", "choice2", "choice3", "choice4"), "And this must be the help"],
    # "aPositionalSwitch": [set([]), "Space separated filenames is a good example of what goes here."]
# }

# if __name__ == "__main__":
    # new_params, help_str = fargv.fargv(params)
    # for k, v in params.items():
        # print(k, repr(v), "->", repr(new_params[k]))

