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
Version:        2.14.1
Release:        0
Summary:        Minimal CLI coding agent by Mistral
License:        Apache-2.0
URL:            https://github.com/mistralai/mistral-vibe
Source0:        https://files.pythonhosted.org/packages/source/m/mistral_vibe/mistral_vibe-%{version}.tar.gz
# PATCH-FIX-UPSTREAM build-tests.patch mcepl@suse.com
# make tests pass
Patch0:         build-tests.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.12
BuildRequires:  python3-editables
BuildRequires:  python3-hatch-vcs
BuildRequires:  python3-hatchling
BuildRequires:  python3-pip
Requires:       python3-GitPython >= 3.1.47
Requires:       python3-PyYAML >= 6.0.3
Requires:       python3-agent-client-protocol >= 0.10.1
Requires:       python3-attrs >= 26.1.0
Requires:       python3-cachetools >= 7.0.6
Requires:       python3-click >= 8.3.3
Requires:       python3-cryptography >= 47.0.0
Requires:       python3-gitdb >= 4.0.12
Requires:       python3-giturlparse >= 0.14.0
Requires:       python3-google-auth >= 2.49.2
Requires:       python3-googleapis-common-protos >= 1.74.0
Requires:       python3-httpx >= 0.28.1
Requires:       python3-humanize >= 4.15.0
Requires:       python3-jaraco.classes >= 3.4.0
Requires:       python3-jaraco.context >= 6.1.2
Requires:       python3-jaraco.functools >= 4.4.0
Requires:       python3-jeepney >= 0.9.0
Requires:       python3-Jinja2
Requires:       python3-jsonpatch >= 1.33
Requires:       python3-jsonpath-python >= 1.1.5
Requires:       python3-jsonpointer >= 3.1.1
Requires:       python3-jsonschema >= 4.26.0
Requires:       python3-jsonschema-specifications >= 2025.9.1
Requires:       python3-keyring >= 25.7.0
Requires:       python3-linkify-it-py >= 2.1.0
Requires:       python3-markdown-it-py >= 4.0.0
Requires:       python3-markdownify >= 1.2.2
Requires:       python3-mcp >= 1.27.1
Requires:       python3-mdit-py-plugins >= 0.5.0
Requires:       python3-mdurl >= 0.1.2
Requires:       python3-mcp >= 1.27.1
Requires:       python3-mistralai >= 2.4.4
Requires:       python3-more-itertools >= 11.0.2
Requires:       python3-opentelemetry-api >= 1.39.1
Requires:       python3-opentelemetry-exporter-otlp-proto-http >= 1.39.1
Requires:       python3-opentelemetry-sdk >= 1.39.1
Requires:       python3-opentelemetry-semantic-conventions >= 0.60b1
Requires:       python3-pexpect >= 4.9.0
Requires:       python3-pydantic >= 2.13.3
Requires:       python3-pydantic-settings >= 2.14.0
Requires:       python3-pyperclip >= 1.11.0
Requires:       python3-python-dotenv >= 1.2.2
Requires:       python3-rich >= 15.0.0
Requires:       python3-sounddevice >= 0.5.5
Requires:       python3-truststore >= 0.10.4
Requires:       python3-syrupy
Requires:       python3-textual >= 8.2.7
Requires:       python3-textual-speedups >= 0.2.1
Requires:       python3-tomli-w >= 1.2.0
Requires:       python3-tomlkit
Requires:       python3-tree-sitter >= 0.25.2
Requires:       python3-tree-sitter-bash >= 0.25.1
Requires:       python3-watchfiles >= 1.1.1
Requires:       python3-websockets >= 16.0
Requires:       python3-zstandard >= 0.25.0
Obsoletes:      python312-mistral-vibe < %{version}
Provides:       python312-mistral-vibe = %{version}
Obsoletes:      python313-mistral-vibe < %{version}
Provides:       python313-mistral-vibe = %{version}
Provides:       python314-mistral-vibe = %{version}
Obsoletes:      python314-mistral-vibe < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-GitPython >= 3.1.47
BuildRequires:  python3-PyYAML >= 6.0.3
BuildRequires:  python3-agent-client-protocol >= 0.10.1
BuildRequires:  python3-attrs >= 26.1.0
BuildRequires:  python3-cachetools >= 7.0.6
BuildRequires:  python3-click >= 8.3.3
BuildRequires:  python3-gitdb >= 4.0.12
BuildRequires:  python3-giturlparse >= 0.14.0
BuildRequires:  python3-google-auth >= 2.49.2
BuildRequires:  python3-googleapis-common-protos >= 1.74.0
BuildRequires:  python3-httpx >= 0.28.1
BuildRequires:  python3-humanize >= 4.15.0
BuildRequires:  python3-jaraco.classes >= 3.4.0
BuildRequires:  python3-jaraco.context >= 6.1.2
BuildRequires:  python3-jaraco.functools >= 4.4.0
BuildRequires:  python3-jeepney >= 0.9.0
BuildRequires:  python3-Jinja2
BuildRequires:  python3-jsonpatch >= 1.33
BuildRequires:  python3-jsonpath-python >= 1.1.5
BuildRequires:  python3-jsonpointer >= 3.1.1
BuildRequires:  python3-jsonschema >= 4.26.0
BuildRequires:  python3-jsonschema-specifications >= 2025.9.1
BuildRequires:  python3-keyring >= 25.7.0
BuildRequires:  python3-linkify-it-py >= 2.1.0
BuildRequires:  python3-markdown-it-py >= 4.0.0
BuildRequires:  python3-markdownify >= 1.2.2
BuildRequires:  python3-mcp >= 1.27.1
BuildRequires:  python3-mdit-py-plugins >= 0.5.0
BuildRequires:  python3-mdurl >= 0.1.2
BuildRequires:  python3-mistralai >= 2.4.4
BuildRequires:  python3-more-itertools >= 11.0.2
BuildRequires:  python3-opentelemetry-api >= 1.39.1
BuildRequires:  python3-opentelemetry-exporter-otlp-proto-http >= 1.39.1
BuildRequires:  python3-opentelemetry-sdk >= 1.39.1
BuildRequires:  python3-opentelemetry-semantic-conventions >= 0.60b1
BuildRequires:  python3-pexpect >= 4.9.0
BuildRequires:  python3-pydantic >= 2.13.3
BuildRequires:  python3-pydantic-settings >= 2.14.0
BuildRequires:  python3-pyperclip >= 1.11.0
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio >= 1.2.0
BuildRequires:  python3-pytest-textual-snapshot >= 1.1.0
BuildRequires:  python3-pytest-timeout >= 2.4.0
BuildRequires:  python3-python-dotenv >= 1.2.2
BuildRequires:  python3-respx >= 0.22.0
BuildRequires:  python3-rich >= 15.0.0
BuildRequires:  python3-sounddevice >= 0.5.5
BuildRequires:  python3-truststore >= 0.10.4
BuildRequires:  python3-syrupy
BuildRequires:  python3-textual >= 8.2.7
BuildRequires:  python3-textual-speedups >= 0.2.1
BuildRequires:  python3-tomli-w >= 1.2.0
BuildRequires:  python3-tomlkit
BuildRequires:  python3-tree-sitter >= 0.25.2
BuildRequires:  python3-tree-sitter-bash >= 0.25.1
BuildRequires:  python3-watchfiles >= 1.1.1
BuildRequires:  python3-websockets >= 16.0
BuildRequires:  python3-zstandard >= 0.25.0
BuildRequires:  python3-uv
# /SECTION

%description
Mistral Vibe is a command-line coding assistant powered by Mistral's
models. It provides a conversational interface to your codebase,
allowing you to use natural language to explore, modify, and interact
with your projects through a powerful set of tools.

%prep
%autosetup -p1 -n mistral_vibe-%{version}

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%check
PYTEST_ADDOPTS="--ignore=tests/audio_player/test_audio_player.py --timeout=60"
export PYTEST_ADDOPTS+=" --ignore=tests/audio_recorder/test_audio_recorder.py"
export PYTEST_ADDOPTS+=" --ignore=tests/snapshots"
%python3_pytest -m 'not network' -k 'not test_generic_backend_streaming_uses_ssl_cert_file'

%files
%license LICENSE
%{_bindir}/vibe
%{_bindir}/vibe-acp
%{python3_sitelib}/vibe
%{python3_sitelib}/mistral_vibe-%{version}.dist-info

%changelog
