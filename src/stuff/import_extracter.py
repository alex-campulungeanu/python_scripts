import ast
import os

imports = []


def find_imports(filepath, f):
    with open(filepath, "r") as file:
        f.write(f"{file.name}\n")
        root = ast.parse(file.read(), filename=filepath)
        for node in ast.walk(root):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    f.write(f"import {alias.name}\n")
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imported_names = ", ".join(alias.name for alias in node.names)
                    f.write(f"from {node.module} import {imported_names}\n")
                    imports.append(f"from {node.module} import {imported_names}")
                else:
                    # Handles cases like "from . import name" (relative imports)
                    imported_names = ", ".join(alias.name for alias in node.names)
                    f.write(f"from . import {imported_names}\n")
                    imports.append(f"from . import {imported_names}")


with open("all_imports.txt", "w") as f:
    for root, dirs, files in os.walk("/home/alexc/work/vf-tmf-sd-wan/common"):
        for file in files:
            if file.endswith(".py"):
                find_imports(os.path.join(root, file), f)

# with open("all_imports.txt", "w") as f:
#     for imp in imports:
#         f.write(f"{imp}\n")
