#
# spec file for package python-gps3
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-gps3
Version:        0.33.3+git.20171101
Release:        0
License:        MIT
Summary:        Python interface for gpsd
Url:            https://github.com/wadda/gps3
Group:          Development/Languages/Python
Source:         gps3-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Python interface for gpsd.

%prep
%setup -q -n gps3-%{version}
# don't use env
find . -name "*.py" -exec sed -i 's|#!/usr/bin/env python3.5|#!/usr/bin/python3|g' {} \;
find . -name "*.py" -exec sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|g' {} \;
# drop shebang
find gps3/ -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
find examples/ -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;

%build
%python_build

%install
%python_install
# remove examples
rm -rf %{buildroot}%{_datadir}/gps3
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc DESCRIPTION.rst README.md
%doc examples/
%{python_sitelib}/*

%changelog
