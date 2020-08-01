#!/usr/bin/env python3
import argparse
import json
import os

import yaml

def build_tree(source):
    tree = dict()
    source = os.path.normpath(source)
    source_parent = os.path.dirname(source)
    for root, dirs, files in os.walk(source):
        print('Building:', root)
        path = os.path.dirname(os.path.relpath(root, source_parent))
        parent = tree
        if path:
            for entry in path.split(os.path.sep):
                parent = parent[entry]
        contents = dict()
        files.remove('current_dir')
        with open(os.path.join(root, 'current_dir'), 'r', encoding='utf-8') as f:
            contents['.'] = yaml.load(f, Loader=yaml.FullLoader)
        for fname in sorted(files):
            with open(os.path.join(root, fname), 'r', encoding='utf-8') as f:
                contents[fname] = yaml.load(f, Loader=yaml.FullLoader)
        parent[os.path.basename(root)] = contents
        dirs.sort()
    return tree

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('filename')
    args = parser.parse_args()
    tree = build_tree(args.source)
    with open(args.filename, 'w', encoding='utf-8') as f:
        json.dump(tree, f, indent=4, ensure_ascii=False)
