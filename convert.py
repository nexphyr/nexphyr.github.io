import re, glob

for file in glob.glob('v2/*.js'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    # Remove imports
    content = re.sub(r'import\s+.*?from\s+[\"\'].*?[\"\'];?', '', content, flags=re.DOTALL)
    # Remove multi-line exports
    content = re.sub(r'export\s+\{.*?\};?', '', content, flags=re.DOTALL)
    # Convert export function to function
    content = re.sub(r'export\s+function', 'function', content)
    # Convert export const to const
    content = re.sub(r'export\s+const', 'const', content)
    # Remove export default
    content = re.sub(r'export\s+default\s+.*?;?', '', content)

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Converted {file}')
