"""
Extract individual product images from the products strip
"""
from PIL import Image
import os

# Load the products strip
img = Image.open('extracted_assets/layer_11_Layer_8_copy_4.png')

print(f"Products strip size: {img.width} x {img.height}")

# The strip has 5 products, let's calculate individual widths
# Looking at the strip, products are evenly spaced
# Each product card is roughly 1/5 of the width

product_width = img.width // 5
print(f"Estimated product width: {product_width}")

# Create output directory
os.makedirs('assets/products', exist_ok=True)

# Extract each product
for i in range(5):
    left = i * product_width
    right = (i + 1) * product_width
    product = img.crop((left, 0, right, img.height))
    
    filename = f'assets/products/product_{i+1}.png'
    product.save(filename)
    print(f"Saved: {filename} ({product.width}x{product.height})")

print("\nProduct extraction complete!")

