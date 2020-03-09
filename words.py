"""Retrieve and print words from a URL.

    Usage:
        python3 words <URL>

"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

      Args:
          url: The URL of a UTF-8 text document.

      Returns:
          A list of strings containing the words from the document.
    """
    from urllib.request import urlopen

    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    for word in items:
        print(word)


def main(url):
    if url == None:
        url = 'http://sixty-north.com/c/t.txt'
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) #the first argument (0) is the python filename.
