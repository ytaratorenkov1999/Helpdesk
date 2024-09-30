from Even_request_list import Even
from ODD_requests_list import Odd

def total_request():
    lst_total = Even.even_request() + Odd.odd_request()
    lst_total.sort(key=lambda x: x[2])

    return lst_total

