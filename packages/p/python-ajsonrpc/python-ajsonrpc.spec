#
# spec file for package python-ajsonrpc
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


%bcond_without libalternatives
Name:           python-ajsonrpc
Version:        1.2.0
Release:        0
Summary:        Async JSON-RPC 20 protocol + server powered by asyncio
License:        MIT
URL:            https://github.com/pavlov99/ajsonrpc
Source:         https://files.pythonhosted.org/packages/source/a/ajsonrpc/ajsonrpc-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
Async JSON-RPC 2.0 protocol + server powered by asyncio.

%prep
%autosetup -p1 -n ajsonrpc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/async-json-rpc-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative async-json-rpc-server

# post and postun macro call is not needed with only libalternatives

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/async-json-rpc-server
%{python_sitelib}/ajsonrpc
%{python_sitelib}/ajsonrpc-%{version}*-info

%changelog
