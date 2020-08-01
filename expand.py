#!/usr/bin/env python3
import argparse
import json
import os

import yaml

def expand(node, dest, path=None, fail_ok=False):
    if path:
        current = os.path.join(dest, path)
        if '.' not in node:
            with open(os.path.join(dest, path), 'x', encoding='utf-8') as f:
                yaml.dump(node, f, allow_unicode=True, sort_keys=False)
            return
        os.mkdir(current)
    for name, node in node.items():
        if name == '.':
            name = 'current_dir'
        child = os.path.join(path, name) if path else name
        try:
            expand(node, dest, child, fail_ok)
        # on Windows, opening "CON" for exclusive creation raises ValueError
        except (OSError, ValueError):
            print('\033[31mUnable to create:', child, '\033[0m')
            if fail_ok:
                continue
            raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('destination')
    args = parser.parse_args()
    with open(args.filename, 'r', encoding='utf-8') as f:
        root = json.load(f)
    if os.name == 'nt':
        os.system('color')
        print('\033[33mWindows places many restrictions on filenames.',\
            'Please use WSL to avoid missing files.\033[0m')
        expand(root, args.destination, fail_ok=True)
    else:
        expand(root, args.destination)
