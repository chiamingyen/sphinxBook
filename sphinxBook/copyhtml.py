# -*- coding: utf-8 -*-
import glob
import os.path as path
import os
import re
import shutil

TARGET = "e:\\web2py\\applications\\books"
TARGET = r"\\dell\applications\books"

copy_files = []

def copy_file(sfn, tfn):
    if not path.exists(tfn) or path.getmtime(sfn) > path.getmtime(tfn):
        copy_files.append((sfn, tfn))
    

def copy_folder(src, target, pattern):
    for sfn in glob.glob(path.join(src, pattern)):
        tfn = path.join(target, path.basename(sfn))
        copy_file(sfn, tfn)
            
def copy_all(src, target):
    for p, dirs, fns in os.walk(src):
        for fn in fns:        
            sfn = path.join(p, fn)
            tfn = target + sfn[len(src):]
            copy_file(sfn, tfn)
            
def do_copy():
    for src, target in copy_files:
        dirname = path.dirname(target)
        if not path.exists(dirname):
            os.makedirs(dirname)
        print src
        shutil.copy(src, target)
        
def copy_book(book):
    book2 = book.replace("_book", "")
    src = path.join(book, "build", "html")
    target = path.join(TARGET, "books", book2)
    copy_folder(src, target, "*.html")
    
    src1 = path.join(src, "_sources")
    target1 = path.join(target, "_sources")    
    copy_folder(src1, target1, "*.txt")
    
    src2 = path.join(src, "_images")
    target2 = path.join(TARGET, "static", "books", book2, "_images")
    copy_folder(src2, target2, "*.png")
    
    copy_folder(src, path.join(TARGET, "static", "books", book2), "*.js")
    
    src3 = path.join(book, "source", "codes")
    target3 = path.join(TARGET, "static", "books", book2, "codes")
    copy_all(src3, target3)
    
    src_cover = glob.glob(path.join(book, "source", "cover_*.png"))
    if len(src_cover) > 0:
        name = src_cover[0]
        copy_file(name, path.join(TARGET, "static", "images", "bookslogo", book.replace("_book", ".png")))
        copy_file(name, path.join(TARGET, "static", "_static", path.basename(name)))
    
if __name__ == "__main__":
    copy_all(r"exts\theme\book\static", path.join(TARGET, "static", "_static"))
    for item in glob.glob("*"):
        if item.endswith("book") and item not in ("scipy_book", "scipy2_book"):
            copy_book(item)
    do_copy()