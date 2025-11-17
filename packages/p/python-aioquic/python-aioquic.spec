#
# spec file for package python-aioquic
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
Name:           python-aioquic
Version:        1.3.0
Release:        0
Summary:        Python implementation of QUIC and HTTP/3
License:        BSD-3-Clause
URL:            https://github.com/aiortc/aioquic
Source:         https://files.pythonhosted.org/packages/source/a/aioquic/aioquic-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(openssl)
Requires:       python-certifi
Requires:       python-cryptography >= 3.1
Requires:       python-pyOpenSSL >= 22
Requires:       python-pylsqpack >= 0.3.3
Requires:       python-service_identity
# SECTION test requirements
BuildRequires:  %{python_module service_identity}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module cryptography >= 2.5}
BuildRequires:  %{python_module pyOpenSSL >= 20}
BuildRequires:  %{python_module pylsqpack >= 0.3.3}
# /SECTION
%python_subpackages

%description
A library for the QUIC network protocol in Python. It features a minimal TLS
1.3 implementation, a QUIC stack and an HTTP/3 stack.

%prep
%autosetup -p1 -n aioquic-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm %{buildroot}%{$python_sitearch}/aioquic/*.c
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%pyunittest_arch -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/aioquic
%{python_sitearch}/aioquic-%{version}.dist-info

%changelog
