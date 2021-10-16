from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def get_decimal_rub_val(soup, currency):
    if currency == 'RUR':
        return Decimal(1)
    node = soup.find('CharCode', text=currency)
    value = Decimal(node.find_next_sibling('Value').string.replace(',', '.'))
    nominal = Decimal(node.find_next_sibling('Nominal').string.replace(',', '.'))
    return value / nominal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp',
                            params={'date_req': date})  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'xml')

    from_ = get_decimal_rub_val(soup, cur_from)
    to_ = get_decimal_rub_val(soup, cur_to)
    result_ = from_ * amount / to_

    return result_.quantize(Decimal('.0001'))  # не забыть про округление до 4х знаков после запятой


if __name__ == '__main__':
    correct = Decimal('3754.8057')
    result = convert(Decimal("1000.1000"), 'RUR', 'JPY', "17/02/2005", requests)
    if result == correct:
        print("Correct")
    else:
        print("Incorrect: %s != %s" % (result, correct))
