import os
import re

files_lapse = ['v2/int64.js', 'v2/ps4_offsets.js', 'v2/core.js', 'v2/mem.js', 'v2/chain_lapse.js']
files_poops = ['v2/int64.js', 'v2/ps4_offsets.js', 'v2/core.js', 'v2/mem.js', 'v2/chain_poops_2.js']

def bundle(files, outfile):
    out = ['(function() {', 'const windowNEX = {};']
    for f in files:
        with open(f, 'r', encoding='utf-8') as fd:
            code = fd.read()
        
        # Strip import statements with multiline imports: import { \n a, \n b \n } from "..."
        code = re.sub(r'import\s+\{([\s\S]*?)\}\s+from\s+[\"\'].*?[\"\'];',
            lambda m: f'const {{{m.group(1)}}} = windowNEX;', code)
        
        # Handle bulk exports with potential newlines like: export { \n func1, \n func2 \n };
        code = re.sub(r'export\s+\{([\s\S]*?)\};',
            lambda m: '\n'.join([f'windowNEX.{x.strip()} = {x.strip()};' for x in m.group(1).split(',') if x.strip()]), code)
        
        # Handle default export
        code = re.sub(r'export\s+default\s+([a-zA-Z0-9_]+);?', r'windowNEX.\1 = \1;', code)
        
        # Handle exported definitions like: export function offsetsFor() ...
        exports = []
        for m in re.finditer(r'export\s+(?:function|const|let)\s+([a-zA-Z0-9_]+)', code):
            exports.append(m.group(1))
        
        # Now remove 'export '
        code = re.sub(r'export\s+(function|const|let)\s+', r'\1 ', code)
        
        # Append manual exports for those
        for e in exports:
            code += f'\nwindowNEX.{e} = {e};\n'
        
        out.append(f'// --- {f} ---')
        out.append('(function() {')
        out.append(code)
        out.append('})();')
        
    out.append('})();')
    with open(outfile, 'w', encoding='utf-8') as fd:
        fd.write('\n'.join(out))

bundle(files_lapse, 'v2/bundle_lapse.js')
bundle(files_poops, 'v2/bundle_poops.js')
print("Bundled with scoped isolation successfully!")
