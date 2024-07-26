from PIL import Image
from rembg import remove

def remove_background(image_path, output_path):
    try:
        input_image = Image.open(image_path)
        
        output_image = remove(input_image)
        
        output_image.save(output_path)
        
        print(f"Background removed and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_image_path = "input/image.jpeg"
    output_image_path = "output/image.png"
    
    remove_background(input_image_path, output_image_path)
