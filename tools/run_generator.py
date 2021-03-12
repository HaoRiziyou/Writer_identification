#!/usr/bin/env python3
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

import fargv

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
    #-input ./docs/img/input.png -text_in 'above or sinking bellow' -text_out 'hello world'
    params={'text_in':'above or sinking bellow','text_out':'hello world' , 'output':'/tmp/','input':'./docs/img/input.png', 'plot':False}
    args, _ = fargv.fargv(params)

    inputImg = Image.open(args.input)

    with Skeletonizer() as skeletonizer:
        skeletonBlurImg = skeletonizer.skeletonize_blurred(inputImg)
        skeletonImg = skeletonizer.skeletonize_sharp(skeletonBlurImg)

    penPositions = sample_to_penpositions(skeletonImg)
    with GravesWriter() as writer:
        for n, text_out in enumerate(args.text_out.split('\n')):
            newPenPositions = writer.write(text_out, args.text_in, penPositions)
            newPenPositions = align(newPenPositions, penPositions)
            newSkeletonBlurImg, newSkeletonImg = render_skeleton(newPenPositions, inputImg.size)
            with PenStyleTransfer() as penStyleTransfer:
                outputImg = penStyleTransfer.transferStyle(newSkeletonBlurImg, inputImg)
            if args.plot:
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
            output_path = f"{args.output}/{n}.png"
            print(f"saving in {output_path} text:'{text_out}'" )
            outputImg.save(output_path)


if __name__ == "__main__":
    main()
    









