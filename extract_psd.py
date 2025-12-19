"""
Extract layers and assets from PSD file
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from psd_tools import PSDImage
import os

# Create output directory
output_dir = 'extracted_assets'
os.makedirs(output_dir, exist_ok=True)

# Load PSD file
psd = PSDImage.open('site_prototipe.psd')

print(f"PSD Size: {psd.width} x {psd.height}")
print(f"Number of layers: {len(psd)}")
print("\n" + "="*60)
print("LAYER STRUCTURE:")
print("="*60)

def safe_print(text):
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode('utf-8', errors='replace').decode('utf-8'))

def print_layer_tree(layer, indent=0):
    """Print layer tree structure"""
    prefix = "  " * indent
    layer_type = type(layer).__name__
    visible = "[V]" if layer.visible else "[H]"
    
    safe_print(f"{prefix}{visible} {layer.name} ({layer_type})")
    
    if hasattr(layer, 'bbox'):
        safe_print(f"{prefix}    Position: {layer.left}, {layer.top} - Size: {layer.width}x{layer.height}")
    
    # If it's a group, print children
    if hasattr(layer, '__iter__'):
        for child in layer:
            print_layer_tree(child, indent + 1)

# Print all layers
for layer in psd:
    print_layer_tree(layer)

print("\n" + "="*60)
print("EXTRACTING LAYERS...")
print("="*60)

def sanitize_filename(name):
    """Sanitize filename for Windows"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, '_')
    return name

def extract_layers(layer, index=0):
    """Extract all layers as images"""
    layer_name = sanitize_filename(layer.name)
    
    # Try to extract the layer as an image
    if layer.visible and layer.width > 0 and layer.height > 0:
        try:
            img = layer.composite()
            if img:
                filename = f"{output_dir}/layer_{index:02d}_{layer_name.replace(' ', '_')}.png"
                img.save(filename)
                safe_print(f"Saved: {filename} ({layer.width}x{layer.height})")
        except Exception as e:
            safe_print(f"Could not extract {layer_name}: {e}")
    
    # Process children if it's a group
    if hasattr(layer, '__iter__'):
        for i, child in enumerate(layer):
            extract_layers(child, index * 100 + i)

# Extract all layers
for i, layer in enumerate(psd):
    extract_layers(layer, i)

# Also save the full composite
print("\nSaving full composite...")
composite = psd.composite()
composite.save(f"{output_dir}/full_composite.png")
print(f"Saved: {output_dir}/full_composite.png")

print("\n" + "="*60)
print("EXTRACTION COMPLETE!")
print("="*60)
