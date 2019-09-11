#
# spec file for package python-singledispatch
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


Name:           python-singledispatch
Version:        3.4.0.3
Release:        0
Summary:        Provides functools.singledispatch for Python 2.x
License:        Python-2.0 AND MIT
Group:          Development/Languages/Python
URL:            https://bitbucket.org/ambv/singledispatch
Source:         https://pypi.python.org/packages/source/s/singledispatch/singledispatch-%{version}.tar.gz
Source1:        https://bitbucket.org/ambv/singledispatch/raw/default/test_singledispatch.py
Source2:        https://raw.githubusercontent.com/python/cpython/master/LICENSE
BuildRequires:  python-setuptools
Provides:       python2-singledispatch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
BuildRequires:  python-ordereddict
Requires:       python-ordereddict
%else
BuildArch:      noarch
%endif

%description
PEP 443 proposed to expose a mechanism in the functools standard library module
in Python 3.4 that provides a simple form of generic programming known as
single-dispatch generic functions.

This library is a backport of this functionality to Python 2.6 - 3.3.

%prep
%setup -q -n singledispatch-%{version}
cp %{SOURCE1} %{SOURCE2} .
sed -i "s/'six'//" setup.py
# remove unwanted shebang
sed -i '1 { /^#!/ d }' singledispatch_helpers.py singledispatch.py

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python test_singledispatch.py

%files
# https://bitbucket.org/ambv/singledispatch/issues/9/mit-license
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
