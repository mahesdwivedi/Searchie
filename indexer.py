# add_page_to_index, takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It updates the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

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

if __name__ == '__main__':
    add_page_to_index(index,'fake.text',"This is a test")
    add_page_to_index(index,'real.text',"This is not a test")
    print(index)


