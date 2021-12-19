from conf import MODEL
import random
from faker import Faker
import json


def title(f):
    """

    :param f: file
    :return: random name from file
    """
    return random.choice(f.readlines()).strip()


def year():
    """

    :return: year
    """
    return random.randint(1900, 2021)


def pages():
    """

    :return: pages
    """
    return random.randint(1, 3000)


def isbn13(fake):
    """

    :param fake:
    :return: isbn code
    """
    return fake.isbn13()


def rating():
    """

    :return: rating
    """
    return round(random.random()*10 % 5, 2)


def price():
    """

    :return: price
    """
    return round(random.random()*1000, 2)


def author(fake):
    """

    :param fake:
    :return: author
    """
    return [fake.name() for i in range(random.randint(1, 3))]


def gen_book(pk):
    """
    function generate book
    :param pk:
    :return: book dict
    """
    while True:
        with open("books.txt", 'r') as f:
            fake = Faker()
            data = {
                "model": MODEL,
                "pk": pk,
                "fields": {
                    "title": title(f),
                    "year": year(),
                    "pages": pages(),
                    "isbn13": isbn13(fake),
#  "isbn13": f"{random.randint(100, 999)}-{random.randint(0, 9)}-{random.randint(10000, 99999)}-{random.randint(100, 999)}-{random.randint(0, 9)}", #Faker.Code.isbn13 #Faker.providers.isbn
                    "rating": rating(),
                    "price": price(),
                    "author": author(fake)
                }
            }
            pk += 1
            yield data


if __name__ == '__main__':
    books_generator = gen_book(1)
    print(next(books_generator))
#   print(next(books_generator))
#   print(next(books_generator))
    res = []
    for i in range(100):
        res.append(next(books_generator))
    # with open("out.txt", 'w') as f:
    #    f.write(str(json.dumps(res)))

    with open("out.txt", 'w', encoding='utf-8') as f:
        for book in res:
            f.write(str(json.dumps(book, ensure_ascii=False)) + '\n')
