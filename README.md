### Comparative_mechanisms_of_gentrification

Description: This python based model:
1) visualizes the effects on demographics (residential population & race) of the different mechanisms of displacement (market-driven rent increase vs tenure conversion of public to private lands) across a set of two case study cities (NYC, New York - Singapore, Singapore) with varied tenure systems
2) applies a Kruskal-Wallis statistical analysis test to assess the results of the demographic data
3) simulates the the skew of definitions of the mechanisms attributed to the term "gentrification" across a sample of literature (on the Global North vs the Global South)
   
# Clone this repository
```python
git clone git@github.com: cskay3/Comparative_mechanisms_of_gentrification.git
cd Comparative_mechanisms_of_gentrification
```
# Required Python packages
```python
pip install numpy pandas scipy matplotlib pypdf
```
# To run your own data
Data on New York and Singapore are included in the code for the bar graphs and the Kruskal-Wallis test. However, to run the literature analysis on your own set of literature, for Text_strip.py input your own file paths of PDFs in the readers list. The model will convert the PDFs to .txt files as well as rename the PDFs so that they can be run through Sort_by_content.py

The census data I used for the New York and Singapore case studies:

New York - https://data.census.gov/profile/New_York?g=040XX00US36

Singapore - https://www.singstat.gov.sg/infographics/census-2020

# Running the models
```python
Kruskal-Wallis_test.py
```
Running this will print out the H-values of the Kruskal-Wallis statistical test of which can be used for comparative purposes.

```python
Sort_by_content.py
```
Running this will print out a list of each .txt file and under it a count of all the keywords that were found and a line that determines the literature's elaborated mechanism of gentrification.
