import ast
import os

import networkx as nx

# Directory to scan
PROJECT_ROOT = ""

# Initialize graph
dependency_graph = nx.DiGraph()


def find_imports(filepath):
    with open(filepath, "r") as file:
        tree = ast.parse(file.read(), filename=filepath)
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.append(node.module)
        return imports


# Traverse all Python files in the project directory
for root, _, files in os.walk(PROJECT_ROOT):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            module = (
                os.path.relpath(file_path, PROJECT_ROOT)
                .replace(os.sep, ".")
                .removesuffix(".py")
            )
            imports = find_imports(file_path)
            for imp in imports:
                dependency_graph.add_edge(module, imp)

# Detect circular dependencies
circular_imports = list(nx.simple_cycles(dependency_graph))

# Print results
if circular_imports:
    print("Circular imports detected:")
    for cycle in circular_imports:
        print(" -> ".join(cycle))
else:
    print("No circular imports detected.")
