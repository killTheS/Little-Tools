#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys

def getContent(filepath):
    path_pair = filepath.rsplit('/',maxsplit=1)
    with open(path_pair[0] + "/Cont_" + path_pair[1]+ ".md", mode='w') as op: 
        print("[TOC]", file=op)
        listdir(filepath,output=op)

    
def listdir(path, deep=0,output="/Users/apple/PycharmProjects/test/getFL_buf.txt"):
    print('#' * (deep + 1) + os.path.split(path)[1],file=output)
    dir_list = sorted(os.listdir(path))
    deep += 1
    for item in dir_list:
        item_path = path + '/' + item
        if os.path.isdir(item_path):
            listdir(item_path, deep,output)
        elif '.DS_Store' not in item:
            print(' ' * deep + '+ [' + item + '](' + item_path + ')', file=output)

      
getContent('sys.argv[1])


