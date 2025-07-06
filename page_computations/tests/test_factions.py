import pytest
from app import app



def test_factions(client):
    response = client.get('api/factions/faction-wr')
    msg = response.get_json()['msg']
    assert msg == 'Test msg'
