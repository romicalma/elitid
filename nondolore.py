import shutil
import os

def merge_directories(src, dest):
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dest_item = os.path.join(dest, item)
        
        if os.path.isdir(src_item):
            if not os.path.exists(dest_item):
                shutil.copytree(src_item, dest_item)
            else:
                merge_directories(src_item, dest_item)
        else:
            if not os.path.exists(dest_item):
                shutil.copy2(src_item, dest_item)
            else:
                # Handle merge logic for files
                pass
