from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)

        for element in attrs:
            print("-> " + str(element[0]) + ' > ' + str(element[1]))

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)

        for element in attrs:
            print("-> " + str(element[0]) + ' > ' + str(element[1]))


n = int(input())
parser = MyHTMLParser()

for _ in range(0, n):

    parser.feed(input())

