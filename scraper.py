import urllib, os.path

PAGE_URL = 'http://hotoddity.com/page'
OUT_DIR = './output'


## simple
def get_page_pic_urls(page_num):
    print 'getting page: %s' % page_num
    html = urllib.urlopen('%s/%s' % (PAGE_URL,page_num)).readlines()
    # hack way of finding all the high res links
    pic_urls = []
    for line in html:
        if 'data-highres' in line:
            url = line.split('data-highres')[1].split('"')[1]
            pic_urls.append(url)

    return pic_urls

def download_photo(url):
    # save it down
    print 'getting: %s' % url
    # grab the image data
    data = urllib.urlopen(url).read()
    photo_name = '%s.jpg' % url.split('_')[-1]
    out_path = os.path.join(OUT_DIR,photo_name)
    print 'saving to: %s' % out_path
    with open(out_path,'w') as fh:
        fh.write(data)


def get_all(total_pages=120):
    print 'getting all'
    # go through the page #'s
    pic_urls = []
    for i in xrange(total_pages):
        # get urls of images
        urls = get_page_pic_urls(i+1)
        if not urls:
            # no more pages
            break
        pic_urls += urls

    # download all the images
    for url in pic_urls:
        download_photo(url)


if __name__ == '__main__':
    print 'starting'
    get_all()
