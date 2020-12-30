from GoogleNews import GoogleNews

news = GoogleNews(lang='en')
news.search('blockchain')
result = news.result()


def get_header(idx):
    title = result[idx]['title']
    split = title.split(' - ')
    header = ''
    for i in range(len(split) - 1):
        header += split[i]
    return header


def get_publisher(idx):
    return result[idx]['media']


def get_content(idx):
    return result[idx]['desc']


def get_link(idx):
    return result[idx]['link']


def get_num_days_ago(idx):
    return result[idx]['date']


def get_base64_img(idx):
    return result[idx]['img']
