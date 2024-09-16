import os
import re

def is_jsx_code(file_content):
    # Regex pattern to detect JSX code
    jsx_pattern = re.compile(r'<[a-zA-Z][^>]*>')
    return bool(jsx_pattern.search(file_content))

def check_js_files_for_jsx(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.js'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if is_jsx_code(content):
                        new_file_path = file_path[:-3] + '.jsx'
                        os.rename(file_path, new_file_path)
                        print(f"Renamed: {file_path} to {new_file_path}")

# Replace './src' with the path to your directory
check_js_files_for_jsx('./src')