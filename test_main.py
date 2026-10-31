from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# test Home api
def test_home():
    response = client.get("/")
    #status code check
    assert response.status_code==200
    # Response data check
    assert response.json()=={"message":"Hello Abhi"}

# Test ADD API

def test_add():
    response = client.get("/add?a=5&b=4")

    assert response.status_code==200
    assert response.json()=={"result":9}