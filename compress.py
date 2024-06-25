import os
import tinify
from env import API_KEY_TINIFY

# Replace 'YOUR_API_KEY' with your actual TinyPNG API key
tinify.key = API_KEY_TINIFY

def compress_images(input_dir, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            try:
                source = tinify.from_file(input_path)
                source.to_file(output_path)
                print(f"Compressed {input_path} and saved to {output_path}")
            except tinify.errors.AccountError:
                print("The error message returned by the API when the credentials are wrong.")
                break
            except tinify.errors.ClientError:
                print(f"Check your source image and request options for {input_path}.")
            except tinify.errors.ServerError:
                print("Temporary issue with the Tinify API.")
            except tinify.errors.ConnectionError:
                print("A network connection error occurred.")
            except Exception as e:
                print(f"An error occurred with {input_path}: {e}")

# Define input and output directories
input_directory = '/Users/aimenobrega/Downloads/ilovepdf_pages-to-jpg'
output_directory = '/Users/aimenobrega/Pictures/Gallery/mcmc'

# Compress images
compress_images(input_directory, output_directory)