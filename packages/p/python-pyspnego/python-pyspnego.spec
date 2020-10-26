#
# spec file for package python-pyspnego
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-pyspnego
Version:        0.1.2
Release:        0
Summary:        Python SPNEGO authentication library 
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jborean93/pyspnego
Source:         https://github.com/jborean93/pyspnego/archive/v%{version}.tar.gz#/pyspnego-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-cryptography
Suggests:       python-gssapi >= 1.5.0
Suggests:       python-ruamel.yaml
BuildArch:      noarch
%python_subpackages

%description
Library to handle SPNEGO (Negotiate, NTLM, Kerberos) authentication.
Also includes a packet parser that can be used to decode raw
NTLM/SPNEGO/Kerberos tokens into a human readable format.

%prep
%setup -q -n pyspnego-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyspnego-parse
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pyspnego-parse

%postun
%python_uninstall_alternative pyspnego-parse

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/pyspnego-parse
%{python_sitelib}/*

%changelog
