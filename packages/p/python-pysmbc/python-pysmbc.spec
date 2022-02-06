#
# spec file for package python-pysmbc
#
# Copyright (c) 2022 SUSE LLC
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
%define         oldpython python
# Tests need a running samba server
%bcond_with     test
Name:           python-pysmbc
Version:        1.0.23
Release:        0
Summary:        Python bindings for samba clients (libsmbclient)
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/hamano/pysmbc
Source:         https://files.pythonhosted.org/packages/source/p/pysmbc/pysmbc-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(smbclient)
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
Obsoletes:      %{oldpython}-smbc < %{version}
Provides:       %{oldpython}-smbc = %{version}
Obsoletes:      python-smbc < %{version}-%{release}
Provides:       python-smbc = %{version}-%{release}
%python_subpackages

%description
This is a set of Python bindings for the libsmbclient library
from the samba project.

%prep
%setup -q -n pysmbc-%{version}
sed -i '1{/^#!.*/ d}' smbc/xattr.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
%pytest_arch
%endif

%files %{python_files}
%license COPYING
%doc NEWS
%{python_sitearch}/smbc
%{python_sitearch}/_smbc*
%{python_sitearch}/pysmbc-%{version}*-info

%changelog
