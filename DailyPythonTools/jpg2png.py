from PIL import Image
import os

def convert_images(folder_path):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
    
    # Create a subfolder for converted images
    output_folder = os.path.join(folder_path, "Converted")
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            # Define file paths
            jpg_path = os.path.join(folder_path, filename)
            png_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")
            
            # Open and convert image
            try:
                with Image.open(jpg_path) as img:
                    img.save(png_path, "PNG")
                print(f"Converted: {filename} -> {os.path.basename(png_path)}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")  # ✅ Correctly placed
    convert_images(folder_path)
