index = []

def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        # not found, add new keyword to index 
        index[keyword] = [url]


def add_page_to_index(index,url,content):
    keyword = content.split()
    for key in keyword:
        add_to_index(index,key,url)
        
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None

def lookup_best(index, ranks, keyword):
	if keyword in index:
		newindex = index[keyword][:]
		index[keyword] = []

		while newindex:
			largest = 0.0
			largestIndex = None
			
			for i in range(0,len(newindex)):
				if ranks[newindex[i]] > largest:
					largest = ranks[newindex[i]]
					largestIndex = i
			
			if largestIndex != None:
				index[keyword].append(newindex.pop(largestIndex))
		
		return index[keyword]
	return None


if __name__ == '__main__':
    add_page_to_index(index,'fake.text',"This is a test")
    add_page_to_index(index,'real.text',"This is not a test")
    print(index)
