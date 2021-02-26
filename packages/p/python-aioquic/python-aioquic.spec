#
# spec file for package python-aioquic
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-aioquic
Version:        0.9.7
Release:        0
Summary:        Python implementation of QUIC and HTTP/3
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/aiortc/aioquic
Source:         https://files.pythonhosted.org/packages/source/a/aioquic/aioquic-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(openssl)
Requires:       python-certifi
Requires:       python-cryptography >= 2.5
Requires:       python-pylsqpack >= 0.3.3
Requires:       (python-dataclasses if python-base < 3.8)
# SECTION test requirements
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module cryptography >= 2.5}
BuildRequires:  %{python_module pylsqpack >= 0.3.3}
BuildRequires:  (python3-dataclasses if python3-base < 3.8)
BuildRequires:  (python36-dataclasses if python36-base)
# /SECTION
%python_subpackages

%description
An implementation of QUIC and HTTP/3.

%prep
%setup -q -n aioquic-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%{python_expand rm %{buildroot}%{$python_sitearch}/aioquic/*.c
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%pyunittest_arch -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
