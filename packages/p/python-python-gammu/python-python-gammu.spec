#
# spec file for package python-python-gammu
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
%define skip_python2 1
Name:           python-python-gammu
Version:        3.2.4
Release:        0
Summary:        Python module to communicate with mobile phones
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://wammu.eu/python-gammu/
Source:         https://github.com/gammu/python-gammu/archive/refs/tags/%{version}.tar.gz#/python-gammu-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  gammu-devel >= 1.37.90
BuildRequires:  libdbi-drivers-dbd-sqlite3
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Obsoletes:      python-gammu < %{version}
Provides:       python-gammu = %{version}
%python_subpackages

%description
This provides gammu module, that can work with any phone Gammu
supports - many Nokias, Siemens, Alcatel, ...

%prep
%setup -q -n python-gammu-%{version}
find . -type f -name "*.py" -exec sed -i -e 's|\/usr\/bin\/env python|\/usr\/bin\/python|g' {} \;

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%check
# Need to limit tests due to brekage of libdbi
rm test/test_smsd.py
export LANG=en_US.UTF-8
mv gammu gammu.hide
%pyunittest_arch discover -v

%files %{python_files}
%license COPYING
%doc README.rst AUTHORS examples/
%{python_sitearch}/*

%changelog
