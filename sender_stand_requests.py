# Максим Шемяков, 17 когорта - Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data


def post_new_order(): #Запрос на создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)  #тут тело


def get_track_number(): #Запрос на сохранение трек-номер заказа
    track = post_new_order()
    return track.json()["track"]

def get_order_body(track): #Запрос на сохранение трек-номер заказа
    return requests.get(configuration.URL_SERVICE + configuration.GET_INFO_BY_TRACK,
          params = {"t": track})




