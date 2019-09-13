#
# spec file for package python-TxSNI
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
Name:           python-TxSNI
Version:        0.1.9
Release:        0
Summary:        Python module for running a TLS server with Twisted
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/glyph/txsni
Source0:        https://github.com/glyph/txsni/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         openssl111.patch
BuildRequires:  %{python_module Twisted} >= 14.0.0
BuildRequires:  %{python_module pyOpenSSL} >= 0.14
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted >= 14.0.0
Requires:       python-pyOpenSSL >= 0.14
BuildArch:      noarch
%python_subpackages

%description
This package brings support for running a TLS server with Twisted.

%prep
%setup -q -n txsni-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
