#!/usr/bin/env python3
import indexer, ranks

def get_page(url):
    try:
        import urllib.request
        return urllib.request.urlopen(url).read().decode('utf-8')
    except:
        return ''

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url, end_quote

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	graph = {} #<url>:[list of pages it links to]
	index = {}
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			indexer.add_page_to_index(index, page, content)
			outlinks = get_all_links(content)
			graph[page] = outlinks
			union(tocrawl, outlinks)
			crawled.append(page)
			#print(crawled)
               
	return index, graph    


if __name__ == '__main__':
	index , graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
	#print(index)
	#print(graph)
	
	rank = ranks.compute_ranks(graph)
	#print(rank)
	
	#print(indexer.lookup(index, "hummus"))
	query = indexer.lookup_best(index, rank, "Hummus")
	for items in query:
		print(items)
