#
# spec file for package python-langsmith
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-langsmith
Version:        0.10.5
Release:        0
Summary:        Client library for the LangSmith LLM tracing and evaluation platform
License:        MIT
URL:            https://github.com/langchain-ai/langsmith-sdk
Source:         https://files.pythonhosted.org/packages/source/l/langsmith/langsmith-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 3.5.0
Requires:       python-distro >= 1.7.0
Requires:       python-httpx >= 0.23.0
Requires:       python-orjson >= 3.9.14
Requires:       python-packaging >= 23.2
Requires:       python-pydantic >= 2
Requires:       python-requests >= 2.0.0
Requires:       python-requests-toolbelt >= 1.0.0
Requires:       python-sniffio >= 1.1
Requires:       python-typing_extensions >= 4.0.0
Requires:       python-uuid-utils >= 0.12.0
Requires:       python-websockets >= 14.2
Requires:       python-xxhash >= 3.0.0
Requires:       python-zstandard >= 0.22.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module anyio >= 3.5.0}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module dataclasses-json}
BuildRequires:  %{python_module distro >= 1.7.0}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module httpx >= 0.23.0}
BuildRequires:  %{python_module multipart}
BuildRequires:  %{python_module opentelemetry-sdk >= 1.30.0}
BuildRequires:  %{python_module orjson >= 3.9.14}
BuildRequires:  %{python_module packaging >= 23.2}
BuildRequires:  %{python_module pydantic >= 2}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.0.0}
BuildRequires:  %{python_module requests-toolbelt >= 1.0.0}
BuildRequires:  %{python_module sniffio >= 1.1}
BuildRequires:  %{python_module typing_extensions >= 4.0.0}
BuildRequires:  %{python_module uuid-utils >= 0.12.0}
BuildRequires:  %{python_module websockets >= 14.2}
BuildRequires:  %{python_module xxhash >= 3.0.0}
BuildRequires:  %{python_module zstandard >= 0.22.0}
# /SECTION
%python_subpackages

%description
LangSmith helps your team debug, evaluate, and monitor your language models and
intelligent agents. It works with any LLM Application, including a native
integration with the LangChain Python and LangChain JS open source libraries.

%prep
%autosetup -p1 -n langsmith-%{version}
# Drop the doctest conftest that pulls in vcrpy and patches network libraries
rm -f conftest.py

%build
%pyproject_wheel

%install
%pyproject_install
# Recompile the installed modules as hash-based bytecode: this package ships
# many modules, so timestamp-based .pyc desync from the reproducibility-clamped
# .py mtimes and trip python-bytecode-inconsistent-mtime.
%python_expand $python -m compileall -q -f --invalidation-mode=unchecked-hash -o 0 -o 1 -s %{buildroot} %{buildroot}%{$python_sitelib}/langsmith
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANGSMITH_TRACING=false
# Run unit tests only; skip integration/network tests and modules that need
# optional providers (LLM wrappers, sandbox websockets client, CLI) or
# langchain-core (which depends on langsmith -> build cycle);
# test_hybrid_tracing.py carries an upstream module-level pytest.skip.
%pytest tests/unit_tests -p no:langsmith_plugin --ignore tests/unit_tests/wrappers --ignore tests/unit_tests/sandbox --ignore tests/unit_tests/cli --ignore tests/unit_tests/evaluation --ignore tests/unit_tests/test_async_client.py --ignore tests/unit_tests/test_client.py --ignore tests/unit_tests/test_run_helpers.py --ignore tests/unit_tests/test_hybrid_tracing.py -k 'not test_client_gc and not test_git_info and not test_as_runnable'

%files %{python_files}
%doc README.md
%{python_sitelib}/langsmith
%{python_sitelib}/langsmith-%{version}.dist-info

%changelog
