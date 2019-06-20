def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
    except:
        return ""
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
      while to_crawl and len(crawled) < max_page:
            page = to_crawl.pop()
            if (page not in crawled):
                  links = get_all_links(get_page(page))
                  to_crawl = union(to_crawl, links)
                  crawled.append(page)
      return crawled
                  
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


# print(crawl_web("http://www.udacity.com/cs101x/index.html",3))
print(crawl_web_depth("http://www.udacity.com/cs101x/index.html",0))
