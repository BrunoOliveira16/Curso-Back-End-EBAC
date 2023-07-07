import requests
import time
import csv
import random
import concurrent.futures

from bs4 import BeautifulSoup

# global headers a serem usados ​​para solicitações
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

MAX_THREADS = 10

def extract_movie_details(movie_link):
    time.sleep(random.uniform(0, 0.2))
    response = BeautifulSoup(requests.get(movie_link, headers=headers).content, 'html.parser')
    movie_soup = response

    if movie_soup is not None:
        title = None
        date = None

        movie_data = movie_soup.find('div', attrs={'class': 'sc-385ac629-3 kRUqXl'})
        if movie_data is not None:
            title = movie_data.find('h1').get_text()
            date = movie_data.find('a', attrs={'class': 'ipc-link ipc-link--baseAlt ipc-link--inherit-color'}).get_text().strip()

        rating = movie_soup.find('span', attrs={'class': 'sc-bde20123-1 iZlgcd'}).get_text() if movie_soup.find('span', attrs={'class': 'sc-bde20123-1 iZlgcd'}) else None

        plot_text = movie_soup.find('span', attrs={'class': 'sc-6a7933c5-1 fPmRoa'}).get_text().strip() if movie_soup.find('span', attrs={'class': 'sc-6a7933c5-1 fPmRoa'}) else None

        with open('movies.csv', mode='a') as file:
            movie_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if all([title, date, rating, plot_text]):
                print(title, date, rating, plot_text)
                movie_writer.writerow([title, date, rating, plot_text])


def extract_movies(soup):
    movies_table = soup.find('div', attrs={'data-testid': 'chart-layout-main-column'}).find('ul')
    # Modificação realizada devido erro AttributeError: 'NoneType' object has no attribute 'find', pois a 'div' não estava sendo encontrada
    movies_table_div = soup.find('div', attrs={'data-testid': 'chart-layout-main-column'})
    if movies_table_div is not None:
        movies_table = movies_table_div.find('ul')
    else:
        print('A div com o atributo data-testid igual a chart-layout-main-column não foi encontrada')

    movies_table_rows = movies_table.find_all('li')
    movie_links = ['https://imdb.com' + movie.find('a')['href'] for movie in movies_table_rows]

    threads = min(MAX_THREADS, len(movie_links))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(extract_movie_details, movie_links)


def main():
    start_time = time.time()

    # IMDB Most Popular Movies - 100 movies
    popular_movies_url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
    response = requests.get(popular_movies_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    #Função principal para extrair 100 filmes do IMDB Most Popular Movies
    extract_movies(soup)

    end_time = time.time()
    print('total time taken: ', end_time - start_time)


if __name__ == '__main__':
    main()