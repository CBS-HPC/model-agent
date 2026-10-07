import pytest

from cbs_model_agent import checks


def test_https_required():
    with pytest.raises(ValueError, match="HTTPS"):
        checks.validate_base_url("http://untrusted.example/openai/v1")
    with pytest.raises(ValueError, match="credentials"):
        checks.validate_base_url("https://secret@example.org/openai/v1")


@pytest.mark.parametrize("failure", [None, "incomplete_stream", "accept_any_key", "response_model"])
def test_chat_contract_and_auth_with_real_http_fixture(api, monkeypatch, failure):
    url, handler = api
    # Only this local fixture bypasses production's HTTPS validation.
    monkeypatch.setattr(checks, "validate_base_url", lambda value: value)
    if failure:
        setattr(handler, failure, "wrong-model" if failure == "response_model" else True)
    result = checks.check_endpoint(url, "test-model", "testing-key", include_models=False, timeout=30)
    assert result["passed"] == (failure is None)
    assert len(result["checks"]) == 4
    assert "testing-key" not in str(result)
