def test_root_redirects_to_static_index(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_all(reset_activities, client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9

    chess = data["Chess Club"]
    assert chess["description"]
    assert chess["schedule"]
    assert chess["max_participants"] == 12
    assert "participants" in chess
