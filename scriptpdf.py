import fitz  # PyMuPDF

def pdf_to_png(pdf_path, output_folder):
    # Deschide PDF-ul
    pdf_document = fitz.open(pdf_path)

    # Parcurge fiecare pagină din PDF
    for page_number in range(len(pdf_document)):
        print(f"Processing page {page_number + 1}...")  # Mesaj de debug
        
        page = pdf_document.load_page(page_number)
        
        # Setăm rezoluția imaginii (zoom pentru calitate mai mare)
        zoom = 4.0  # 4x scaling pentru claritate
        mat = fitz.Matrix(zoom, zoom)

        # Redenumește fiecare pagină ca imagine PNG
        output_path = f"{output_folder}/pagina_{page_number + 1}.png"
        
        # Salvează imaginea
        pix = page.get_pixmap(matrix=mat)
        pix.save(output_path)
        print(f"Pagina {page_number + 1} salvată în {output_path}")
    
    pdf_document.close()
    print("Conversia s-a terminat cu succes!")

# Exemplu de utilizare
pdf_path = "C:/Users/alexa/proiectul_meu/document.pdf"  # Calea completă către PDF-ul tău
output_folder = "./imagini"  # Folderul de ieșire (presupunem că există)
pdf_to_png(pdf_path, output_folder)
