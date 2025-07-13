import os
from PIL import Image

# 入出力フォルダ
input_folder = "images/full"
output_folder = "images/thumbs"
thumb_size = (512, 512)

# 出力フォルダがなければ作成
os.makedirs(output_folder, exist_ok=True)

# 画像ファイルを名前順で取得（.png, .jpg, .jpegなどを対象）
files = sorted([
    f for f in os.listdir(input_folder)
    if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
])

# サムネイルを順に生成
for idx, filename in enumerate(files, start=1):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, f"img{idx}_thumb.webp")

    with Image.open(input_path) as img:
        width, height = img.size
        min_edge = min(width, height)

        # 上端基準のトリミング（正方形）
        img_cropped = img.crop((0, 0, min_edge, min_edge))
        img_thumb = img_cropped.resize(thumb_size, Image.LANCZOS)

        img_thumb.save(output_path, format="WEBP")

print("✅ サムネイルの生成が完了しました。")
