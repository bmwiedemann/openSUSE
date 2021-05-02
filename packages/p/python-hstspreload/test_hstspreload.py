import base64
import hashlib
import json

import pytest
import urllib3

import hstspreload

HSTS_PRELOAD_URL = (
    "https://chromium.googlesource.com/chromium/src/+/master/"
    "net/http/transport_security_state_static.json?format=TEXT"
)


def load_test_cases():
    http = urllib3.PoolManager()
    r = http.request(
        "GET",
        HSTS_PRELOAD_URL,
        headers={"Accept": "application/json"},
        preload_content=True,
    )
    content = base64.b64decode(r.data)
    content_checksum = hashlib.sha256(content).hexdigest()

    assert content_checksum == hstspreload.__checksum__

    content = content.decode("ascii")
    entries = json.loads(
        "\n".join(
            [line for line in content.split("\n") if not line.strip().startswith("//")]
        )
    )["entries"]

    allow_subdomains = []

    for entry in sorted(entries, key=lambda x: len(x["name"])):
        host = entry["name"].encode("ascii")
        include_subdomains = entry.get("include_subdomains", False)
        force_https = entry.get("mode", "") == "force-https"

        if force_https:
            yield host, True
            if include_subdomains:
                allow_subdomains.append(b"." + host)

            # Handle cases where a subdomain like 'example.org' is
            # given 'includeSubdomains' but then the 'www.example.org'
            # entry isn't assigned 'includeSubdomains'. Thankfully
            # this isn't allowed anymore and they only accept
            # 'example.org' domains now.
            if not include_subdomains:
                for subdom in allow_subdomains:
                    if host.endswith(subdom):
                        include_subdomains = True
                        break

            yield b"zzz-subdomain." + host, include_subdomains


@pytest.mark.parametrize(
    ["host", "expected"],
    [
        (b"www.google.com", False),
        ("www.google.com", False),
        (b"google.com", False),
        ("google.com", False),
        ("paypal.com", True),
        (b"paypal.com", True),
    ],
)
def test_data_types(host, expected):
    assert hstspreload.in_hsts_preload(host) is expected


@pytest.mark.parametrize(["host", "expected"], list(load_test_cases()))
def test_in_hsts_preload(host, expected):
    assert hstspreload.in_hsts_preload(host) is expected
