#
# spec file for package python-langchain-anthropic
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


%{?sle15_python_module_pythons}
Name:           python-langchain-anthropic
Version:        1.4.8
Release:        0
Summary:        Integration package connecting Claude (Anthropic) APIs and LangChain
License:        MIT
URL:            https://github.com/langchain-ai/langchain
Source:         https://files.pythonhosted.org/packages/source/l/langchain_anthropic/langchain_anthropic-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anthropic >= 0.96.0
Requires:       python-langchain-core >= 1.4.7
Requires:       python-pydantic >= 2.7.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module anthropic >= 0.96.0}
BuildRequires:  %{python_module blockbuster}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module langchain-core >= 1.4.7}
BuildRequires:  %{python_module pydantic >= 2.7.4}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-socket}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module syrupy}
# /SECTION
%python_subpackages

%description
langchain-anthropic is the integration package that connects the Claude
(Anthropic) chat and language model APIs with the LangChain framework,
exposing the ChatAnthropic and AnthropicLLM classes and related middleware.

%prep
%autosetup -p1 -n langchain_anthropic-%{version}
# Drop the conftest that pulls in langchain-tests and vcrpy for the
# integration cassette tests; the offline unit tests do not need it.
rm -f tests/conftest.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Run the offline unit tests only. Skip test_standard.py (needs langchain-tests
# and pytest-benchmark, not in Factory) and the middleware tests (need
# langgraph / langchain, not in Factory); both also require network providers.
# Deselect the one chat-model test that imports langchain-tests as well.
%pytest tests/unit_tests --ignore tests/unit_tests/test_standard.py --ignore tests/unit_tests/middleware --deselect tests/unit_tests/test_chat_models.py::test_anthropic_stream_events_v3_lifecycle
# Recompile the installed modules as hash-based bytecode: this package ships
# many modules, so timestamp-based .pyc desync from the reproducibility-clamped
# .py mtimes and trip python-bytecode-inconsistent-mtime.
%python_expand $python -m compileall -q -f --invalidation-mode=unchecked-hash -o 0 -o 1 -s %{buildroot} %{buildroot}%{$python_sitelib}/langchain_anthropic
# Re-link the freshly compiled identical .pyc/.opt-1.pyc (brp-python-hardlink
# already ran before %%check).
%python_expand %fdupes %{buildroot}%{$python_sitelib}/langchain_anthropic

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/langchain_anthropic
%{python_sitelib}/langchain_anthropic-%{version}.dist-info

%changelog
