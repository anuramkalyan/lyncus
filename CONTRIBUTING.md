# Contributing to Lyncus

Thanks for your interest! Lyncus is an early-stage learning project, and contributions are welcome.

## Getting started

1. Fork the repo and clone your fork.
2. Create a virtual environment and run `pip install -r requirements.txt`.
3. Make sure `python -m pytest` passes before you change anything.

## Making a change

- Open an issue first for anything bigger than a small fix.
- Add a test for every new detection: one test that it fires, one that it stays quiet on a clean file.
- Keep each pull request focused on one thing.

## Ground rules

- **Never commit malware samples.** Create test data in code, or share a SHA-256 hash.
- **Lyncus must never execute or upload a scanned file.**
- Report security issues privately, as described in [SECURITY.md](SECURITY.md).
