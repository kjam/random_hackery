from lxml import html
from collections import Counter
import re

tree = html.parse('http://2015.djangocon.eu/talks/')
root = tree.getroot()

talks = root.cssselect('li.programme')
all_talk_text = ''
titles = ''
cardiff = 0

for talk in talks:
    talk_text = (lambda x: x[0].text_content() if x
                 else '')(talk.cssselect('span.summary'))
    talk_title = talk.cssselect('span.title')[0]
    all_talk_text += ' '.join([talk_title.text_content().encode('utf8'),
                               talk_text])
    titles += talk_title.text_content()
    if 'Cardiff' in ' '.join([talk_title.text_content(), talk_text]):
        cardiff += 1
    #print '{}: {}'.format(talk_title.text_content().encode('utf8'), talk_text)

all_words = re.findall(r'\w+', all_talk_text)
all_titles = re.findall(r'\w+', titles)

print len(titles) / (len(talks)) * 1.0
print (cardiff * 1.0) / len(talks)
#print Counter(all_words)

