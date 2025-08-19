# Election Results Scraper

This project is part of the Engeto Online Python Academy.  
It is a Python script designed to extract election results from the Czech parliamentary elections in 2017.   

---

## Project Description

The script downloads and processes election results for a selected district from [volby.cz](https://www.volby.cz).  
The output is saved into a `.csv` file containing information about the number of registered voters, envelopes issued, valid votes, and votes for individual parties.

---

## Installation

The project uses external libraries, which are listed in the `requirements.txt` file.  
It is recommended to install them in a virtual environment.  

Run the following commands in your terminal:

```bash
# check pip version
pip3 --version

# install all required libraries
pip3 install -r requirements.txt
```

## Running the Project

The script requires two arguments:
  1) A valid URL of the selected district from volby.cz.
  2) The output .csv file name.
     
In this format:
```
python main.py <district_url> <output_file.csv>
```
Unless the inputs are invalid, the csv file will be created in your current directory.

## Example:
Results of voting for the Prostějov district:

1st argument:
https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103


2nd argument:
results_prostejov.csv

## Command to run:
```
python main.py  "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" results_prostejov.csv
```

## Console output:
```
Nalezeno obcí: 97
Stahuji: Prostějov
Stahuji: Bedihošť
Stahuji: Čelčice
...
Úloha dokončena. Data uložená v souboru: results_prostejov.csv
```

## Partial .csv output
```
code	name	registered	envelopes	valid	ANO 2011	Blok proti islam.-Obran.domova	CESTA ODPOVĚDNÉ SPOLEČNOSTI
506761	Alojzov	205	145	144	32	0	0
589268	Bedihošť	834	527	524	140	1	0
589276	Bílovice-Lutotín	431	279	275	83	0	0
```
