#
# spec file for package python-diskcache
#
# Copyright (c) 2023 SUSE LLC
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
%global skip_python2 1
Name:           python-diskcache
Version:        5.6.1
Release:        0
Summary:        Disk and file backed cache
License:        Apache-2.0
URL:            https://grantjenks.com/docs/diskcache/
Source:         https://github.com/grantjenks/python-diskcache/archive/v%{version}.tar.gz#/diskcache-%{version}.tar.gz
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module Django if (%python-base without python36-base)}
BuildRequires:  %{python_module pytest-django if (%python-base without python36-base)}
Requires:       python
BuildArch:      noarch
%python_subpackages

%description
DiskCache: Disk Backed Cache

DiskCache is a disk and file backed cache library, written
in pure Python, and compatible with Django.

%prep
%setup -q
sed -i '/--cov/d' tox.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No python36-Django 4 on TW
python36_flags=("--ignore" "tests/test_doctest.py" "-k" "not README.rst")
# Broken since Django 3.2 -- https://github.com/grantjenks/python-diskcache/issues/210
donttest_djangocache="--ignore tests/test_djangocache.py"
%pytest "${$python_flags[@]}" ${donttest_djangocache}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/diskcache
%{python_sitelib}/diskcache-%{version}*-info

%changelog
