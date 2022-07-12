# APP TESTING
# tests/test_app.py

import unittest
import os
from app import app

os.environ['TESTING'] = 'true'

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200

        html = response.get_data(as_text=True)
        assert "<title>Talike Bennett's MLH Portfolio</title>" in html

    def test_about_me(self):
        response = self.client.get("/static/Talike.jpg")
        assert response.status_code == 200

    def test_timeline(self):
        response = self.client.get("/api/timeline-post/")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) > 0

        response2 = self.client.post("/api/timeline-post/", data={
            "name": "MLH Fellow",
            "email": "MLHFellow@MLH.com",
            "content": "Production engineering is fun.",
        })
        assert response2.status_code == 200

        response3 = self.client.get("/api/timeline-posts/")
        assert response3.status_code == 404

    # Edge cases
    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline-post/", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline-post/", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline-post/", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
