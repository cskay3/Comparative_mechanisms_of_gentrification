### Comparative_mechanisms_of_gentrification

Description: This python based model:
1) Visualizes the effects on demographics (residential population & race) of the different mechanisms of displacement (market-driven rent increase vs tenure conversion of public to private lands) across a set of two case study cities (NYC, New York - Singapore, Singapore) with varied tenure systems
2) Applies a Kruskal-Wallis statistical test to assess the results of the demographic data
3) Simulates the the skew of definitions of the mechanisms attributed to the term "gentrification" across a sample of literature (on the Global North vs the Global South)
4) Visualizes the literature analysis data in pie charts
5) Applies a Kruskal-Wallis statistical test to assess the results of the literature analysis
   
# Clone this repository
```python
git clone https://github.com/cskay3/Comparative_mechanisms_of_gentrification
```

# Set up
Navigate into the specific directory:
```python
cd Comparative_mechanisms_of_gentrification
```
Create virtual environment:
```python
python3 -m venv venv
source venv/bin/activate
```
Then install the required Python packages:
```python
pip install numpy pandas scipy matplotlib pypdf
```
# To run your own data
Data on New York and Singapore is included in the code for the bar graphs and the Kruskal-Wallis test. However, to run the literature analysis on your own set of literature, for Text_strip.py input your own file paths of PDFs in the readers list. The model will convert the PDFs to .txt files as well as rename the PDFs so that they can be run through Sort_by_content.py

The census data I used for the New York and Singapore case studies:

New York - https://data.census.gov/profile/New_York?g=040XX00US36

Singapore - https://www.singstat.gov.sg/infographics/census-2020

# Running the models
Navigate into the specific directory:
```python
cd Comparative_mechanisms_of_gentrification
```
```python
Sort_by_content.py
```
It will first ask you: Provide path to folder with article .txt files:
Please respond with ex: /home/name/Comparative_mechanisms_of_gentrification/Articles
Input your name!

Then the program will run as intended. It will classify each .txt article's stated mechanism of gentrification by running it through a list of keywords per each mechanism category. It will print out:  
article#  
Market driven: # of words in text/22  
Tenure conversion: # of words in text/19  

And:
```python
Kruskal-Wallis_test_stats.py
Kruskal-Wallis_test_lit.py
```
Running this will print out the H-values and p-values of the Kruskal-Wallis statistical test of which can be used for comparative purposes. Kruskal-Wallis_test_stats.py will output values for the New York City vs Singapore datasets. Kruskal-Wallis_test_lit.py will output values for the three different North vs South vs East cases of the literature analysis.

## Reproduce study's paper and slideshow
#PAPER  
Download the entire "Tex_report" folder (inclusive of all image .png and .bib files)
Open a LaTeX distribution and compile:
```bash
pdflatex KeinaGa_Global_Gentrification_report.tex
bibtex main
pdflatex KeinaGa_Global_Gentrification_report.tex
pdflatex KeinaGa_Global_Gentrification_report.tex
```
To produce the study's report  
#SLIDES  
Download the raw file of "KeinaGa_Global_Gentrification_slides.odp"  
Open the .odp with LibreOffice Impress to produce the study's slideshow
