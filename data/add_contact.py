from model.contact import Contact
import random
import string


constant = [
    Contact(firstname='firstname1', lastname='lastname1', email='email@1', mobilephone='0123456789'),
    Contact(firstname='firstname2', lastname='lastname2', email='email@2', mobilephone='1234567890'),
]


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
    for i in range(5)
]