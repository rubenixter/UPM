For this assesment our program must:
- Draw a keyword cloud based on the words found in the abstract of your papers.
- Create a visualization showing the number of ﬁgures per article.
- Create a list of the links found in each paper.

To achieve this IAOS.py gets the pdfs for the folder ToAnalize and uses the grobid API to generate the XML file of each paper. For each XML file the program finds the XML object
of the abstract in order to get a wordcloud using python wordclouds module. For the number of figures, the program look for figure tags and counts them so that at the end it generates a bar plot diagram.
Finally, for the list of links, it writes a txt file showing the links of each paper in gramatical order, if the paper does not contain any link it won´t write anything.
