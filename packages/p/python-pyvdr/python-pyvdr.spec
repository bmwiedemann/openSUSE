#
# spec file for package python-pyvdr
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
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
Name:           python-pyvdr
Version:        0.3.1
Release:        0
Summary:        Python library for accessing a Linux VDR via SVDRP
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/baschno/pyvdr
Source:         https://github.com/baschno/pyvdr/archive/%{version}.tar.gz#/pyvdr-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python library for accessing a Linux VDR via SVDRP.

%prep
%setup -q -n pyvdr-%{version}
sed -i -e '/^#!\//, 1d' pyvdr/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pyvdr*

%changelog
