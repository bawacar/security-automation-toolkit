# Security Automation Toolkit

A small Python toolkit demonstrating repeatable security-operations automation.

## Features

- IOC validation for documentation-safe IP addresses/domains
- SHA-256 file hashing
- structured JSON reporting
- deterministic output
- command-line interface

## Why it matters

Security teams routinely automate repetitive tasks so analysts can spend more time on investigation and decision-making.

The project demonstrates the engineering pattern:

**Input → Validate → Process → Report**

## Usage

Hash a file:

```bash
python src/security_toolkit.py hash path/to/file
```

Validate a documentation IP:

```bash
python src/security_toolkit.py ip 192.0.2.10
```

Create a JSON report:

```bash
python src/security_toolkit.py report
```

## Safety

The toolkit deliberately does not perform scanning, exploitation, credential collection or interaction with third-party systems.

## Future improvements

- CSV ingestion
- STIX-compatible export
- SIEM webhook integration
- unit-test coverage
- structured logging
