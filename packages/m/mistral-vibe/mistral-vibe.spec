#
# spec file for package python-mistral-vibe
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           mistral-vibe
Version:        2.19.1
Release:        0
Summary:        Minimal CLI coding agent by Mistral
License:        Apache-2.0
URL:            https://github.com/mistralai/mistral-vibe
Source0:        https://github.com/mistralai/mistral-vibe/archive/refs/tags/v%{version}.tar.gz#/mistral-vibe-%{version}.tar.gz
# PATCH-FIX-OPENSUSE no_network.patch gh#mistralai/mistral-vibe!893 mcepl@suse.com
# make the test suite work in the network isolated environment
Patch0:         no_network.patch
# PATCH-FIX-UPSTREAM fix_tests.patch gh#mistralai/mistral-vibe!796 mcepl@suse.com
# Fix test failures in build environments
Patch1:         fix_tests.patch
# PATCH-FIX-UPSTREAM no_terminal.patch gh#mistralai/mistral-vibe!884 mcepl@suse.com
# Stabilize the tests to work on slow build environments
Patch2:         no_terminal.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.12
BuildRequires:  python3-editables
BuildRequires:  python3-hatch-vcs
BuildRequires:  python3-hatchling
BuildRequires:  python3-pip
Requires:       python3-GitPython >= 3.1.50
Requires:       python3-Jinja2
Requires:       python3-PyJWT >= 2.13.0
Requires:       python3-PyYAML >= 6.0.3
Requires:       python3-SecretStorage >= 3.5.0
Requires:       python3-agent-client-protocol >= 0.10.1
Requires:       python3-annotated-types >= 0.7.0
Requires:       python3-attrs >= 26.1.0
Requires:       python3-beautifulsoup4 >= 4.14.3
Requires:       python3-cachetools >= 7.0.6
# Requires:       python3-certifi >= 2026.6.17
Requires:       python3-certifi >= 2026.5.20
Requires:       python3-cffi >= 2.0.0
Requires:       python3-charset-normalizer >= 3.4.7
Requires:       python3-click >= 8.3.3
Requires:       python3-cryptography >= 48.0.1
Requires:       python3-eval-type-backport >= 0.3.1
Requires:       python3-gitdb >= 4.0.12
Requires:       python3-giturlparse >= 0.15.0
Requires:       python3-google-auth >= 2.49.2
Requires:       python3-googleapis-common-protos >= 1.74.0
Requires:       python3-h11 >= 0.16.0
Requires:       python3-httpcore >= 1.0.9
Requires:       python3-httpx >= 0.28.1
Requires:       python3-httpx-sse >= 0.4.3
# Requires:       python3-humanize >= 4.16.0
Requires:       python3-humanize >= 4.15.0
Requires:       python3-idna >= 3.18
Requires:       python3-importlib-metadata >= 8.7.1
Requires:       python3-jaraco.classes >= 3.4.0
Requires:       python3-jaraco.context >= 6.1.2
Requires:       python3-jaraco.functools >= 4.4.0
Requires:       python3-jeepney >= 0.9.0
Requires:       python3-jsonpatch >= 1.33
Requires:       python3-jsonpath-python >= 1.1.5
Requires:       python3-jsonpointer >= 3.1.1
Requires:       python3-jsonschema >= 4.26.0
Requires:       python3-jsonschema-specifications >= 2025.9.1
Requires:       python3-keyring >= 25.7.0
Requires:       python3-linkify-it-py >= 2.1.0
Requires:       python3-markdown-it-py >= 4.0.0
Requires:       python3-markdownify >= 1.2.2
Requires:       python3-mcp >= 1.28.1
Requires:       python3-mdit-py-plugins >= 0.5.0
Requires:       python3-mdurl >= 0.1.2
Requires:       python3-mistralai >= 2.5.0
Requires:       python3-more-itertools >= 11.0.2
Requires:       python3-opentelemetry-api >= 1.39.1
Requires:       python3-opentelemetry-exporter-otlp-proto-http >= 1.39.1
Requires:       python3-opentelemetry-proto >= 1.39.1
Requires:       python3-opentelemetry-sdk >= 1.39.1
Requires:       python3-opentelemetry-semantic-conventions >= 0.60b1
Requires:       python3-packaging >= 26.2
Requires:       python3-pexpect >= 4.9.0
Requires:       python3-platformdirs >= 4.9.6
Requires:       python3-protobuf >= 6.33.6
Requires:       python3-ptyprocess >= 0.7.0
Requires:       python3-pyasn1 >= 0.6.3
Requires:       python3-pyasn1-modules >= 0.4.2
Requires:       python3-pycparser >= 3.0
Requires:       python3-pydantic >= 2.13.4
Requires:       python3-pydantic-settings >= 2.14.2
Requires:       python3-pygments >= 2.20.0
Requires:       python3-pyperclip >= 1.11.0
Requires:       python3-python-dateutil >= 2.9.0.post0
Requires:       python3-python-dotenv >= 1.2.2
Requires:       python3-python-multipart >= 0.0.32
Requires:       python3-referencing >= 0.37.0
Requires:       python3-requests >= 2.34.2
Requires:       python3-rich >= 15.0.0
Requires:       python3-rpds-py >= 0.30.0
# Requires:       python3-sentry-sdk >= 2.64.0
Requires:       python3-sentry-sdk >= 2.63.0
Requires:       python3-six >= 1.17.0
Requires:       python3-smmap >= 5.0.3
Requires:       python3-sounddevice >= 0.5.5
Requires:       python3-soupsieve >= 2.8.3
Requires:       python3-sse-starlette >= 3.4.1
Requires:       python3-starlette >= 1.0.0
Requires:       python3-syrupy
# Requires:       python3-textual >= 8.2.8
Requires:       python3-textual >= 8.2.7
Requires:       python3-textual-speedups >= 0.2.1
Requires:       python3-tomli-w >= 1.2.0
Requires:       python3-tomlkit
Requires:       python3-tree-sitter >= 0.25.2
Requires:       python3-tree-sitter-bash >= 0.25.1
Requires:       python3-truststore >= 0.10.4
Requires:       python3-typing-extensions >= 4.15.0
Requires:       python3-typing-inspection >= 0.4.2
Requires:       python3-uc-micro-py >= 2.0.0
Requires:       python3-urllib3 >= 2.7.0
# Requires:       python3-uvicorn >= 0.46.0
Requires:       python3-uvicorn >= 0.41.0
# Requires:       python3-watchfiles >= 1.2.0
Requires:       python3-watchfiles >= 1.1.1
Requires:       python3-websockets >= 16.0
Requires:       python3-zipp >= 3.23.1
Requires:       python3-zstandard >= 0.25.0
Obsoletes:      python312-mistral-vibe < %{version}
Provides:       python312-mistral-vibe = %{version}
Obsoletes:      python313-mistral-vibe < %{version}
Provides:       python313-mistral-vibe = %{version}
Provides:       python314-mistral-vibe = %{version}
Obsoletes:      python314-mistral-vibe < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  ca-certificates
BuildRequires:  ca-certificates-mozilla
BuildRequires:  python3-GitPython >= 3.1.50
BuildRequires:  python3-Jinja2
BuildRequires:  python3-PyJWT >= 2.13.0
BuildRequires:  python3-PyYAML >= 6.0.3
BuildRequires:  python3-SecretStorage >= 3.5.0
BuildRequires:  python3-agent-client-protocol >= 0.10.1
BuildRequires:  python3-annotated-types >= 0.7.0
BuildRequires:  python3-attrs >= 26.1.0
BuildRequires:  python3-beautifulsoup4 >= 4.14.3
BuildRequires:  python3-cachetools >= 7.0.6
# BuildRequires:  python3-certifi >= 2026.6.17
BuildRequires:  python3-certifi >= 2026.5.20
BuildRequires:  python3-cffi >= 2.0.0
BuildRequires:  python3-charset-normalizer >= 3.4.7
BuildRequires:  python3-click >= 8.3.3
BuildRequires:  python3-cryptography >= 48.0.1
BuildRequires:  python3-eval-type-backport >= 0.3.1
BuildRequires:  python3-gitdb >= 4.0.12
BuildRequires:  python3-giturlparse >= 0.15.0
BuildRequires:  python3-google-auth >= 2.49.2
BuildRequires:  python3-googleapis-common-protos >= 1.74.0
BuildRequires:  python3-h11 >= 0.16.0
BuildRequires:  python3-httpcore >= 1.0.9
BuildRequires:  python3-httpx >= 0.28.1
BuildRequires:  python3-httpx-sse >= 0.4.3
# BuildRequires:  python3-humanize >= 4.16.0
BuildRequires:  python3-humanize >= 4.15.0
BuildRequires:  python3-idna >= 3.18
BuildRequires:  python3-importlib-metadata >= 8.7.1
BuildRequires:  python3-jaraco.classes >= 3.4.0
BuildRequires:  python3-jaraco.context >= 6.1.2
BuildRequires:  python3-jaraco.functools >= 4.4.0
BuildRequires:  python3-jeepney >= 0.9.0
BuildRequires:  python3-jsonpatch >= 1.33
BuildRequires:  python3-jsonpath-python >= 1.1.5
BuildRequires:  python3-jsonpointer >= 3.1.1
BuildRequires:  python3-jsonschema >= 4.26.0
BuildRequires:  python3-jsonschema-specifications >= 2025.9.1
BuildRequires:  python3-keyring >= 25.7.0
BuildRequires:  python3-linkify-it-py >= 2.1.0
BuildRequires:  python3-markdown-it-py >= 4.0.0
BuildRequires:  python3-markdownify >= 1.2.2
BuildRequires:  python3-mcp >= 1.28.1
BuildRequires:  python3-mdit-py-plugins >= 0.5.0
BuildRequires:  python3-mdurl >= 0.1.2
BuildRequires:  python3-mistralai >= 2.5.0
BuildRequires:  python3-more-itertools >= 11.0.2
BuildRequires:  python3-opentelemetry-api >= 1.39.1
BuildRequires:  python3-opentelemetry-exporter-otlp-proto-http >= 1.39.1
BuildRequires:  python3-opentelemetry-proto >= 1.39.1
BuildRequires:  python3-opentelemetry-sdk >= 1.39.1
BuildRequires:  python3-opentelemetry-semantic-conventions >= 0.60b1
BuildRequires:  python3-packaging >= 26.2
BuildRequires:  python3-pexpect >= 4.9.0
BuildRequires:  python3-platformdirs >= 4.9.6
BuildRequires:  python3-protobuf >= 6.33.6
BuildRequires:  python3-ptyprocess >= 0.7.0
BuildRequires:  python3-pyasn1 >= 0.6.3
BuildRequires:  python3-pyasn1-modules >= 0.4.2
BuildRequires:  python3-pycparser >= 3.0
BuildRequires:  python3-pydantic >= 2.13.4
BuildRequires:  python3-pydantic-settings >= 2.14.2
BuildRequires:  python3-pygments >= 2.20.0
BuildRequires:  python3-pyperclip >= 1.11.0
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xdist >= 3.8.0
BuildRequires:  python3-pytest-asyncio >= 1.2.0
BuildRequires:  python3-pytest-textual-snapshot >= 1.1.0
BuildRequires:  python3-pytest-timeout >= 2.4.0
BuildRequires:  python3-python-dateutil >= 2.9.0.post0
BuildRequires:  python3-python-dotenv >= 1.2.2
BuildRequires:  python3-python-multipart >= 0.0.32
BuildRequires:  python3-referencing >= 0.37.0
BuildRequires:  python3-respx >= 0.22.0
BuildRequires:  python3-rich >= 15.0.0
BuildRequires:  python3-rpds-py >= 0.30.0
# BuildRequires:  python3-sentry-sdk >= 2.64.0
BuildRequires:  python3-sentry-sdk >= 2.63.0
BuildRequires:  python3-sounddevice >= 0.5.5
BuildRequires:  python3-soupsieve >= 2.8.3
BuildRequires:  python3-sse-starlette >= 3.4.1
BuildRequires:  python3-starlette >= 1.0.0
BuildRequires:  python3-syrupy
# BuildRequires:  python3-textual >= 8.2.8
BuildRequires:  python3-textual >= 8.2.7
BuildRequires:  python3-textual-speedups >= 0.2.1
BuildRequires:  python3-tomli-w >= 1.2.0
BuildRequires:  python3-tomlkit
BuildRequires:  python3-tree-sitter >= 0.25.2
BuildRequires:  python3-tree-sitter-bash >= 0.25.1
BuildRequires:  python3-truststore >= 0.10.4
BuildRequires:  python3-typing-extensions >= 4.15.0
BuildRequires:  python3-typing-inspection >= 0.4.2
BuildRequires:  python3-uc-micro-py >= 2.0.0
BuildRequires:  python3-urllib3 >= 2.7.0
BuildRequires:  python3-uv
# BuildRequires:  python3-uvicorn >= 0.46.0
BuildRequires:  python3-uvicorn >= 0.41.0
# BuildRequires:  python3-watchfiles >= 1.2.0
BuildRequires:  python3-watchfiles >= 1.1.1
BuildRequires:  python3-websockets >= 16.0
BuildRequires:  python3-zipp >= 3.23.1
BuildRequires:  python3-zstandard >= 0.25.0
# /SECTION

%description
Mistral Vibe is a command-line coding assistant powered by Mistral's
models. It provides a conversational interface to your codebase,
allowing you to use natural language to explore, modify, and interact
with your projects through a powerful set of tools.

%prep
%autosetup -p1

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%check
export PYTHONTRACEMALLOC=20
PYTEST_ADDOPTS="--ignore=tests/audio_player/test_audio_player.py --timeout=60"
export PYTEST_ADDOPTS+=" --ignore=tests/audio_recorder/test_audio_recorder.py"
export PYTEST_ADDOPTS+=" --ignore=tests/snapshots"
%python3_pytest -m 'not (network or terminal)' -k 'not test_generic_backend_streaming_uses_ssl_cert_file'

%files
%license LICENSE
%{_bindir}/vibe
%{_bindir}/vibe-acp
%{python3_sitelib}/vibe
%{python3_sitelib}/mistral_vibe-%{version}.dist-info

%changelog
