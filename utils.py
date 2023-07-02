import os
import glob
import random
import pathlib
from shutil import copyfile

def erase_old_images(path):
    files = glob.glob(f'{path}/*/*')
    for file in files:
        os.remove(file)

def balance_dataset(up, down, ground):
    up_list = os.listdir(up)
    down_list = os.listdir(down)
    ground_list = os.listdir(ground)

    min_size = min(len(up_list), len(down_list), len(ground_list))

    up_sample = random.sample(up_list, min_size)
    down_sample = random.sample(down_list, min_size)
    ground_sample = random.sample(ground_list, min_size)
    
    
    for (subset, lst, path) in [(up_sample, up_list, up), (down_sample, down_list, down), (ground_sample, ground_list, ground)]:
        if (len(lst) == min_size):
            continue

        for sample in lst:
            if sample not in subset:
                p = os.path.join(path, sample)
                os.remove(p)

def split_images(source, train, test, test_size=0.1):
    # creating dirs if not exist
    pathlib.Path(train).mkdir(parents=True, exist_ok=True)
    pathlib.Path(test).mkdir(parents=True, exist_ok=True)

    images = os.listdir(source)
    random.shuffle(images)

    split = int(len(images) * test_size)

    # copy training part
    for image in images[split:]:
        src = os.path.join(source, image)
        dst = os.path.join(train, image)
        copyfile(src, dst)

    # copy testing part
    for image in images[:split]:
        src = os.path.join(source, image)
        dst = os.path.join(test, image)
        copyfile(src, dst)

    print(f'# training images: {len(os.listdir(train))}')
    print(f'# test images: {len(os.listdir(test))}\n')
