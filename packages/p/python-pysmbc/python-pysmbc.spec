#
# spec file for package python-pysmbc
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
%define         oldpython python
# Tests don't work in rpmbuild sandbox
%bcond_with     test
Name:           python-pysmbc
Version:        1.0.16
Release:        0
Summary:        Python bindings for samba clients (libsmbclient)
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            http://cyberelk.net/tim/software/pysmbc/
Source:         https://files.pythonhosted.org/packages/source/p/pysmbc/pysmbc-%{version}.tar.bz2
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libsmbclient-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module nose}
%endif
%ifpython2
Obsoletes:      %{oldpython}-smbc < %{version}
Provides:       %{oldpython}-smbc = %{version}
%endif
%ifpython3
Obsoletes:      python3-smbc < %{version}
Provides:       python3-smbc = %{version}
%endif
%python_subpackages

%description
This is a set of Python bindings for the libsmbclient library
from the samba project.

%prep
%setup -q -n pysmbc-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%{python_expand chmod a+x %{buildroot}%{$python_sitearch}/smbc/xattr.py
sed -i "s|^#!%{_bindir}/python$|#!%__$python|" %{buildroot}%{$python_sitearch}/smbc/xattr.py
$python -m compileall -d %{$python_sitearch} %{buildroot}%{$python_sitearch}/smbc/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitearch}/smbc/
%fdupes %{buildroot}%{$python_sitearch}
}

%if %{with test}
%check
pushd tests
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -B -m nose .
}
%endif

%files %{python_files}
%license COPYING
%doc NEWS
%{python_sitearch}/*

%changelog
