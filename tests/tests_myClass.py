from src.myClass import GoogleConnector

def test_google_connector():
    google_connector = GoogleConnector()
    google_connector.connect()
    google_connector.close()
    # Add assertions to verify the behavior
    # For example, check if the connection was successful
    # You can also check for specific content in the response
    assert True  # If the test runs without raising an exception, it will pass
