from pypdf import PdfReader

readers = [PdfReader("/home/kay/Downloads/Papers/PaperEX.pdf"),
           PdfReader("/home/kay/Downloads/Papers/PaperEX2.pdf")]

a = 0

for i in range(2):
    reader = readers[i]
    text = ""
    
    for page in reader.pages: 
        page_text = page.extract_text()
        if page_text:
            if "References" in page_text:
                indexref = page_text.find("References")
                text += page_text[:indexref]
                break
        text += page_text + "\n"

    text = text.replace("\x00", "")

    file_name = "Paper" + str(i+1)  + ".txt"
    
    with open(file_name, "w", encoding="utf-8", errors="ignore") as f:
        f.write(text)
        
