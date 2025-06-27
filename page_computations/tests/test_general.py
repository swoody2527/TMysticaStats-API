import pytest
from app import app



def test_general(client):
    response = client.get('api/general/strongest-faction')
    msg = response.get_json()['msg']
    assert msg == 'Test model response'
