#!/usr/bin/env python3
import argparse
import os
import shutil


def main():
    args = get_arguments()
    folder_name = "day" + str(args.DayNumber)
    bootstrap_folder(folder_name)


def get_arguments() -> argparse.Namespace:
    """Gets the cli arguments"""
    parser = argparse.ArgumentParser(
        description="Bootstrap a new day based on template"
    )
    parser.add_argument("DayNumber", type=int)

    return parser.parse_args()


def bootstrap_folder(name: str):
    """Bootstrap a folder from the template if the folder doesn't exist"""
    parent_dir = os.path.dirname(__file__)
    template_dir = os.path.join(parent_dir, "template")
    dst_dir = os.path.join(parent_dir, name)
    shutil.copytree(template_dir, dst_dir, dirs_exist_ok=False)
    src = os.path.join(dst_dir, "template.py")
    dst = os.path.join(dst_dir, name + ".py")
    os.rename(src, dst)


if __name__ == "__main__":
    main()
