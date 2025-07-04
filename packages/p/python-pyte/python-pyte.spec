#
# spec file for package python-pyte
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-pyte
Version:        0.8.2
Release:        0
Summary:        VTXXX-compatible linux terminal emulator
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/selectel/pyte
Source:         https://files.pythonhosted.org/packages/source/p/pyte/pyte-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wcwidth}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-wcwidth
BuildArch:      noarch
%python_subpackages

%description
An in-memory VTXXX-compatible terminal emulator supporting VT100 and
other DEC VTs between 1970 and 1995. pyte can be used to:

* screen scrape terminal apps, for example htop or aptitude.
* write terminal emulators; either with a graphical (xterm, rxvt)
  or a web interface, like AjaxTerm.

%prep
%setup -q -n pyte-%{version}
# all fail as missing data files
rm tests/test_input_output.py
sed -i '/pytest-runner/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README AUTHORS CHANGES docs/*rst
%dir %{python_sitelib}/pyte
%{python_sitelib}/pyte/*
%{python_sitelib}/pyte-%{version}*-info

%changelog
