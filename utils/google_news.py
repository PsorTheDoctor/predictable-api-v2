from pygooglenews import GoogleNews

api = GoogleNews(lang='en')
news = api.search('blockchain')


def get_header(idx):
    title = news['entries'][idx]['title']
    split = title.split(' - ')
    header = ''
    for txt in range(len(split) - 1):
        header += txt
    return header


def get_publisher(idx):
    title = news['entries'][idx]['title']
    split = title.split(' - ')
    publisher = split[len(split) - 1]
    return publisher


def get_link(idx):
    return news['entries'][idx]['link']


def get_publish_date(idx):
    return news['entries'][idx]['published']
