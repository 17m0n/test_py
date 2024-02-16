import requests

def test_unsuccessful_request_data_format():

    response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params={'status': 'unavailable'})

    assert response.headers'Content-Type' == 'application/json', "Response is not in JSON format"

    try:
        data = response.json()
        assert 'id' in data0, "Field 'id' not found in the response data"
        assert 'name' in data0, "Field 'name' not found in the response data"

    except ValueError:
        assert False, "Response is not valid JSON"

    print("Test is successfully!")

test_unsuccessful_request_data_format()
