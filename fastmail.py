import cfscrape
from ast import literal_eval as le

scraper = cfscrape.CloudflareScraper()

help_text = '''
-h вызвать справку
-l [логин почты] получаем все сообщения
-i [id сообщения] читаем выбранное сообщение
-q выход
'''

print('Вызвать справку: -h')

login = ''


def getMessages(login):
    response = scraper.get(
        'https://www.1secmail.com/api/v1/?action=getMessages&login=%s&domain=1secmail.com' %login).text
    get_str = ''.join(response).replace('[','').replace(']','').replace('{','').replace('}','').replace(',','\n')
    return get_str


def readMessage(login, id):
    response = scraper.get(
        'https://www.1secmail.com/api/v1/?action=readMessage&login=%s&domain=1secmail.com&id'
        '=%s' %(login, id)).text
    result = le(response)
    return result.get('textBody')


while True:
    member_input = input('Ввод: ')

    if member_input.startswith('-l'):
        login = member_input.replace('-l ', '')
        print(getMessages(login))

    if member_input.startswith('-i'):
        id = member_input.replace('-i ', '')
        print(readMessage(login, id))

    if member_input == '-h':
        print(help_text)

    if member_input == '-q':
        break


