from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address(maxlen):
    symbols = string.ascii_letters + string.digits
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, postfix, maxlen):
    symbols = string.ascii_letters + "._-"
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + postfix


def random_phone(maxlen):
    symbols = '0123456789'
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", email='', mobilephone='')] + [
    Contact(firstname=random_string('name', 10), lastname=random_string('header', 20),
            email=random_email('email', '@gmail.com', 10), mobilephone=random_phone(10),
            email2=random_email('email', '@mail.ru', 10), title=random_string('name', 10),
            address=random_address(20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(jsonpickle.encode(testdata))
