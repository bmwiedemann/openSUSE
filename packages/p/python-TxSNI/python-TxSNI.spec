#
# spec file for package python-TxSNI
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
Name:           python-TxSNI
Version:        0.2.0
Release:        0
Summary:        Python module for running a TLS server with Twisted
License:        MIT
URL:            https://github.com/glyph/txsni
Source0:        https://github.com/glyph/txsni/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module Twisted-tls >= 14.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyOpenSSL >= 0.14}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted-tls >= 14.0.0
Requires:       python-pyOpenSSL >= 0.14
BuildArch:      noarch
%python_subpackages

%description
This package brings support for running a TLS server with Twisted.

%prep
%setup -q -n txsni-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/[Tt]x[Ss][Nn][Ii]
%{python_sitelib}/[Tt]x[Ss][Nn][Ii]-%{version}.dist-info
%{python_sitelib}/twisted/plugins/txsni_endpoint.py
%pycache_only %{python_sitelib}/twisted/plugins/__pycache__/txsni_endpoint*

%changelog
