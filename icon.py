from PIL import Image, ImageDraw

# Create a new image with a transparent background
img = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw a semi-transparent rectangle
draw.rectangle([(50, 50), (206, 206)], fill=(255, 255, 255, 128))

# Draw a border
draw.rectangle([(50, 50), (206, 206)], outline=(0, 0, 0, 255), width=2)

# Save as ICO file
img.save('notepad.ico', format='ICO') 