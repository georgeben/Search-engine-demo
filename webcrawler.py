import urllib.request


def get_page(url):
    try:
      content = urllib.request.urlopen(url).read()
      return str(content)
    except:
      return ""


def union(list1, list2):
    for item in list2:
        if item not in list1:
            list1.append(item)
    return list1

def get_next_link(page):
      link_structure = "<a href="
      start_index = page.find(link_structure)
      if (start_index == -1):
            return None, 0
      start_quote_index = page.find('"', start_index)
      end_quote_index = page.find('"', start_quote_index+1)
      url = page[start_quote_index+1: end_quote_index]
      return url, end_quote_index

def get_all_links(page):
      links = []
      while True:
            url, end_quote_index = get_next_link(page)
            if url:
                  # print(url)
                  links.append(url)
                  page = page[end_quote_index:]
            else:
                  break
      return links

def crawl_web(seed, max_page):
      to_crawl = [seed]
      crawled = []
      index = []
      while to_crawl and len(crawled) < max_page:
            url = to_crawl.pop()
            if (url not in crawled):
                  page_content = get_page(url)
                  links = get_all_links(page_content)
                  to_crawl = union(to_crawl, links)
                  crawled.append(url)
                  add_page_to_index(index, url, page_content)
      return index
                  
def crawl_web_depth(seed, max_depth):
      to_crawl = [seed]
      crawled = []
      next_depth = []
      depth = 0

      while to_crawl and depth <= max_depth:
            page = to_crawl.pop()
            if (page not in crawled):
                  next_depth = union(next_depth, get_all_links(get_page(page)))
                  crawled.append(page)
            if not to_crawl:
                  to_crawl, next_depth = next_depth, []
                  depth += 1
      return crawled

def add_to_index(index, url, keyword):
      #index structure - [[keyword, [url1, url2]]]
      for entry in index:
            if (entry[0] == keyword):
                  entry[1].append(url)
                  return
      index.append([keyword, [url]])

def lookup(index, keyword):
      for entry in index:
            if (entry[0] == keyword):
                  return entry[1]
      return []

def add_page_to_index(index, url, content):
      for word in content.split():
            add_to_index(index, url, word)

index = crawl_web("https://georgeben.dev",5)
print(index)
# print(crawl_web_depth("http://www.udacity.com/cs101x/index.html",0))
# index = []
# add_page_to_index(index, 'georgeben.dev', 'My name is George Benjamin')
# add_page_to_index(index, 'github.com', 'George Benjamin is a software developer')
print(lookup(index, 'developer'))
#print(index)
