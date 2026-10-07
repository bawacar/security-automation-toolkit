from src.security_toolkit import validate_ip

def test_valid_documentation_ip():
    result = validate_ip("192.0.2.10")
    assert result["valid"] is True
    assert result["version"] == 4

def test_invalid_ip():
    assert validate_ip("not-an-ip")["valid"] is False
