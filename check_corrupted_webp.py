import os
import zipfile
from PIL import Image
import io
from pathlib import Path

def check_webp_corruption(webp_data):
    """Check if a WebP file is corrupted by trying to open it with PIL"""
    try:
        with io.BytesIO(webp_data) as bio:
            img = Image.open(bio)
            img.verify()  # Verify image integrity
        return False  # Not corrupted
    except Exception:
        return True  # Corrupted

def scan_cbz_files(root_path):
    """Scan for corrupted WebP files in CBZ archives"""
    corrupted_files = []
    root_path = Path(root_path)
    
    # Find all .cbz files recursively
    for cbz_path in root_path.rglob('*.cbz'):
        try:
            with zipfile.ZipFile(cbz_path, 'r') as zip_ref:
                # Get list of all files in the archive
                file_list = zip_ref.namelist()
                
                # Check only WebP files
                webp_files = [f for f in file_list if f.lower().endswith('.webp')]
                
                for webp_file in webp_files:
                    try:
                        # Read WebP file content without extracting
                        webp_data = zip_ref.read(webp_file)
                        
                        # Check if WebP is corrupted
                        if check_webp_corruption(webp_data):
                            corrupted_files.append(f"{cbz_path}:{webp_file}")
                    except Exception as e:
                        # If we can't read the file, consider it corrupted
                        corrupted_files.append(f"{cbz_path}:{webp_file} (Error: {str(e)})")
        
        except Exception as e:
            # If we can't open the CBZ file, log it
            corrupted_files.append(f"Error processing {cbz_path}: {str(e)}")
    
    return corrupted_files

def main():
    # Get path from command line arguments
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python check_corrupted_webp.py <path>")
        return
        
    path = sys.argv[1]
    
    # Check if path exists
    if not os.path.exists(path):
        print("Error: Path does not exist!")
        return
    
    print("Scanning for corrupted WebP files in CBZ archives...")
    corrupted_files = scan_cbz_files(path)
    
    # Write results to file
    output_file = "corrupted_webp_files.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        if corrupted_files:
            f.write("Found corrupted WebP files:\n")
            for file in corrupted_files:
                f.write(f"{file}\n")
        else:
            f.write("No corrupted WebP files found.\n")
    
    print(f"Scan complete! Results written to {output_file}")

if __name__ == "__main__":
    main() 