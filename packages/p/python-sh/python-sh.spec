#
# spec file for package python-sh
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
Name:           python-sh
Version:        1.13.1
Release:        0
Summary:        Python subprocess interface
License:        MIT
URL:            https://github.com/amoffat/sh
Source:         https://files.pythonhosted.org/packages/source/s/sh/sh-%{version}.tar.gz
Patch0:         no-coverage.patch
Patch1:         fix-test_signal_group.diff
Patch2:         fix-test_general_signal.diff
Patch3:         fix-sleep-path-in-test.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
sh is a full-fledged subprocess replacement for Python 2.6 - 3.6, PyPy
and PyPy3 that allows you to call any program as if it were a
function:

    from sh import ifconfig
    print ifconfig("eth0")

sh is not a collection of system commands implemented in Python.

%prep
%setup -q -n sh-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install

%check
%python_exec test.py

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.md README.rst
%{python_sitelib}/sh.py*
%pycache_only %{python_sitelib}/__pycache__/sh.*py*
%{python_sitelib}/sh-%{version}-*.egg-info

%changelog
