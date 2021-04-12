#
# spec file for package python-ajsonrpc
#
# Copyright (c) 2021 SUSE LLC
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

%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-ajsonrpc
Version:        1.1.0
Release:        0
Summary:        Async JSON-RPC 20 protocol + server powered by asyncio
License:        MIT
URL:            https://github.com/pavlov99/ajsonrpc
Source:         https://files.pythonhosted.org/packages/source/a/ajsonrpc/ajsonrpc-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Async JSON-RPC 2.0 protocol + server powered by asyncio.

%prep
%setup -q -n ajsonrpc-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/async-json-rpc-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# 1 test fails on python 3.6
# See https://github.com/pavlov99/ajsonrpc/issues/19
%if 0%{?suse_version} > 1530
%__python38 -m unittest -v
%endif

%post
%python_install_alternative async-json-rpc-server

%postun
%python_uninstall_alternative async-json-rpc-server

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/async-json-rpc-server
%{python_sitelib}/*

%changelog
