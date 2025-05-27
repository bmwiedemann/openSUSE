#
# spec file for package python-gps3
#
# Copyright (c) 2025 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define pkg_version 0.33.0
Name:           python-gps3
Version:        0.33.3+git.20171101
Release:        0
Summary:        Python interface for gpsd
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wadda/gps3
Source:         gps3-%{version}.tar.xz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python interface for gpsd.

%prep
%setup -q -n gps3-%{version}
# don't use env
find . -name "*.py" -exec sed -i 's|#!%{_bindir}/env python3.5|#!%{_bindir}/python3|g' {} \;
find . -name "*.py" -exec sed -i 's|#!%{_bindir}/env python3|#!%{_bindir}/python3|g' {} \;
# drop shebang
find gps3/ -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
find examples/ -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;

%build
%pyproject_wheel

%install
%pyproject_install
# remove examples
rm -rf %{buildroot}%{_datadir}/gps3
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc DESCRIPTION.rst README.md
%doc examples/
%{python_sitelib}/gps3
%{python_sitelib}/gps3-%{pkg_version}*-info

%changelog
