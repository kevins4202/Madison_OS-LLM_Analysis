import fitz
import os
from PIL import Image
import matplotlib.pyplot as plt

def pdf_to_pngs(pdf_path, output_folder, dpi=300, display=True):
    # Open the PDF
    doc = fitz.open(pdf_path)
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    images = []

    # Iterate through each page
    for page_num in range(len(doc)):
        # Get the page
        page = doc[page_num]
        
        # Convert page to pixmap (image)
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi/72, dpi/72))
        
        # Define output PNG file name
        output_file = os.path.join(output_folder, f"page_{page_num + 1}.png")
        
        # Save the pixmap as PNG
        pix.save(output_file)
        
        print(f"Saved page {page_num + 1} as {output_file}")
        
        # Open the saved image and append to list
        if display:
            img = Image.open(output_file)
            images.append(img)
    
    # Close the document
    doc.close()
    
    print("Conversion completed.")
    
    # Display the images
    if display:
        for i, img in enumerate(images):
            plt.figure(figsize=(10, 14))
            plt.imshow(img)
            plt.axis('off')
            plt.title(f"Page {i + 1}")
            plt.show()

# Example usage
pdf_path = "../exam_pdfs/18-spring-mid.pdf"
output_folder = "output_images"
pdf_to_pngs(pdf_path, output_folder)