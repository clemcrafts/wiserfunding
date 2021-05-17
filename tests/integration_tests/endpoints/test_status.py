from . import get, put


def test_get_status():
    """
    Testing the status GET endpoint (health check).
    """
    status_code, response_data = get(url='/status', headers={})
    assert response_data == {'alive': True}
