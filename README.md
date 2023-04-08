# ImageNet-Validation-labels

The repo is used to get the labels of images in __ILSVRC2012 validation set__.

All images should be put in ./data under without any directories, 
i.e.
```
./data
-- ILSVRC2012_val_00000001_n01751748.JPEG
-- ILSVRC2012_val_00000002_n09193705.JPEG
-- ...
```
(Only one image is saved in the directory now, to keep the directory reserved in the git repo.)

Just directly run
``` bash
    python main.py
```
and the result will be saved in __./labels.csv__.

__labels.csv__
```
filename,label
ILSVRC2012_val_00047905.JPEG,495
ILSVRC2012_val_00002304.JPEG,744
...
```

I thought it's very easy to get the labels at first, but it did took me some time. Therefore, in case I need to do it again in the future or someone else needs to do the same thing, I put the useful data and scripts here in the repo.