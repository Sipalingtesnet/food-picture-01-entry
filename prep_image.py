from PIL import Image

src_path = "/home/hatch/workspace/makefun/food-picture-01-work/media-generation-food-hero-burger-0-4c7c1495-75ce-4d6f-a2d9-c180540f01b5.png"
im = Image.open(src_path).convert("RGB")
width, height = im.size

min_dim = min(width, height)
left = (width - min_dim) // 2
top = (height - min_dim) // 2
right = left + min_dim
bottom = top + min_dim

im_cropped = im.crop((left, top, right, bottom))
im_resized = im_cropped.resize((1024, 1024), Image.Resampling.LANCZOS)

# Quantize to 256 colors to fit under 1MB while remaining RGB mode
im_quantized = im_resized.quantize(colors=256, method=Image.Quantize.MEDIANCUT).convert("RGB")
im_quantized.save("entry.png", format="PNG", optimize=True, compress_level=9)
print("Successfully generated entry.png with size 1024x1024")
