#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Smoke-test an already built git-bug binary. Requires Python 3 and Git."""
import argparse
import gzip
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request


class Assets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        value = attrs.get("src") if tag == "script" else attrs.get("href") if tag == "link" else None
        if value and value.endswith((".js", ".css")):
            self.urls.append(value)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def smoke_test(binary):
    with tempfile.TemporaryDirectory(prefix="git-bug-webui-test-") as directory:
        work = Path(directory)
        env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        env.update(HOME=directory, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL="/dev/null")
        subprocess.run(["git", "init", "--quiet", str(work)], env=env, check=True)
        log_path = work / "server.log"
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with log_path.open("w") as log:
            server = subprocess.Popen([str(binary), "webui", "--no-open", "--read-only",
                                       "--bind", "127.0.0.1"], cwd=work, env=env,
                                      stdout=log, stderr=subprocess.STDOUT)
            try:
                base = None
                for _ in range(100):
                    text = log_path.read_text()
                    require(server.poll() is None, "Server exited:\n" + text)
                    match = re.search(r"Web UI: (http://127\.0\.0\.1:\d+)", text)
                    if match:
                        base = match[1]
                        try:
                            with opener.open(base, timeout=2) as response:
                                html = response.read()
                            break
                        except (urllib.error.URLError, ConnectionError):
                            pass
                    time.sleep(0.1)
                else:
                    raise RuntimeError("Server did not become ready:\n" + log_path.read_text())

                def get(path, compressed=False):
                    url = urllib.parse.urljoin(base, path)
                    require(urllib.parse.urlsplit(url).netloc == urllib.parse.urlsplit(base).netloc,
                            "Unexpected external asset: " + path)
                    request = urllib.request.Request(url, headers={
                        "Accept-Encoding": "gzip" if compressed else "identity"})
                    with opener.open(request, timeout=5) as response:
                        return response.read(), response.headers

                require(b"<html" in html.lower(), "Root response is not HTML")
                spa, _ = get("/_/issues")
                require(spa == html, "SPA fallback differs from root page")
                compressed, headers = get("/", True)
                require(headers.get("Content-Encoding") == "gzip", "HTML gzip response missing")
                require(gzip.decompress(compressed) == html, "Gzip HTML does not match plain response")
                parser = Assets()
                parser.feed(html.decode())
                require(any(url.endswith(".js") for url in parser.urls), "No embedded JavaScript")
                require(any(url.endswith(".css") for url in parser.urls), "No embedded stylesheet")
                fonts = set()
                for url in parser.urls:
                    plain, _ = get(url)
                    encoded, headers = get(url, True)
                    decoded = gzip.decompress(encoded) if headers.get("Content-Encoding") == "gzip" else encoded
                    require(plain and decoded == plain, "Asset encoding mismatch: " + url)
                    if url.endswith(".css"):
                        for font in re.findall(r'url\([\"\']?([^\s)\"\']+\.woff2)[\"\']?\)', plain.decode()):
                            fonts.add(urllib.parse.urljoin(url, font))
                require(fonts, "No embedded webfonts referenced by CSS")
                for font in fonts:
                    content, _ = get(font)
                    require(content.startswith(b"wOF2"), "Invalid webfont: " + font)
                request = urllib.request.Request(base + "/graphql",
                    data=json.dumps({"query": "{ __typename }"}).encode(),
                    headers={"Content-Type": "application/json"})
                with opener.open(request, timeout=5) as response:
                    result = json.load(response)
                require(result.get("data", {}).get("__typename") == "Query" and not result.get("errors"),
                        "GraphQL query failed: " + repr(result))
                print(f"PASS: HTML, SPA route, gzip, {len(parser.urls)} assets, {len(fonts)} fonts, GraphQL")
            finally:
                if server.poll() is None:
                    server.send_signal(signal.SIGINT)
                    try:
                        server.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        server.kill()
                        server.wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("binary", type=Path)
    args = parser.parse_args()
    smoke_test(args.binary.resolve())
