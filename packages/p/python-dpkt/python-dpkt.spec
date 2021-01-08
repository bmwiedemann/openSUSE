#
# spec file for package python-dpkt
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
Name:           python-dpkt
Version:        1.9.4
Release:        0
Summary:        Packet creation and parsing module for Python
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/kbandla/dpkt
Source:         https://github.com/kbandla/dpkt/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_s390x_tests.patch gh#kbandla/dpkt#505 mcepl@suse.com
# Skip failing tests on s390x arch
Patch0:         fix_s390x_tests.patch
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A packet creation / parsing module for Python, with definitions for
the basic TCP/IP protocols.

%prep
%setup -q -n dpkt-%{version}
%autopatch -p1

# do not add extra pytest argumetns
sed -i -e '/addopts=/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#kbandla/dpkt#505
%pytest -s dpkt

%files %{python_files}
%license LICENSE
%doc examples AUTHORS CHANGES README.rst
%{python_sitelib}/*

%changelog
