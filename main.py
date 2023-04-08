import csv
from classes import IMAGENET2012_CLASSES
import os
from label_to_id import label2id

image_dir = "./data"
# All images should be put in ./data under without any directories
# i.e. ./data
#      -- ILSVRC2012_val_00000001_n01751748.JPEG
#      -- ILSVRC2012_val_00000002_n09193705.JPEG
#      -- ...

with open("labels.csv", "w", newline='') as csv_fl:
    csv_writer = csv.writer(csv_fl, delimiter=',')
    csv_writer.writerow(["filename", "label"])

    for root, dirs, files in os.walk(image_dir):
        for filename in files:
            _, synset_id = os.path.basename(filename).rsplit("_", 1)
            synset_id = synset_id.split(".")[0]
            label = IMAGENET2012_CLASSES[synset_id]

            name = filename.split("_n")[0] + ".JPEG"
            csv_writer.writerow([name, label2id[label]])
