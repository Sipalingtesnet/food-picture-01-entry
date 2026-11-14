from PIL import Image
from pathlib import Path

source_path = Path("/home/hatch/workspace/makefun/food-picture-01-work/media-generation-food-hero-ramen-pull-v2-0-16e6e6ac-2a5f-4a80-b18a-8785b7cc309a.webp")
output_path = Path("entry.png")

img = Image.open(source_path).convert("RGB")
# Target dimensions: 683x1024 portrait (within 1024x1024 max dimension limit)
img = img.resize((683, 1024), Image.Resampling.LANCZOS)
img = img.quantize(colors=256, method=Image.Quantize.MEDIANCUT).convert("RGB")
img.save(output_path, format="PNG", optimize=True, compress_level=9)
print(f"Successfully processed {source_path} to {output_path} with size {img.size}")
