import fitz  # PyMuPDF

def pdf_to_png(pdf_path, output_folder):
    # Deschide PDF-ul
    pdf_document = fitz.open(pdf_path)

    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        
        # Setăm rezoluția imaginii (scalare mare pentru calitate)
        zoom = 2.0  # 2x scaling
        mat = fitz.Matrix(zoom, zoom)

        # Redenumește fiecare pagină
        output_path = f"{output_folder}/pagina_{page_number + 1}.png"
        
        # Salvează ca imagine
        pix = page.get_pixmap(matrix=mat)
        pix.save(output_path)
        print(f"Pagina {page_number + 1} salvată în {output_path}")
    
    pdf_document.close()
    print("Conversia s-a terminat cu succes!")

# Exemplu de utilizare
pdf_path = "document.pdf"  # Calea către PDF-ul tău
output_folder = "./imagini"  # Folderul de ieșire
pdf_to_png(pdf_path, output_folder)
