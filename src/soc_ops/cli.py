from __future__ import annotations

import argparse
import ipaddress
import json
from pathlib import Path
import re
import sys
from typing import Any

from soc_ops.config import load_config

DOMAIN_PATTERN = re.compile(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b")
SHA256_PATTERN = re.compile(r"\b[a-fA-F0-9]{64}\b")


def _extract_iocs(text: str) -> dict[str, list[str]]:
    ips: set[str] = set()
    domains = set(DOMAIN_PATTERN.findall(text))
    hashes = set(SHA256_PATTERN.findall(text))

    for token in re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", text):
        try:
            ipaddress.ip_address(token)
        except ValueError:
            continue
        ips.add(token)

    return {
        "ipv4": sorted(ips),
        "domains": sorted(domains),
        "sha256": sorted(hashes),
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="socops", description="SOC ops toolkit")
    parser.add_argument("--config", type=str, default=None, help="Path to YAML config")

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("health", help="Run a lightweight health check")

    parse_ioc = subparsers.add_parser("parse-ioc", help="Extract basic IOCs from text")
    parse_ioc.add_argument("--text", required=True, help="Input text to parse")

    return parser


def _cmd_health(config: dict[str, Any]) -> int:
    output = {
        "status": "ok",
        "config_loaded": bool(config),
        "enabled_sources": config.get("sources", []),
    }
    print(json.dumps(output, indent=2))
    return 0


def _cmd_parse_ioc(text: str) -> int:
    print(json.dumps(_extract_iocs(text), indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    config = load_config(Path(args.config)) if args.config else load_config()

    if args.command == "health":
        return _cmd_health(config)
    if args.command == "parse-ioc":
        return _cmd_parse_ioc(args.text)

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
