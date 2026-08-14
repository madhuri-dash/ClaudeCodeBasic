import time

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# --- Current behavior: GET / health check ------------------------------------

def test_health_check_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_health_check_returns_status_ok_body():
    response = client.get("/")
    assert response.json() == {"status": "OK"}


def test_health_check_rejects_post():
    response = client.post("/")
    assert response.status_code == 405


# --- PRD target behavior: GET /hola greeting endpoint ------------------------
# These encode PRD.md's functional requirements ("Serve the greeting from a
# backend API", success metric "API responds in under 300ms"). They will fail
# until GET /hola is implemented — remove the xfail marker at that point.

@pytest.mark.xfail(reason="GET /hola not implemented yet (see PRD.md)", strict=True)
def test_hola_endpoint_returns_200():
    response = client.get("/hola")
    assert response.status_code == 200


@pytest.mark.xfail(reason="GET /hola not implemented yet (see PRD.md)", strict=True)
def test_hola_endpoint_returns_expected_message():
    response = client.get("/hola")
    assert response.json() == {"message": "Hola MADHURI DASH!!"}


@pytest.mark.xfail(reason="GET /hola not implemented yet (see PRD.md)", strict=True)
def test_hola_endpoint_content_type_is_json():
    response = client.get("/hola")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")


@pytest.mark.xfail(reason="GET /hola not implemented yet (see PRD.md)", strict=True)
def test_hola_endpoint_rejects_post():
    response = client.post("/hola")
    assert response.status_code == 405


@pytest.mark.xfail(reason="GET /hola not implemented yet (see PRD.md)", strict=True)
def test_hola_endpoint_responds_within_300ms():
    # PRD success metric: "API responds in under 300ms."
    start = time.monotonic()
    response = client.get("/hola")
    elapsed_ms = (time.monotonic() - start) * 1000
    assert response.status_code == 200
    assert elapsed_ms < 300


# --- General API behavior -----------------------------------------------------

def test_unknown_route_returns_404():
    response = client.get("/does-not-exist")
    assert response.status_code == 404
