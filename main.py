from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get("https://www.scrapethissite.com/pages/simple/").text
# print(html_text)
# print(dir(html_text))
# print(html_text.text)

souped_html = BeautifulSoup(html_text, "lxml")

countries = souped_html.find_all('h3')
country_capital_list = souped_html.find_all('span', class_="country-capital")
country_population_list =souped_html.find_all('span', class_="country-population")
country_area_list =souped_html.find_all('span', class_="country-area")

for each_area in country_area_list:
    print(each_area.text.strip())
# for each_population in country_population_list:
#     print(each_population.text.strip())
# for each_capital in country_capital_list:
#     print(each_capital.text.strip())
# print(countries)
# for each_country in countries:
#    print(each_country.text.strip())
     #.strip removes spaces

df = pd.DataFrame({
    "Countries": [each_country.text.strip()for each_country in countries],
    "Capitals": [each_capital.text.strip() for each_capital in country_capital_list],
    "Population": [each_population.text.strip() for each_population in country_population_list],
    "Area": [each_area.text.strip() for each_area in country_area_list]})
print(df)

# Save the DataFrame to an Excel file
excel_filename = 'main_info.xlsx'
df.to_excel(excel_filename, index=False)
