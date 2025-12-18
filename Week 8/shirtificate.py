def main():
    # Prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate with their name on it
    name = input("Name: ")
    generate_shirtificate(name)

# The orientation of the PDF should be portrait
# The format of the PDF should be A4, which is 210mm wide by 297mm tall
# The top the PDF should say "CS50 Shirtificate" as text, centered horizontally and vertically
# The user's name should be on top of the shirt, in white text.
def generate_shirtificate(name):
    from fpdf import FPDF

    # Create a new PDF document
    pdf = FPDF()
    pdf.add_page()

    # Set the font to Arial, bold, and size 24
    pdf.set_font("Arial", "B", 24)

    # Add the CS50 shirt text to the PDF
    pdf.cell(0, 10, "CS50 Shirtificate", align="C")

    # Set the font to Arial, regular, and size 16
    pdf.set_font("Arial", "", 16)

    # Add the user's name to the PDF
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    # Save the PDF to a file
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()