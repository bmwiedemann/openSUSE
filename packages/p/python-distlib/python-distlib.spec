#
# spec file for package python-distlib
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-distlib
Version:        0.3.8
Release:        0
Summary:        Distribution utilities
License:        Python-2.0
URL:            https://github.com/pypa/distlib
Source:         https://files.pythonhosted.org/packages/source/d/distlib/distlib-%{version}.tar.gz
Patch1:         https://github.com/pypa/distlib/commit/1c08845b05d022692252ed45cb07e9cb9647caac.patch#/py313-interpreter-repr.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python distribution utilities.

%prep
%autosetup -p1 -n distlib-%{version}

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
