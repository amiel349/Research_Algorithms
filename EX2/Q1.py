import re
regex = re.compile(r'([A-Za-z0-9]+[.\-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def email_validation_print(file_name: str):
    """
    This method receive a text file and print 2 lists one with all the valid email addresses that the file contain
    and the other with all the invalid emails
    :param file_name:
    :return:
    """
    valid_mails = []
    invalid_mails = []
    try:
        file = open(file_name, 'r')
    except Exception as e:
        print(f'Error while trying to read {file_name} file {str(e)}')
        return
    lines = file.read()
    words =[mail for mail in lines.split() if '@' in mail]
    for mail in words:
        if is_valid(mail):
            valid_mails.append(mail)
        else:
            invalid_mails.append(mail)

    print(f'These are the valid mails addresses {valid_mails}')
    print(f'These are the invalid mails addresses {invalid_mails}')


def is_valid(mail: str):
    """
    This method use regex to check if a given email is valid or invalid
    :param mail:
    :return: None  if invalid otherwise a regex object
    """
    return re.fullmatch(regex, mail)


if __name__ == '__main__':
    email_validation_print('text.txt')