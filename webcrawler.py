webpage = """ <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://fonts.googleapis.com/css?family=Josefin+Sans" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
    <title>My profile - iReporter</title>
  </head>
  <body class="body">
    <nav class="navbar">
      <span class="navbar-toggle" id="js-navbar-toggle">
        <i class="fas fa-bars"></i>
      </span>
      <a href="http://testing" class="logo"><h1 class="title"> iReporter </h1></a>
      <ul class="main-nav" id="js-menu">
          <li>
              <a href="sign-in.html" class="nav-links">Home</a>
          </li>
          <li>
              <a href="admin.html" class="nav-links">Admin</a>
          </li>
          <li>
              <a href="new-record.html" class="nav-links">New record</a>
          </li>
          <li>
              <a href="profile.html" class="nav-links">My Profile</a>
          </li>
          <li>
              <a href="sign-up.html" class="nav-links">Logout</a>
          </li>
      </ul>
    </nav>
    <div class="row-plain user-record-stats">
      <div class="stat-box">
        <h1 class="stat-number" >9</h1>
        <p class="stat-text">Total</p>
      </div>
      <div class="stat-box">
        <h1 class="stat-number" >9</h1>
        <p class="stat-text">Resolved</p>
      </div>
      <div class="stat-box">
        <h1 class="stat-number" >9</h1>
        <p class="stat-text">Rejected</p>
      </div>
    </div>
    <div class="filter-row">
      <div class="selects">
        <select>
          <option>Type</option>
          <option value="1">Intervention</option>
          <option value="2">Red flag</option>
        </select>
      </div>
      <div class="selects">
        <select>
          <option>Status</option>
          <option value="1">Under Investigation</option>
          <option value="2">Resolved</option>
          <option value="3">Rejected</option>
        </select>
      </div>
      <button class="filter-button" >Filter</button>
    </div>
    <div class="card-grid">
      <div class="card-wrap">
        <div class="card">
          <a href="#modal"><img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="card-img"/></a>
          <div>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at efficitur nisl. </p>
          </div>
          <div class="row-icons"> 
              <p class="type">Red flag</p>
              <div class="buttons">
                <i class="fa fa-edit sm-icon sm-icon-edit" aria-hidden="true"></i>
                <i class="fa fa-trash sm-icon sm-icon-delete" aria-hidden="true"></i>
              </div>
          </div>
        </div>
      </div>
      <div class="card-wrap">
          <div class="card">
            <a href="#modal"><img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="card-img"/></a>
            <div>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at efficitur nisl. </p>
            </div>
            <div class="row-icons"> 
                <p class="type">Red flag</p>
                <div class="buttons">
                  <i class="fa fa-edit sm-icon sm-icon-edit" aria-hidden="true"></i>
                  <i class="fa fa-trash sm-icon sm-icon-delete" aria-hidden="true"></i>
                </div>
            </div>
          </div>
        </div>
        <div class="card-wrap">
            <div class="card">
              <a href="#modal"><img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="card-img"/></a>
              <div>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at efficitur nisl. </p>
              </div>
              <div class="row-icons"> 
                  <p class="type">Red flag</p>
                  <div class="buttons">
                    <i class="fa fa-edit sm-icon sm-icon-edit" aria-hidden="true"></i>
                    <i class="fa fa-trash sm-icon sm-icon-delete" aria-hidden="true"></i>
                  </div>
              </div>
            </div>
          </div>
          <div class="card-wrap">
              <div class="card">
                <a href="#modal"><img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="card-img"/></a>
                <div>
                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at efficitur nisl. </p>
                </div>
                <div class="row-icons"> 
                    <p class="type">Red flag</p>
                    <div class="buttons">
                      <i class="fa fa-edit sm-icon sm-icon-edit" aria-hidden="true"></i>
                      <i class="fa fa-trash sm-icon sm-icon-delete" aria-hidden="true"></i>
                    </div>
                </div>
              </div>
            </div>
            <div class="card-wrap">
                <div class="card">
                  <a href="#modal"><img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="card-img"/></a>
                  <div>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at efficitur nisl. </p>
                  </div>
                  <div class="row-icons"> 
                      <p class="type">Red flag</p>
                      <div class="buttons">
                        <i class="fa fa-edit sm-icon sm-icon-edit" aria-hidden="true"></i>
                        <i class="fa fa-trash sm-icon sm-icon-delete" aria-hidden="true"></i>
                      </div>
                  </div>
                </div>
              </div>
              <div class="card-wrap">
                  <div class="card">
                    <a href="#modal"><img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="card-img"/></a>
                    <div>
                      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at efficitur nisl. </p>
                    </div>
                    <div class="row-icons"> 
                        <p class="type">Red flag</p>
                        <div class="buttons">
                          <i class="fa fa-edit sm-icon sm-icon-edit" aria-hidden="true"></i>
                          <i class="fa fa-trash sm-icon sm-icon-delete" aria-hidden="true"></i>
                        </div>
                    </div>
                  </div>
                </div>
                <div class="card-wrap">
                    <div class="card">
                      <a href="#modal"><img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="card-img"/></a>
                      <div>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at efficitur nisl. </p>
                      </div>
                      <div class="row-icons"> 
                          <p class="type">Red flag</p>
                          <div class="buttons">
                            <i class="fa fa-edit sm-icon sm-icon-edit" aria-hidden="true"></i>
                            <i class="fa fa-trash sm-icon sm-icon-delete" aria-hidden="true"></i>
                          </div>
                      </div>
                    </div>
                  </div>
                  <div class="card-wrap">
                      <div class="card">
                        <a href="#modal"><img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="card-img"/></a>
                        <div>
                          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at efficitur nisl. </p>
                        </div>
                        <div class="row-icons"> 
                            <p class="type">Red flag</p>
                            <div class="buttons">
                              <i class="fa fa-edit sm-icon sm-icon-edit" aria-hidden="true"></i>
                              <i class="fa fa-trash sm-icon sm-icon-delete" aria-hidden="true"></i>
                            </div>
                        </div>
                      </div>
                    </div>
                    <div class="card-wrap">
                        <div class="card">
                          <a href="#modal"><img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="card-img"/></a>
                          <div>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at efficitur nisl. </p>
                          </div>
                          <div class="row-icons"> 
                              <p class="type">Red flag</p>
                              <div class="buttons">
                                <i class="fa fa-edit sm-icon sm-icon-edit" aria-hidden="true"></i>
                                <i class="fa fa-trash sm-icon sm-icon-delete" aria-hidden="true"></i>
                              </div>
                          </div>
                        </div>
                      </div>
                      <div class="card-wrap">
                          <div class="card">
                            <a href="#modal"><img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="card-img"/></a>
                            <div>
                              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at efficitur nisl. </p>
                            </div>
                            <div class="row-icons"> 
                                <p class="type">Red flag</p>
                                <div class="buttons">
                                  <i class="fa fa-edit sm-icon sm-icon-edit" aria-hidden="true"></i>
                                  <i class="fa fa-trash sm-icon sm-icon-delete" aria-hidden="true"></i>
                                </div>
                            </div>
                          </div>
                        </div>
                        <div class="card-wrap">
                            <div class="card">
                              <a href="#modal"><img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="card-img"/></a>
                              <div>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at efficitur nisl. </p>
                              </div>
                              <div class="row-icons"> 
                                  <p class="type">Red flag</p>
                                  <div class="buttons">
                                    <i class="fa fa-edit sm-icon sm-icon-edit" aria-hidden="true"></i>
                                    <i class="fa fa-trash sm-icon sm-icon-delete" aria-hidden="true"></i>
                                  </div>
                              </div>
                            </div>
                          </div>
    </div>
    <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/all.js" integrity="sha384-xymdQtn1n3lH2wcu0qhcdaOpQwyoarkgLVxC/wZ5q7h9gHtxICrpcaSUfygqZGOe"
      crossorigin="anonymous"></script>
    <script src="js/index.js"></script>
  </body>
  <div id="modal" class="modaloverlay">
    <div class="modal">
      <a href="#close" class="close">&times;</a>
      <div class="modal-content">
        <img src="https://images.pexels.com/photos/1464220/pexels-photo-1464220.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" class="modal-img" />
        <div class="modal-record-details">
          <h2 class="modal-record-type">Red flag</h2>
          <p>by olamilekan</p>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <h2 class="modal-record-type">Comment</h2>
          <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
          &nbsp;&nbsp;&nbsp;&nbsp;
          <div class="row-plain">
            <div>
              <h2 class="modal-record-type">Location</h2>
              <p>Lagos, Nigeria</p>
            </div>
            <div>
                <h2 class="modal-record-type">Status</h2>
                <p>Under Investigation</p>
              </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <footer class="footer">
    <p class="footer-text">Copyright iReporter 2018</p>
    <a href="http://thisworks"> Hahaha this works </a>
  </footer>
</html>"""

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

#first_link_index = webpage.find(link_structure)
#print(first_link_index)
#start_quote = webpage.find('"', first_link_index)
#end_quote = webpage.find('"', start_quote+1)
#print(webpage[start_quote+1:end_quote])

#links = get_all_links(webpage)
#print(links)

# print(crawl_web("http://www.udacity.com/cs101x/index.html",3))
print(crawl_web_depth("http://www.udacity.com/cs101x/index.html",0))
