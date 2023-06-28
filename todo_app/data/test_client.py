import  pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import mongomock

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client
            
def test_index_page(monkeypatch, client):
    # This replaces any call to requests.get with our own function
    monkeypatch.setattr(stub)

    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()
    
class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def stub(url, params={}):

    expected_url = f'fakemongo.com'

    if url == expected_url:
        fake_response_data = [{
            '_id': '123abc',
            'status': 'To Do',
            'item name': 'Test card'
        }]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}", instead expected "{expected_url}"')