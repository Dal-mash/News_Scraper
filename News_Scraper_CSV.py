import csv
import requests
import time
from bs4 import BeautifulSoup

interval = int(input("Enter the interval in seconds: "))


while True:
    try:
        #create a csv file to write to
        with open('news.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['No.', "headline", "time", "author","points", "link"])

            ##################################
            # Scrape the website

            print("Scraping...")

            url = "https://news.ycombinator.com/"

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            headlines = soup.find_all('span', class_='titleline')

            subLines = soup.find_all("span", class_="subline")

            index = 1

            #loop through the headlines and sublines to get the information
            for subline, headline in zip(subLines,headlines):

                headlineText = headline.a.text

                post_time = subline.find("span",class_='age').text
                
                author = subline.find("a",class_='hnuser')
                if author:
                    author = author.text
                else:
                    authoe = "N/A"
                
                points = subline.find("span", class_="score")
                if points:
                    points = points.text
                else:
                    points = "0 points"
                
                link = headline.a['href']
                
                csv_writer.writerow([index,headlineText,post_time,author, points, link])
                index += 1

            csv_file.flush()


    except Exception as e:
        print("An error occured, scraping failed")
        print(e)
    finally:    
        print("Scrpaing done, now wating...")
        print("press ctrl+c to stop the program")
        time.sleep(interval)