import re
import os

def fix_math_content(content):
    # 1. Standardize minus signs and weird characters
    content = content.replace('−', '-')
    content = content.replace('⋅', r'\cdot')
    content = content.replace('…', r'\dots')
    
    # 2. Fix broken math splits
    lines = content.split('\n')
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Detect fragmented math lines
        # Signs of math: presence of ^, _, {, }, \sum, \binom, C, or starting/ending with $
        is_math_fragment = (
            stripped.startswith('$') or 
            stripped.endswith('$') or 
            '^{ ' in stripped or 
            '_{ ' in stripped or
            re.search(r'[a-zA-Z0-9]\^[a-zA-Z0-9]', stripped) or
            re.search(r'[a-zA-Z0-9]_[a-zA-Z0-9]', stripped) or
            stripped == '+' or stripped == '=' or stripped == '-'
        )
        
        if is_math_fragment and not stripped.startswith('#'):
            merged_math = stripped
            j = i + 1
            while j < len(lines) and j < i + 15:
                next_stripped = lines[j].strip()
                if not next_stripped:
                    # Allow one empty line between fragments if it seems they continue
                    if j + 1 < len(lines):
                        nn_stripped = lines[j+1].strip()
                        if nn_stripped.startswith('$') or nn_stripped.endswith('$') or nn_stripped.startswith('+') or nn_stripped.startswith('='):
                            j += 1
                            continue
                    break
                
                # If next line looks like more math or a connector
                is_next_math = (
                    next_stripped.startswith('$') or 
                    next_stripped.endswith('$') or 
                    next_stripped.startswith('+') or 
                    next_stripped.startswith('=') or 
                    next_stripped.startswith('-') or
                    '^' in next_stripped or
                    '_' in next_stripped or
                    '\\' in next_stripped
                )
                
                if is_next_math:
                    merged_math += " " + next_stripped
                    j = j + 1
                else:
                    break
            
            # Clean up redundant dollars
            merged_math = merged_math.replace('$$', '##DBL##').replace('$', '').replace('##DBL##', '$$')
            
            # Re-wrap properly
            if merged_math.startswith('$$'):
                if not merged_math.endswith('$$'):
                    merged_math += ' $$'
            else:
                merged_math = f"$ {merged_math.strip()} $"
                
            # Final touch: fix the \tag usage
            merged_math = re.sub(r'\\tag\{(\d+)\}', r'\\quad (\1)', merged_math)
            
            new_lines.append(merged_math)
            i = j
        else:
            new_lines.append(line)
            i += 1
            
    return '\n'.join(new_lines)

def main():
    path = r'c:\sheare\masatoyo\RONET\HP\math-number-theory\math-theory_fixed.md'
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
        
    print(f"Reading {path}...")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    print("Fixing math content...")
    fixed_content = fix_math_content(content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    print("Optimization complete.")

if __name__ == "__main__":
    main()
