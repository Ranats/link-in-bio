import os
from PIL import Image

# 入力フォルダと出力フォルダ（上書きなら同じでもOK）
input_dir = 'assets/full'
output_dir = 'assets/full_webp'
os.makedirs(output_dir, exist_ok=True)

# .pngファイル一覧（ソート付き）
png_files = sorted([f for f in os.listdir(input_dir) if f.lower().endswith('.png')])

# 変換処理
for idx, filename in enumerate(png_files, start=1):
    img_path = os.path.join(input_dir, filename)
    img = Image.open(img_path).convert('RGB')  # WebPはRGBで保存

    output_filename = f'img{idx}.webp'
    output_path = os.path.join(output_dir, output_filename)

    img.save(output_path, 'webp', quality=95)
    print(f"Saved {output_filename}")

print("✅ 全ファイルをWebPに変換し、連番で保存しました。")
