#
# spec file for package python-distlib
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
Name:           python-distlib
Version:        0.3.6
Release:        0
Summary:        Distribution utilities
License:        Python-2.0
URL:            https://github.com/pypa/distlib
Source:         https://files.pythonhosted.org/packages/source/d/distlib/distlib-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python distribution utilities.

%prep
%setup -q -n distlib-%{version}
%autopatch -p1

# This test module requires internet access and are unnecessary
sed -i '/from test_locators import LocatorTestCase/d' tests/distlib_tests.py

# Unneeded on Linux
rm distlib/*.exe

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# This file and two tests need internet access
%pytest --ignore tests/test_locators.py -k 'not (test_search or test_package_data)'

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/distlib
%{python_sitelib}/distlib-%{version}*-info

%changelog
