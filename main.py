from PIL import Image
import svgwrite

def png_to_svg(png_path, svg_path):
    img = Image.open(png_path)
    pixels = img.load()
    width, height = img.size

    dwg = svgwrite.Drawing(svg_path, size=(width, height))
    
    for y in range(height):
        for x in range(width):
            color = pixels[x, y]
            if color[3] == 0:  # Skip transparent pixels
                continue
            
            hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            dwg.add(dwg.rect(insert=(x, y), size=(1, 1), fill=hex_color))
    
    dwg.save()

# Usage
png_to_svg("pixel_art.png", "pixel_art.svg")
