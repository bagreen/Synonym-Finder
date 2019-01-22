import bs4
import requests


articles = ['a', 'an', 'the']
conjunctions = ['after', 'although', 'and', 'as', 'because', 'before', 'both', 'but', 'either', 'even', 'for', 'if', 'lest', 'neither', 'nor', 'once', 'or', 'since', 'so', 'than', 'that', 'though', 'till', 'unless', 'until', 'when', 'whenever', 'where', 'wherever', 'whether', 'while', 'yet']
interjections = ['aha', 'ahem', 'ah', 'ahh', 'ahoy', 'alas', 'arg', 'aw', 'bam', 'bingo', 'blah', 'boo', 'bravo', 'brrr', 'cheers', 'congratulations', 'dang', 'drat', 'darn', 'duh', 'eek', 'eh', 'encore', 'eureka', 'fiddlesticks', 'gadzooks', 'gee', 'golly', 'goodbye', 'goodness', 'gosh', 'ha-ha', 'hallelujah', 'hello', 'hey', 'hmm', 'huh', 'humph', 'hurray', 'oh', 'oops', 'ouch', 'ow', 'phew', 'phooey', 'pooh', 'pow', 'rats', 'shh', 'shoo', 'thanks', 'there', 'tut-tut', 'uh-huh', 'uh-oh', 'ugh', 'wahoo', 'well', 'whoa', 'whoops', 'wow', 'yeah', 'yes', 'yikes', 'yippee', 'yo', 'yuck']
prepositions = ['aboard', 'about', 'above', 'across', 'after', 'against', 'along', 'amid', 'among', 'anti', 'around', 'as', 'at', 'at', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between', 'beyond', 'but', 'by', 'concerning', 'considering', 'despite', 'down', 'during', 'except', 'excepting', 'excluding', 'following', 'for', 'from', 'in', 'inside', 'into', 'like', 'minus', 'near', 'of', 'off', 'on', 'onto', 'opposite', 'outside', 'over', 'past', 'per', 'plus', 'regarding', 'round', 'save', 'since', 'than', 'through', 'to', 'toward', 'under', 'underneath', 'unlike', 'until', 'up', 'upon', 'versus', 'via', 'with', 'within', 'without']


def pick_file():
    return open('test.txt', 'r')


def get_words():
    file = pick_file()
    words = []

    for line in file.readlines():
        line_words = line.split()

        for line_word in line_words:
            word = ''

            for char in line_word:
                if char.isalpha():
                    word = word + char.lower()

            if word not in articles and word not in conjunctions and word not in interjections and word not in prepositions and word not in words:
                words.append(word)

    words.sort()
    return words


def find_synonyms(word):
    synonyms = []
    url = 'https://www.thesaurus.com/browse/' + word

    web_request = bs4.BeautifulSoup(requests.get(url).text, features='html.parser')

    try:
        for synonym in web_request.find('ul', class_='css-1lc0dpe et6tpn80'):
            synonyms.append(synonym.text)
    except TypeError:
        pass

    return synonyms


def main():
    words = get_words()

    for word in words:
        print(word)

    # print()
    # print()
    #
    # for word in words:
    #     synonyms = find_synonyms(word)
    #
    #     if len(synonyms) is 0:
    #         print(word + ' has no synonyms')
    #     else:
    #         print(word + ' has these synonyms:')
    #
    #         for synonym in synonyms:
    #             print(synonym)
    #     print()


if __name__ == '__main__':
    main()
