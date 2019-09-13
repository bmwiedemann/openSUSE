#
# spec file for package python-pyte
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pyte
Version:        0.8.0
Release:        0
Summary:        VTXXX-compatible linux terminal emulator
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/selectel/pyte
Source:         https://files.pythonhosted.org/packages/source/p/pyte/pyte-%{version}.tar.gz
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wcwidth}
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

%build
%python_build

%install
%python_install

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README AUTHORS CHANGES docs/*rst
%{python_sitelib}/*

%changelog
