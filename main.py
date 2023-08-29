import cv2

def sharpen(image):
    # Define parameters for the Laplacian filter
    ddepth = cv2.CV_16S  # Data depth for intermediate calculations
    kernel_size = 3      # Size of the Laplacian kernel

    # Apply Gaussian blur to the input image to reduce noise
    blur_image = cv2.GaussianBlur(image, (3, 3), 0)

    # Apply Laplacian filter to the blurred image
    laplacian_image = cv2.Laplacian(blur_image, ddepth, ksize=kernel_size)

    # Calculate sharpened image by subtracting Laplacian from blurred image
    sharpened_image = blur_image + (-1) * laplacian_image

    # Convert the images to absolute scale (0-255)
    abs_blur = cv2.convertScaleAbs(blur_image)
    abs_laplacian = cv2.convertScaleAbs(laplacian_image)
    abs_sharpen = cv2.convertScaleAbs(sharpened_image)

    # Save the images
    cv2.imwrite("original.png", image)
    cv2.imwrite("blurred.png", abs_blur)
    cv2.imwrite("laplacian_filter.png", abs_laplacian)
    cv2.imwrite("result.png", abs_sharpen)


if __name__ == '__main__':
    image = cv2.imread("moon.jpg", 0)
    sharpen(image)