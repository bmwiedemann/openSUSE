#
# spec file for package python-distlib
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.3.1
Release:        0
Summary:        Distribution utilities
License:        Python-2.0
URL:            https://bitbucket.org/pypa/distlib
Source:         https://files.pythonhosted.org/packages/source/d/distlib/distlib-%{version}.zip
Patch0:         remove-backports.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%python_subpackages

%description
Python distribution utilities.

%prep
%setup -q -n distlib-%{version}
%autopatch -p1

rm -r tests/unittest2

# tarfile backport is broken
rm distlib/_backport/tarfile.py

# sysconfig backport is unnecessary and untested
rm distlib/_backport/sysconfig.*

# These test modules require internet access and are unnecessary
rm tests/test_locators.py tests/test_sysconfig.py

# Unused
rm distlib/_backport/misc.*

# Unneeded on Linux
rm distlib/*.exe

# However, the tests for shutil fail when not using using provided backport

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# These two tests need internet access
%pytest -k 'not (test_search or test_package_data)'

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
