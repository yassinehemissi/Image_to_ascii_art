from PIL import Image
import os.path 

# setting ASCII values based on the gray scale
VALUES = {
    30:" ",
    60 :"*",
    100: "%",
    150 :"o",
    255 :"@"
}

# setting the picture new size width and heigh
W, H = 60, 30

# Calculating the gray scale (summing the rgb values and dividing by 3)
def calculate_gray_scale(pixel_rgb_values):
    pix = 0 
    for z in range(3):
            pix = pix + pixel_rgb_values[z]
    return pix / 3

# Ouput valid ASCII character (comparing to the VALUES in the upper dictionary)
def get_valid_char(gray_scale):
    for z in VALUES:
        if (gray_scale <= z):
            return VALUES[z]


def main(): 

    # Getting the picture path and checking validaty (otherwise restarting)
    path = input("insert your full image path here (should be local):")
    if not os.path.isfile(path) or not path.lower().endswith(('.png', '.jpg', '.jpeg')):
        return main()
    
    # Opening image and resizing it for better quality
    myImage = Image.open(path)
    myImage = myImage.resize((W,H))

    # Declaring the output string
    output = "\n"

    # Extracting the pixel values (which is an array of tuples that has the RGBA values of a pixel)
    pixel_values = list(myImage.getdata())

    # Extracting the output string
    for y in range(H):
        for x in range(W):
            pix = calculate_gray_scale(pixel_values[x + W * y])
            output = output + get_valid_char(pix)
        output = output + "\n"

    # Printing out
    print(output)
    
    # Restarting the script
    main()

# Starting the script
main()
