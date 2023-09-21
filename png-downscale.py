from PIL import Image

def downscale_image(input_path, output_path, new_size):
    with Image.open(input_path) as img:
        img_resized = img.resize(new_size, Image.NEAREST)
        img_resized.save(output_path)

# Usage
downscale_image("shh-piano-v002.png", "shh-piano-v002_resized.png", (43, 43))
