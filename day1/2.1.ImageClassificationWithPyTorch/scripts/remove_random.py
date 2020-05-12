import numpy as np
import argparse
import glob
import shutil
import os


if __name__ == "__main__":

    # Argument
    parser = argparse.ArgumentParser(description='This script deletes half of the images in a directory randomly')
    parser.add_argument("--dir", dest='dir', help="The directory of images from which to delete random images")
    args = parser.parse_args()

    # Image files
    imgfiles = glob.glob(os.path.join(args.dir, 'normal', '*.jpg'))
    imgfiles.extend(glob.glob(os.path.join(args.dir, 'suspicious', '*.jpg')))

    # Choose random images
    choice_array = np.random.randint(low=0, high=2, size=len(imgfiles))
    imgfiles_to_delete = [imgfiles[i] for i,choice in enumerate(choice_array) if choice == 1]
    print('Total files = ', len(imgfiles))
    print('Deleting ', len(imgfiles_to_delete), ' files')

    for img in imgfiles_to_delete:
        os.remove(img)
