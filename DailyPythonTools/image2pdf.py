from PIL import Image
import os

def convert_images_to_pdf(folder_path):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
    
    # Create a subfolder for converted images
    output_folder = os.path.join(folder_path, "Converted_PDFs")
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg") or filename.lower().endswith(".png"):
            # Define file paths
            image_path = os.path.join(folder_path, filename)
            pdf_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".pdf")
            
            # Open and convert image
            try:
                with Image.open(image_path) as img:
                    img.convert("RGB").save(pdf_path, "PDF")
                print(f"Converted: {filename} -> {os.path.basename(pdf_path)}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    convert_images_to_pdf(folder_path)