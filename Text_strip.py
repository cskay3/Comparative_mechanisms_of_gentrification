#imports python package
from pypdf import PdfReader
from pathlib import Path

#creates a list of pdfs from folder
readers = []

for pdf in Path("/home/kay/Desktop/Temp2/East").rglob("*.pdf"):
    print(pdf)
    readers.append(PdfReader(pdf))

folder_output = "/home/kay/Desktop/project_papers"

#converts the entire list of pdfs to .txt files 
for i in range(len(readers)):
    reader = readers[i]
    text = ""

    #goes through the pdf page by page
    for page in reader.pages: 
        page_text = page.extract_text()
        if not page_text:
            continue
        
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
    file_name = folder_output + f"/Paper{i+1}.txt"

    #writes all the strings of text into file and adds to folder
    with open(file_name, "w", encoding="utf-8", errors="ignore") as f:
        f.write(text)

    
        
