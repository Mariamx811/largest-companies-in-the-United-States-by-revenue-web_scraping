#%%
from bs4 import BeautifulSoup
import requests
# %%
url ='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
# %%
print(soup.prettify())
# %%
table = soup.find('table', class_="wikitable sortable")
# %%
header_list = table.find_all('th')
headers = [title.text.strip() for title in header_list]
print(headers)
# %%
import pandas as pd
df = pd.DataFrame(columns=headers)
df
# %%
row_list = table.find_all("tr")[1:]
for row in row_list:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    df.loc[len(df)] = individual_row_data

#%%
table2 = soup.find_all(class_ = "wikitable sortable")[2]
headers_2_list = table2.find_all("th")
headers2 = [header.text.strip() for header in headers_2_list]
df2 = pd.DataFrame(columns=headers2)

#%%
rows_2_list = table2.find_all("tr")[1:]
for row in rows_2_list:
    datas = row.find_all("td")
    data2 = [info.text.strip() for info in datas]
    df2.loc[len(df2)] = data2
#%%
with pd.ExcelWriter(r"C:\Users\Dell\Desktop\webScraping\largest_company_revenue.xlsx") as writer:
    df.to_excel(writer, sheet_name='largest public traded companies',index=False)
    df2.to_excel(writer, sheet_name='companies by profit', index=False)
# %%
