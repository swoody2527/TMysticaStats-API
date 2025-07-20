


def test_winrate_ot(client):
    response = client.get('/api/trends/win-rate-ot?s_year=2013&e_year=2014')


    assert response.status_code == 200


def test_winrate_ot(client):
    response = client.get('/api/trends/pick-rate-ot?s_year=2013&e_year=2014')


    assert response.status_code == 200


def test_winrate_ot(client):
    response = client.get('/api/trends/map-picks-ot?s_year=2013&e_year=2014')



    assert response.status_code == 200

def test_winrate_ot(client):
    response = client.get('/api/trends/map-picks-ot?s_year=2013&e_year=2014')

    

    assert response.status_code == 200