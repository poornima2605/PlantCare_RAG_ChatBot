import pytest
import requests

BASE_URL = "http://localhost:8000/ask"

@pytest.mark.parametrize("question, expected_keyword", [
    ("How often should I water a snake plant?", "snake"),
    ("What type of light do succulents need?", "light"),
    ("", None),  # Edge case: empty question
])
def test_query_endpoint(question, expected_keyword):
    response = requests.post(f"{BASE_URL}", json={"question": question})
    
    # Basic response check
    assert response.status_code == 200, f"Expected 200 OK but got {response.status_code}"
    
    json_response = response.json()
    assert "answer" in json_response, "Response JSON should contain 'answer'"

    if expected_keyword:
        # Check if answer is related to question (sanity check)
        assert expected_keyword in json_response["answer"].lower(), f"Expected keyword '{expected_keyword}' in answer"
    else:
        # If the question is empty, it should still handle gracefully
        assert len(json_response["answer"]) > 0, "Answer should not be empty even for empty input"
