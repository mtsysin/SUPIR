import cv2
import numpy as np
import argparse
import os

def process_image(input_path, output_path, noise_mean, noise_std, blur_ksize):
    """
    Loads an image, adds noise, applies Gaussian blur, and saves the result.
    
    Args:
        input_path: Path to the input image.
        output_path: Path to save the processed image.
        noise_mean: Mean of the Gaussian noise.
        noise_std: Standard deviation of the Gaussian noise.
        blur_ksize: Kernel size for Gaussian blur (must be odd).
    """
    # Load image
    image = cv2.imread(input_path)
    if image is None:
        raise ValueError(f"Error: Image not found or unable to load: {input_path}")
    
    # Add Gaussian noise
    noise = np.random.normal(noise_mean, noise_std, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(noisy_image, (blur_ksize, blur_ksize), 0)
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save processed image
    cv2.imwrite(output_path, blurred_image)
    print(f"Processed image saved at {output_path}")

def process_directory(input_dir, output_dir, noise_mean, noise_std, blur_ksize):
    """Processes every image in a file structure and saves results to the same structure."""
    assert os.path.exists(input_dir), f"Input directory does not exist: {input_dir}, current direcory: {os.getcwd()}"
    for root, _, files in os.walk(input_dir):
        print(root)
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                process_image(input_path, output_path, noise_mean, noise_std, blur_ksize)

#TODO: add some more types of degradations

# Driver code
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images by adding noise and applying Gaussian blur.")
    parser.add_argument("--input_dir", type=str, required=True, help="Path to the input directory containing images.")
    parser.add_argument("--output_dir", type=str, required=True, help="Path to save the processed images.")
    parser.add_argument("--noise_mean", type=float, default=0, help="Mean of the Gaussian noise.")
    parser.add_argument("--noise_std", type=float, default=25, help="Standard deviation of the Gaussian noise.")
    parser.add_argument("--blur_ksize", type=int, default=5, help="Kernel size for Gaussian blur (must be odd).")
    
    args = parser.parse_args()
    print(f"Input directory: {args.input_dir}")
    process_directory(args.input_dir, args.output_dir, args.noise_mean, args.noise_std, args.blur_ksize)


# Sample usage:
# python degrade.py --input_dir ./test_data/orginal --output_dir ./test_data/degraded --noise_mean 0 --noise_std 25 --blur_ksize 5
