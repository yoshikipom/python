import json
from collections import OrderedDict
import sys

REMOVE_ITEM_LIST = ["remove_target1", "remove_target2"]

def remove_fields(arg):
    if isinstance(arg, list):
        for item in arg:
            remove_fields(item)
    elif isinstance(arg, dict):
        for remove_item in REMOVE_ITEM_LIST:
            if remove_item in arg:
                del(arg[remove_item])
        for value in arg.values():
            remove_fields(value)

if __name__ == '__main__':
    args = sys.argv
    path = args[1]

    with open(path) as f:
        od = json.load(f, object_pairs_hook=OrderedDict)
        remove_fields(od)
        print(json.dumps(od, indent=2, ensure_ascii=False))
