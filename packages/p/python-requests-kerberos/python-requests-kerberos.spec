#
# spec file for package python-requests-kerberos
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


%{?sle15_python_module_pythons}
Name:           python-requests-kerberos
Version:        0.15.0
Release:        0
Summary:        A Kerberos authentication handler for python-requests
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/requests/requests-kerberos
Source:         https://files.pythonhosted.org/packages/source/r/requests-kerberos/requests_kerberos-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-pyspnego
Requires:       python-requests >= 1.1.0
BuildArch:      noarch
%python_subpackages

%description
Requests is an HTTP library, written in Python, for human beings. This library
adds optional Kerberos/GSSAPI authentication support and supports mutual
authentication. Basic GET usage:

%prep
%setup -q -n requests_kerberos-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/*

%changelog
