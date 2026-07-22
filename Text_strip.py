#imports python package
from pypdf import PdfReader

#list of pdfs
readers = [PdfReader("/home/kay/Downloads/Papers/PaperEX.pdf"),
           PdfReader("/home/kay/Downloads/Papers/PaperEX2.pdf")]

a = 0

#converts the entire list of pdfs to .txt files 
for i in range(2):
    reader = readers[i]
    text = ""

    #goes through the pdf page by page
    for page in reader.pages: 
        page_text = page.extract_text()
        if page_text:
            #omits the reference section 
            if "References" in page_text:
                indexref = page_text.find("References")
                text += page_text[:indexref]
                break
        #continuously adds the text of the page to text
        text += page_text + "\n"

    #prevents any null characters by replacing it with blank
    text = text.replace("\x00", "")

    #names the new .txt file as "Paper" and its number 
    file_name = "Paper" + str(i+1)  + ".txt"

    #writes all the strings of text into file
    with open(file_name, "w", encoding="utf-8", errors="ignore") as f:
        f.write(text)
        
