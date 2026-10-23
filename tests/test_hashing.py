import hashlib

from lyncus.hashing import hash_file


def test_hashes_match_hashlib(tmp_path):
    data = b"lyncus" * 20_000          # larger than one 64 KB chunk
    f = tmp_path / "sample.bin"
    f.write_bytes(data)

    h = hash_file(str(f))

    assert h["md5"] == hashlib.md5(data).hexdigest()
    assert h["sha1"] == hashlib.sha1(data).hexdigest()
    assert h["sha256"] == hashlib.sha256(data).hexdigest()


def test_one_byte_change_changes_hash(tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    a.write_bytes(b"hello")
    b.write_bytes(b"hellp")
    assert hash_file(str(a))["sha256"] != hash_file(str(b))["sha256"]