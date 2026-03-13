from soc_ops.cli import _extract_iocs


def test_extract_iocs_finds_ipv4_domain_and_sha256() -> None:
    text = (
        "Investigate 8.8.8.8 and host evil.example.com with hash "
        "a3f5d4e9c6b1a2f7d8e0c1b2a3d4f5e6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
    )

    result = _extract_iocs(text)

    assert result["ipv4"] == ["8.8.8.8"]
    assert result["domains"] == ["evil.example.com"]
    assert len(result["sha256"]) == 1


def test_extract_iocs_ignores_invalid_ip() -> None:
    text = "Invalid 999.10.10.10 but valid 10.0.0.1"

    result = _extract_iocs(text)

    assert result["ipv4"] == ["10.0.0.1"]
