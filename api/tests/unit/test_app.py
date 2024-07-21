def test_ping(client):
    res = client.get('/ping')
    assert res.status_code == 200
    response_json = res.get_json()
    expected = {'message': 'Pong!'}
    assert response_json == expected