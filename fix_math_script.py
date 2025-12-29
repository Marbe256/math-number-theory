import re
import os

def fix_math_markdown_v4(content):
    # --- 0. 下準備: ゼロ幅スペースを削除 ---
    content = content.replace('​', '')

    # --- 1. 構造的な記号 (大型記号) ---
    # シグマ記号 ∑
    content = re.sub(r'([a-z]=0)\s*\n\s*∑\s*\n\s*([m-n∞α0-9]+)', r'\\sum_{\1}^{\2}', content)

    # 組み合わせ記号 C (多桁対応) 
    # かなり限定的なパターンでマッチさせる
    content = re.sub(r'\b([m-nαk0-9]{1,3})\s*\n\s*C\s*\n\s*([p-rj0-9k]{1,3})\b', r'${}_{\1}C_{\2}$', content)

    # 二項係数 \binom ( \n k \n n \n ) -> \binom{n}{k}
    content = re.sub(r'\(\s*\n\s*([p-rj0-9k]+)\s*\n\s*([nα0-9]+)\s*\n\s*\)', r'\\binom{\2}{\1}', content)
    content = re.sub(r'\(\s*\n\s*([nα0-9]+)\s*\n\s*([p-rj0-9k]+)\s*\n\s*\)', r'\\binom{\1}{\2}', content)

    # --- 2. 特定の数学的コンテキストでの指数結合 ---
    # ()^{n}, x^{2}, n^{k} など
    # 日本語の途中の数字を吸い込まないように、対象を限定
    chars_to_sup = 'xnkpmabjr'
    for c in chars_to_sup:
        content = re.sub(rf'\b{c}\s*\n\s*([0-9rjα])\b', rf'{c}^{{\1}}', content)
    
    # 閉じ括弧の後の指数
    content = re.sub(r'\)\s*\n\s*([αn0-9rj\-\+]{1,3})\b', r')^{\1}', content)
    
    # 特殊記号
    content = re.sub(r'Δ\s*\n\s*([m-n0-9]+)', r'Δ^{\1}', content)
    content = re.sub(r'\(n\+k\)\s*\n\s*([αn0-9\-\+]+)', r'(n+k)^{\1}', content)
    content = re.sub(r'\(k\+p\)\s*\n\s*([αn0-9\-\+]+)', r'(k+p)^{\1}', content)
    content = re.sub(r'\(1[-+]1\)\s*\n\s*([m-nα]+)', r'(1-1)^{\1}', content)

    # --- 3. 微調整 ---
    # 分数などの並びを少し整理
    content = re.sub(r'([0-9][!]?)\s*\n\s*([0-9][!]?)\s*\n\s*([0-9][!]?)', r'(\1 \2 \3)', content)

    # 連続する空行を整理
    content = re.sub(r'\n{3,}', '\n\n', content)

    # 冒頭の不要なリスト（Geminiの履歴など）を削除
    lines = content.split('\n')
    if len(lines) > 20 and "Gemini" in lines[0]:
        # 「2項式」などのキーワードが出るまでスキップ
        trigger = "2項式"
        for i, line in enumerate(lines[:30]):
            if trigger in line:
                content = '\n'.join(lines[i:])
                break

    return content

file_path = r'c:\sheare\masatoyo\RONET\HP\math-number-theory\math-theory copy.md'
output_path = r'c:\sheare\masatoyo\RONET\HP\math-number-theory\math-theory_fixed.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

fixed_content = fix_math_markdown_v4(content)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(fixed_content)

print(f"Refined V4 content saved to {output_path}")
