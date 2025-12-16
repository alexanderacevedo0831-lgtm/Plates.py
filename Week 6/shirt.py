import sys
import os
from PIL import Image, ImageOps


def main():
    # Must have exactly 2 command line arguments
    if len(sys.argv) != 3: 
        sys.exit("Too few/many command-line arguments")

    infile = sys.argv[1]
    outfile = sys.argv[2]

    # The input and output files must end in .jpg, .jpeg, or .png, case insensitive
    valid_extensions = (".jpg", ".jpeg", ".png")
    
    if not infile.lower().endswith(valid_extensions):
        sys.exit("Invalid input file")

    if not outfile.lower().endswith(valid_extensions):
        sys.exit("Invalid output file")

    # Infile must exist
    if not os.path.exists(infile):
        sys.exit("File does not exist")

    # The input's name must have the same extension as the output's name
    infile_extension = os.path.splitext(infile)[1].lower()
    outfile_extension = os.path.splitext(outfile)[1].lower()

    if infile_extension != outfile_extension:
        sys.exit("Input and output have different extensions")

    # Overlay shirt.png on the input image and save as the output image
    # (After resizing and cropping the input to be the same size, saving the result as its output)

    shirt = Image.open("shirt.png")

    # Open and fit the input image to shirt size
    with Image.open(infile) as im:
        fitted = ImageOps.fit(im, shirt.size)

        # Overlay shirt.png using paste with mask
        fitted.paste(shirt, shirt)

        # Save the result as the output image
        fitted.save(outfile)

if __name__ == "__main__":
    main()