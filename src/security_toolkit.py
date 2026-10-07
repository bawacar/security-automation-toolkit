import argparse
import hashlib
import ipaddress
import json
from pathlib import Path

def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()

def validate_ip(value):
    try:
        ip = ipaddress.ip_address(value)
        return {"valid": True, "version": ip.version, "address": str(ip)}
    except ValueError:
        return {"valid": False, "address": value}

def main():
    parser = argparse.ArgumentParser(description="Safe security-operations utilities")
    sub = parser.add_subparsers(dest="command", required=True)

    h = sub.add_parser("hash")
    h.add_argument("path")

    i = sub.add_parser("ip")
    i.add_argument("address")

    sub.add_parser("report")

    args = parser.parse_args()

    if args.command == "hash":
        print(sha256_file(Path(args.path)))
    elif args.command == "ip":
        print(json.dumps(validate_ip(args.address), indent=2))
    elif args.command == "report":
        print(json.dumps({
            "project": "security-automation-toolkit",
            "purpose": "repeatable defensive security operations",
            "external_network_access": False
        }, indent=2))

if __name__ == "__main__":
    main()
