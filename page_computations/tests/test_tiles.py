from app import app


def test_scor_freq(client):
    
    response = client.get('/api/tiles/score-tile-freq?s_year=2013&e_year=2014')
    print(response.get_json())
    assert response.status_code == 200