from PIL import Image

# Load the PNG image
img = Image.open('assets/logo/invisiblepad logo.png')

# Save as ICO file. Resize to a common icon size if necessary. Windows icons often use 16x16, 32x32, 48x48, 256x256.
# For simplicity, let's resize to 256x256 for now, as it's a common larger size for modern icons.
img = img.resize((256, 256), Image.Resampling.LANCZOS)
img.save('invisiblepad_logo.ico', format='ICO') 