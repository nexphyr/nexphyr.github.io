import re

def clean_code(code):
    code = re.sub(r'import\s+.*?from\s+[\"\'].*?[\"\'];?', '', code, flags=re.DOTALL)
    code = re.sub(r'export\s+\{.*?\};?', '', code, flags=re.DOTALL)
    code = re.sub(r'export\s+default\s+[a-zA-Z0-9_]+;?', '', code)
    code = re.sub(r'export\s+function\s+', 'function ', code)
    code = re.sub(r'export\s+const\s+', 'const ', code)
    code = re.sub(r'export\s+let\s+', 'let ', code)
    return code

lapse_deps = ['v2/int64.js', 'v2/ps4_offsets.js', 'v2/core.js', 'v2/mem.js', 'v2/chain_lapse.js']
poops_deps = ['v2/int64.js', 'v2/ps4_offsets.js', 'v2/core.js', 'v2/mem.js', 'v2/chain_poops_2.js']

def bundle(deps, out_file):
    bundled = ''
    for f in deps:
        with open(f, 'r', encoding='utf-8') as fd:
            bundled += f'// --- {f} ---\n'
            bundled += clean_code(fd.read()) + '\n\n'
    with open(out_file, 'w', encoding='utf-8') as fd:
        fd.write(bundled)

bundle(lapse_deps, 'v2/bundle_lapse.js')
bundle(poops_deps, 'v2/bundle_poops.js')
print('Bundled successfully!')
