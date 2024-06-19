#
# spec file for package python-jsonrpclib-pelix
#
# Copyright (c) 2024 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-jsonrpclib-pelix
Version:        0.4.3.3
Release:        0
Summary:        JSPN-RPC over HTTP Library for Pelix Remote Services
License:        Apache-2.0
URL:            https://github.com/tcalmant/jsonrpclib/
Source:         https://github.com/tcalmant/jsonrpclib/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python (2 & 3) JSON-RPC over HTTP that mirrors xmlrpclib syntax.

%prep
%setup -q -n jsonrpclib-%{version}
sed -i -e 's:python$:python3:' tests/cgi-bin/cgi_server.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/*
%license LICENSE
%doc README.md

%changelog
