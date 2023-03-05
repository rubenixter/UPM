"""
Author: Rubén Llorente Canet 
"""

import os
import requests
import re
from grobid_client_python.grobid_client.grobid_client import GrobidClient
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Directory where the PDF files are stored
pdf_dir = "./ToAnalize"
fig_dir="./Results"
nums=[]

i=1
# Grobid API endpoint
grobid_api = "http://localhost:8070/api/processFulltextDocument"
client = GrobidClient(config_path="./config.json")
headers = {'Accept': 'application/xml'}
with open('./Results/urls1'+'.txt', 'w') as file:
    # Loop over all PDF files in the directory
    for file_name in os.listdir(pdf_dir):
        urls = []
        if file_name.endswith(".pdf"):
            # Get the binary data of the PDF file
            file_path = os.path.join(pdf_dir, file_name)
            with open(file_path, "rb") as f:
                pdf_data = f.read()
            respuesta =client.post(grobid_api, headers=headers, files={'input': ('input.pdf', pdf_data)})
            fres=respuesta[0].text.encode('utf-8')
            results = re.findall(r"<abstract>(.*?)</abstract>", str(fres), re.DOTALL)
        
            if results:
                for result in results:
                    abs = re.findall(r"<p>(.*?)</p>", str(result), re.DOTALL)
                    abstract  = abs[0].encode("utf-8").decode("utf-8")
                    wordcloud = WordCloud(width=800, height=800, background_color='white').generate(abstract)

                    # plot the word cloud
                    #plt.figure(figsize=(6,6), facecolor=None)
                    plt.title('Cloud'+str(i))
                    plt.imshow(wordcloud)
                    plt.axis("off")
                    plt.tight_layout(pad=0)
                    
                    #plt.show()
                    plt.savefig(fig_dir+'/Wordcloud'+str(i)+'.png')
                    
        else:
            print("No results found")

        figure_count = len(re.findall(r"</figure>", str(fres), re.DOTALL))
        nums.append(figure_count)
        pattern = r'<ptr target=(\S+)'
        words = re.findall(pattern,  str(fres), re.DOTALL)
        if words:
            # If matches are found, add them to the url_list
            urls.extend(words)

        if urls:
            file.write('pdf'+str(i) + '\n')
            for url in urls:
                file.write(url + '\n')
        i=i+1
                
    nombres = []

    # Loop through a range of numbers from 1 to 10
    for x in range(1, i):
        # Create a new string of the form "Fichero i"
        nombre = "Fichero " + str(x)
        
        # Append the new string to the list
        nombres.append(nombre)

plt.figure(figsize=(6,6), facecolor=None)
plt.title('bars')
plt.bar(nombres,nums)


plt.xlabel("Number")

#plt.show()
plt.savefig(fig_dir+'/Bars'+'.png')
print('Finished')
