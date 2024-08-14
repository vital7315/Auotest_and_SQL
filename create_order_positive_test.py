import configuration

import requests

import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


order_response = post_new_order(data.order_body)
print(order_response.status_code)
print(order_response.json())
order_track = order_response.json().get("track")

print(order_track)


def get_order_by_track(my_order_track):
    return requests.get(configuration.URL_SERVICE
                        + configuration.GET_ORDER_BY_TRACK
                        + "?t=" + my_order_track)


def positive_assert():
    my_order_response = post_new_order(data.order_body)
    my_order_track = str(my_order_response.json().get("track"))
    print("Заказ с трек номером " + my_order_track + " выполнен")
    assert get_order_by_track(my_order_track).status_code == 200


def test_create_order_positive():
    positive_assert()

# Буравов Виталий, 20-я когорта — Финальный проект. Инженер по тестированию плюс
