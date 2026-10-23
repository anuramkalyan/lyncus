# Lyncus

**Offline malware triage for analysts.** Lyncus inspects a suspicious file
without running it or uploading it anywhere: it fingerprints it, identifies
what it really is, and explains how urgently a human should look at it.

> Named after Lynceus, the Argonaut who could see through solid objects.

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
