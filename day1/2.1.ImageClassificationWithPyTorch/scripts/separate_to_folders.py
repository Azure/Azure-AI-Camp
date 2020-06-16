"""
Splits the single directory of images randomly into
training and validation folders based on labels for
training ML model for image classification.
"""

import os
import glob
import shutil
import random
import argparse

os.makedirs('data/train/normal', exist_ok=True)
os.makedirs('data/val/normal', exist_ok=True)
os.makedirs('data/train/suspicious', exist_ok=True)
os.makedirs('data/val/suspicious', exist_ok=True)

imglookup = {}

def arg_parse():
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser(description='Split the image data into train and val folders.')
    parser.add_argument("--dir", dest='dir', help="The base directory of images")
    return parser.parse_args()

args = arg_parse()

with open('cctvFrames_train_labels.csv') as f:
    for line in f:
        linespl = line.rstrip().split(',')
        imglookup[linespl[0]] = linespl[1]

imgfiles = glob.glob(os.path.join(args.dir, '*.jpg'))
print(len(imgfiles))

for imgf in imgfiles:
    randnum = random.choice(range(10))
    if imglookup[os.path.basename(imgf)] == '1':
        if randnum not in [0,1]:
            shutil.copyfile(imgf, 'data/train/suspicious/' + os.path.basename(imgf))
        else:
            shutil.copyfile(imgf, 'data/val/suspicious/' + os.path.basename(imgf))
    else:
        if randnum not in [0,1]:
            shutil.copyfile(imgf, 'data/train/normal/' + os.path.basename(imgf))
        else:
            shutil.copyfile(imgf, 'data/val/normal/' + os.path.basename(imgf))

if __name__ == "__main__":
    pass
