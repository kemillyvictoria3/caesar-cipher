from caesar_cipher import create_app

def test_home_page():
    flak_app = create_app()

    with flak_app.test_client() as test_clent: 
        response = test_clent.get('/')
        assert response.status_code == 200 