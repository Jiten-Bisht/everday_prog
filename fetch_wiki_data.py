# You can Extract the Wikipedia data this simple Advanced Script of Python. Just you had to install the following module and follow the Code example below.

# Install this module: pip install wikipedia
import wikipedia
# get Suggestion
s =  wikipedia.search("Python", result=3)  # 'Python (programming language)', 'Python', 'Monty Python'
# get page
wikipage = wikipedia.page("Python")
# get page title
title = wikipage.title
# get Url of page
print(wikipage.url)
# get content of the Page
c = wikipage.content
# get Images of Page
print(len(wikipage.images))
wikipage.images[0]
# get links on the Page
link = wikipage.links[0:5]
# get Summary with lang
sm = wikipedia.set_lang("en")
sm = sm.summary("Python")
