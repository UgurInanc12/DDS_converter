from PIL import Image
import os

def convert_dds_to_png(input_folder, output_folder):
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.lower().endswith(".dds"):
                input_path = os.path.join(root, filename)
                output_path = os.path.join(root, os.path.splitext(filename)[0] + ".png")

                # Open the DDS image and save it as PNG
                try:
                    img = Image.open(input_path)
                    img.save(output_path, format="PNG")
                    print(f"Converted {filename} to {output_path}")
                except Exception as e:
                    print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    input_folder2 = input("What is the location? ")
    input_folder = input_folder2.replace("\\", "\\\\")
    print(input_folder)
    convert_dds_to_png(input_folder, input_folder)  # Output files will be saved in the same directory
