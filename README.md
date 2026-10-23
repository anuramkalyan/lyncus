<p align="center">
  <img src="assets/logo.svg" alt="Lyncus logo" width="160">
</p>

<h1 align="center">Lyncus</h1>

<p align="center">
  <b>Offline malware triage for analysts.</b><br>
  Inspect a suspicious file without running it or uploading it anywhere.
</p>

<p align="center">
  <a href="https://github.com/anuramkalyan/lyncus/actions/workflows/tests.yml"><img src="https://github.com/anuramkalyan/lyncus/actions/workflows/tests.yml/badge.svg" alt="tests"></a>
  <img src="https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/github/license/anuramkalyan/lyncus?color=14b8a6" alt="license">
  <img src="https://img.shields.io/badge/status-early%20development-f59e0b" alt="status">
</p>

---

Lyncus fingerprints a file, identifies what it really is from its bytes,
reads Windows executable headers, and explains how urgently a human should
look at it. Named after Lynceus, the Argonaut who could see through solid objects.

## Status

Early development. Building in public as a learning project.

- [x] File hashing (MD5, SHA-1, SHA-256)
- [ ] File type detection from magic bytes
- [ ] Windows PE header analysis
- [ ] Risk score and command line
- [ ] Desktop app with drag-and-drop
- [ ] YARA rule scanning
- [ ] VirusTotal hash lookups

## Quick start

```bash
git clone https://github.com/anuramkalyan/lyncus.git
cd lyncus
python -m venv .venv
.venv\Scripts\activate        # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
python -m pytest
```

## Safety

Lyncus only reads bytes. It never opens, runs or uploads the files it scans.
Analyse unknown files inside a virtual machine.

## License

MIT, see [LICENSE](LICENSE).
