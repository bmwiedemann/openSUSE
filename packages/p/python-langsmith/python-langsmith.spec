#
# spec file for package python-langsmith
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-langsmith
Version:        0.1.52
Release:        0
Summary:        Interact with langsmitt platform
License:        MIT
URL:            https://github.com/langchain-ai/langsmith-sdk
Source:         https://github.com/langchain-ai/langsmith-sdk/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module dataclasses-json}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module marshmallow}
BuildRequires:  %{python_module orjson}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-inspect}
BuildRequires:  fdupes
Requires:       python-orjson
Requires:       python-pydantic
Requires:       python-requests
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
LangSmith helps your team debug, evaluate, and monitor your language models and
intelligent agents. It works with any LLM Application, including a native
integration with the LangChain Python and LangChain JS open source libraries.

%prep
%autosetup -n langsmith-sdk-%{version}

%build
cd python
%pyproject_wheel

%install
cd python
%pyproject_install
%python_clone -a %{buildroot}/%{_bindir}/langsmith
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/

%check
cd python/tests/unit_tests
%pytest -k 'not test_client_gc and not test_git_info and not test_as_runnable'

%post
%{python_install_alternative langsmith}

%postun
%{python_uninstall_alternative langsmith}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/langsmith
%{python_sitelib}/langsmith-%{version}.dist-info
%python_alternative %{_bindir}/langsmith

%changelog
