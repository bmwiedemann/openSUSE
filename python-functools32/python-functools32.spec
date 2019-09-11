#
# spec file for package python-functools32
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           python-functools32
# Dashes are not allowed in version numbers
Version:        3.2.3.2
Release:        0
%define tarver  3.2.3-2
Summary:        Backport of the functools module from Python 3.2
License:        Python-2.0
Group:          Development/Languages/Python
Url:            https://github.com/MiCHiLU/python-functools32
Source:         https://pypi.python.org/packages/source/f/functools32/functools32-%{tarver}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-nose
# For singlespec compatibility
Provides:       python2-functools32 = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a backport of the functools standard library module from
Python 3.2.3 for use on Python 2.7 and PyPy. It includes
new features `lru_cache` (Least-recently-used cache decorator).

%prep
%setup -q -n functools32-%{tarver}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
nosetests

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE
%{python_sitelib}/*

%changelog
