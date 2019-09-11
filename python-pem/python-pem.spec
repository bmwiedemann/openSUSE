#
# spec file for package python-pem
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pem
Version:        19.1.0
Release:        0
Summary:        PEM file parsing in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hynek/pem
Source0:        https://github.com/hynek/pem/archive/%{version}/%{name}-%{version}.tar.gz
# extra
BuildRequires:  %{python_module Sphinx}
# extra dev
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
pem is a Python module for parsing and splitting of PEM files,
i.e. Base64 encoded DER keys and certificates.

%prep
%setup -q -n pem-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
rm -f %{buildroot}/%{python_sitelib}/pem/py.typed #zero length
rm -f %{buildroot}/%{python3_sitelib}/pem/py.typed #zero length

%check
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
