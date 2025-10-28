import streamlit as st
import ast
import os
import time
import tracemalloc
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import re
import tempfile

def extract_structure(code):
    tree = ast.parse(code)
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    return functions, classes

def benchmark_runtime(code):
    local_env = {}
    start = time.time()
    exec(code, {}, local_env)
    end = time.time()
    return end - start

def benchmark_memory(code):
    tracemalloc.start()
    exec(code)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 10**6

def safe_mutate_variables(code):
    var_names = set(re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', code))
    replacements = {v: f"{v}_mut" for v in var_names if v not in ('def', 'class', 'return', 'for', 'if', 'else')}
    for old, new in replacements.items():
        code = re.sub(rf'\b{old}\b', new, code)
    return code

def visualize_code_structure(functions, classes):
    G = nx.DiGraph()
    for cls in classes:
        G.add_node(cls, color='lightblue', shape='s')
    for func in functions:
        G.add_node(func, color='lightgreen', shape='o')
    for cls in classes:
        for func in functions:
            G.add_edge(cls, func)
    colors = [G.nodes[n]['color'] for n in G.nodes]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=2000, font_size=10)
    st.pyplot(plt)

st.title("Ultimate Python Code Insight Lab")
uploaded_files = st.file_uploader("Upload Python script(s)", accept_multiple_files=True, type="py")

if uploaded_files:
    results = []
    for uploaded_file in uploaded_files:
        code = uploaded_file.read().decode()
        functions, classes = extract_structure(code)
        runtime = benchmark_runtime(code)
        memory = benchmark_memory(code)
        mutated_code = safe_mutate_variables(code)
        results.append({
            'Script': uploaded_file.name,
            'Functions': ', '.join(functions),
            'Classes': ', '.join(classes),
            'Runtime (s)': round(runtime, 4),
            'Memory (MB)': round(memory, 4)
        })
        st.subheader(f"Code Structure for {uploaded_file.name}")
        st.write("Functions:", functions)
        st.write("Classes:", classes)
        st.write("Original Code")
        st.code(code, language='python')
        st.write("Mutated Code")
        st.code(mutated_code, language='python')
        st.write("Visualization")
        visualize_code_structure(functions, classes)
    st.subheader("Benchmark Summary")
    df = pd.DataFrame(results)
    st.dataframe(df)
