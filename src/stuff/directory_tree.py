
import os


def print_tree(directory, prefix=""):
    """Recursively prints the tree structure of a directory."""
    try:
        entries = sorted(os.listdir(directory))
    except PermissionError:
        print(f"{prefix}[Permission Denied]")
        return

    for i, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        connector = "└── " if i == len(entries) - 1 else "├── "
        # print(entry)
        _, extension = os.path.splitext(entry)
        if extension != ".pyc":
            if entry not in ["__pycache__"]:
                print(f"{prefix}{connector}{entry}")
        if os.path.isdir(path):
            new_prefix = "    " if i == len(entries) - 1 else "│   "
            print_tree(path, prefix + new_prefix)


if __name__ == "__main__":
    root_directory = "/Users/alexandru.campulungeanu/work/vf-tmf-sd-wan/danger_mouse"
    print(root_directory)
    print_tree(root_directory)
