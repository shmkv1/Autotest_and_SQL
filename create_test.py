# Максим Шемяков, 17 когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_requests

def test_create_track():
    track = sender_stand_requests.get_track_number()
    track = sender_stand_requests.get_order_body(track)
    assert track.status_code == 200




