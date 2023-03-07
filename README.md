# UPM
In this document, the operation of the IAOS.py program will be explained, in addition to giving instructions on how to make an environment to run this locally, 
and some Docker run instructions

[![DOI](https://zenodo.org/badge/598232222.svg)](https://zenodo.org/badge/latestdoi/598232222)
## AIOS.py

It is supossed that you have grobbid properly instaled in your machine and running at localhost:8070

This python script will read the .pdf files from the folder./ToAnalize which and will Create some files on ./Results. The folder ./ToAnalize must contain papers in pdf format. The program will create 3 types of results. 
The first one will be a set of .png images that will show a wordcloud of the keywords in the abstract of the papers with the name WordcloudX.png in which X is the number of the pdf in grammatical order. 
Another .png image will be created where it will show a bar chart showing the number of figures in each pdf
Finally a urls.txt will be created if the with the url in each paper.

## Environment

You this code was made under python 3.9.16 and uses pip 22.3.1.
The code imports os, request, wordcloud, re, and matplot.pyplot modules. To get this modules simply copy the pip install bash code bellow.


```bash
pip install requests
```
```bash
pip install matplot
```
```bash
pip install wordcloud
```

Assuming that you have the grobid instalation for python done. If not check: https://github.com/kermitt2/grobid_client_python

## Docker
 
To create the container, use this command in the same directory as the environment:
```bash
docker build -t iaos .
```

To run the container:
```bash
docker run --network=host -v ./ToAnalize:/app/ToAnalize -v ./Results:/app/Results iaos
```

