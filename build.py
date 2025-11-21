import os
import re
import base64

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def bundle():
    print("Bundling dashboard...")
    
    if not os.path.exists('index.html'):
        print("Error: index.html not found")
        return

    html = read_file('index.html')
    
    # 1. Inline CSS
    print("Inlining CSS...")
    css_path = 'assets/css/style.css'
    if os.path.exists(css_path):
        css_content = read_file(css_path)
        html = html.replace(f'<link rel="stylesheet" href="{css_path}">', f'<style>{css_content}</style>')
    else:
        print(f"Warning: {css_path} not found")

    # 2. Inline JS
    print("Inlining JS...")
    js_files = ['assets/js/dashboard.js', 'assets/js/charts.js']
    for js_file in js_files:
        if os.path.exists(js_file):
            js_content = read_file(js_file)
            html = html.replace(f'<script src="{js_file}"></script>', f'<script>{js_content}</script>')
        else:
            print(f"Warning: {js_file} not found")

    # 3. Inline Favicon
    print("Inlining Favicon...")
    if os.path.exists('favicon.ico'):
        with open('favicon.ico', 'rb') as f:
            favicon_b64 = base64.b64encode(f.read()).decode('utf-8')
        html = html.replace('href="favicon.ico"', f'href="data:image/x-icon;base64,{favicon_b64}"')

    # 4. Basic Cleanup (Remove comments)
    # Be careful not to remove conditional comments or important markers if any
    html = re.sub(r'<!--(.*?)-->', '', html, flags=re.DOTALL)

    # Output
    os.makedirs('dist', exist_ok=True)
    output_path = 'dist/index.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Build complete! Output: {output_path}")

if __name__ == '__main__':
    bundle()
