def test_unregister_removes_participant(reset_activities, client):
    email = "michael@mergington.edu"

    response = client.delete(
        "/activities/Chess Club/unregister",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from Chess Club"

    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_rejects_missing_participant(reset_activities, client):
    response = client.delete(
        "/activities/Chess Club/unregister",
        params={"email": "not.registered@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Not registered for this activity"


def test_unregister_unknown_activity_returns_404(reset_activities, client):
    response = client.delete(
        "/activities/Unknown Club/unregister",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
