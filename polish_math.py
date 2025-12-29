import re
import os

def final_polish(content):
    # 1. 指数の追加修正 (3x \n 2 -> 3x^2 など)
    # 数字+英字 の後の改行指数を結合
    content = re.sub(r'([0-9][a-zA-Z])\s*\n\s*([0-9rjα])\b', r'\1^{\2}', content)
    
    # 2. 依然として残っている単独の数字行を、前の行の末尾が変数なら指数として結合
    # ただし慎重に行う
    content = re.sub(r'([xnkpma])\s*\n\s*([0-9])\s*\n', r'\1^{\2}\n', content)

    # 3. 冒頭の重複したタイトルやメタ情報の整理
    lines = content.split('\n')
    if len(lines) > 10:
        # 最初の数行が同じタイトルの繰り返しなら整理
        # 17行目の「2項式を示して」あたりからが本編
        new_start = 0
        for i, line in enumerate(lines[:20]):
            if "2項式を示して" in line:
                new_start = i
                break
        if new_start > 0:
            content = '\n'.join(lines[new_start:])

    return content

file_path = r'c:\sheare\masatoyo\RONET\HP\math-number-theory\math-theory_fixed.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

polished_content = final_polish(content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(polished_content)

print(f"Final polish completed on {file_path}")
