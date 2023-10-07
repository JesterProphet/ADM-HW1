from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):

        print(tag)

        for attribute in attrs:
            print("-> {} > {}".format(*attribute))


n = int(input())
parser = MyHTMLParser()

for _ in range(0, n):

    html_code = input()
    parser.feed(html_code)
