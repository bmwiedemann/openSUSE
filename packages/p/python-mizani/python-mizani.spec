#
# spec file for package python-mizani
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
%define         skip_python2 1
%define         skip_python36 1
Name:           python-mizani
Version:        0.7.2
Release:        0
Summary:        Scales for Python
License:        BSD-3-Clause
URL:            https://github.com/has2k1/mizani
Source:         https://files.pythonhosted.org/packages/source/m/mizani/mizani-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 3.1.1
Requires:       python-numpy
Requires:       python-palettable
Requires:       python-pandas >= 1.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib >= 3.1.1}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module palettable}
BuildRequires:  %{python_module pandas >= 1.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
Mizani is a scales package for graphics.

%prep
%setup -q -n mizani-%{version}
# correct np.timedelta64 usage
sed -i 's/unit=//' mizani/tests/test_*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
