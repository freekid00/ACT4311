#coding=utf8
"""
Created on Wed Sep 20 23:10:43 2018

@author: Neal LONG
"""

from bs4 import BeautifulSoup

#Read HTML string from file
with open('./data/table.html','r',encoding='utf8') as rf:
    html_string = rf.read()
    
#print(html_string)

# Parse the HTML string and get the root of DOM
root = BeautifulSoup(html_string,"html.parser") 

table = root.find('table',attrs={'id':2}) # Locate the table under the 
print(table)
print("="*20)
row_marker = 0
#get the children rows under table
for row in table.find_all('tr'):
    column_marker = 0
    print("\nProcessing row",row_marker)
    #get the children columns under row tr
    columns = row.find_all('td')
    for column in columns:
        print("We are now proceesing row=",row_marker,"and column=",column_marker,
              ' with value=',column.get_text())
#        pd_table.loc[row_marker,column_marker] = column.get_text()
        column_marker += 1 #process next column of current row
    row_marker+=1 #process next row
print("="*20)    
print(root.find('td',string="20")) # Locate the element by text


print("="*20)    

markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup,"html.parser")

print(soup.get_text())
print(soup.i.get_text())
