import threading
import urllib2
import time

start = time.time()
urls = ['htttps://www.jogosbr.net', 'https://www.jogos360.com.br', 'https://clickjogos.com.br', 'https://www.papajogos.com.br']

def chama_url(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print( "'%s\ ' carregado em %ss" % (url, (time.time() - start)))

threads = [threading.Thread(target=chama_url, args=(url,)) for url in urls]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Elapsed Time: %s" %(time.time() - start))