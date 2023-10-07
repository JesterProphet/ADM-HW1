import textwrap

def wrap(string, max_width):

    l = textwrap.wrap(string, max_width)
    output = "\n".join(l)

    return output

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)