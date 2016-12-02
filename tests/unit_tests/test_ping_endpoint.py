from flask import url_for

# Example of test by class
class TestApp:
    def test_ping(self, client):
        res = client.get(url_for('ping'))
        assert res.status_code == 200, 'Ensure respose 200 of endpoint ping'
        assert res.json == {'ping': 'pong'}, 'Ensure json return endpoint ping'
