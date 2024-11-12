import ast
import os


class InitArgCounter(ast.NodeVisitor):
    def __init__(self):
        self.init_methods = []

    def visit_FunctionDef(self, node):
        if node.name == "__init__":
            # Subtract one to exclude 'self' from the count
            arg_count = len(node.args.args) - 1
            self.init_methods.append((node.lineno, arg_count))
        self.generic_visit(node)


def count_init_args_in_file(filepath):
    with open(filepath, encoding="utf-8") as file:
        file_content = file.read()
    tree = ast.parse(file_content)
    counter = InitArgCounter()
    counter.visit(tree)
    return counter.init_methods


def count_init_args_in_project(project_path, excludes):
    init_methods_info = []
    for root, dirs, files in os.walk(project_path):
        # Skip the .env directory
        if not root.startswith(tuple(excludes)):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    file_init_methods = count_init_args_in_file(filepath)
                    for lineno, arg_count in file_init_methods:
                        init_methods_info.append((filepath, lineno, arg_count))
    return init_methods_info


if __name__ == "__main__":
    project_path = ""  # Replace with your project path
    exception_list = [f"{project_path}/env"]
    init_methods_info = count_init_args_in_project(project_path, exception_list)
    for filepath, lineno, arg_count in init_methods_info:
        if arg_count > 4:
            print(
                f"File: {filepath}, Line: {lineno}, __init__ arguments (excluding 'self'): {arg_count}"
            )
