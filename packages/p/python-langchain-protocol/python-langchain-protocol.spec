#
# spec file for package python-langchain-protocol
#
# Copyright (c) 2026 SUSE LLC
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


%define modname langchain_protocol
Name:           python-langchain-protocol
Version:        0.0.18
Release:        0
Summary:        Python bindings for the LangChain agent streaming protocol
License:        MIT
URL:            https://github.com/langchain-ai/agent-protocol
Source:         https://files.pythonhosted.org/packages/source/l/langchain_protocol/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module typing_extensions >= 4.13.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing_extensions >= 4.13.0
BuildArch:      noarch
%python_subpackages

%description
Python bindings for the LangChain agent streaming protocol.

This package provides generated TypedDict and Literal definitions for the
protocol's commands, events, results, and payload shapes. It does not include
a runtime client, transport, or helper APIs; it is intended as a source of
typing primitives only.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/langchain_protocol
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import langchain_protocol"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/langchain_protocol
%{python_sitelib}/langchain_protocol-%{version}.dist-info

%changelog
