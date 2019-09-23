#
# spec file for package python-bcrypt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
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
%define oldpython python
Name:           python-bcrypt
Version:        3.1.7
Release:        0
Summary:        BSD type 2a and 2b password hashing
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pyca/bcrypt/
Source:         https://files.pythonhosted.org/packages/source/b/bcrypt/bcrypt-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest >= 3.2.1}
BuildRequires:  %{python_module setuptools >= 40.8.0}
BuildRequires:  %{python_module six >= 1.4.1}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libffi)
Requires:       python-six >= 1.4.1
%requires_eq    python-cffi
Provides:       python-py-bcrypt = %{version}
Obsoletes:      python-py-bcrypt < %{version}
# This is intended as a drop-in replacement for py-bcrypt
%ifpython2
Provides:       %{oldpython}-py-bcrypt = %{version}
Obsoletes:      %{oldpython}-py-bcrypt < %{version}
%endif
%python_subpackages

%description
This Python module supports creating (and verifying) password hashes
using the BSD-originating hashing methods known as "2a" and "2b".

%prep
%setup -q -n bcrypt-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}/%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/bcrypt
%{python_sitearch}/bcrypt-%{version}-py*.egg-info

%changelog
