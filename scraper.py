# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

# This can be changed to the URL you want to start from
starturl = 'https://github.com/search?utf8=%E2%9C%93&q=location%3Abirmingham&type=Users&ref=searchresults'
# Later this can be adapted to generate different results based on parameters such as location, in name, type
# See https://help.github.com/articles/searching-users/

# # Read in a page
html = scraperwiki.scrape(starturl)
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
listinfo = root.cssselect("div.user-list-info")
#user_search_results > div.user-list > div:nth-child(1) > div.user-list-info
for user in listinfo:
  print user
  print user.text()
#
# # Write out to the sqlite database using scraperwiki library
#scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
