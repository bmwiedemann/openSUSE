#
# spec file for package python-PyGetWindow
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
Name:           python-PyGetWindow
Version:        0.0.8
Release:        0
Summary:        Obtain GUI information on application's windows
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/asweigart/pygetwindow
Source:         https://files.pythonhosted.org/packages/source/P/PyGetWindow/PyGetWindow-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/asweigart/PyGetWindow/master/LICENSE.txt
BuildRequires:  %{python_module PyRect}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyRect
BuildArch:      noarch
%python_subpackages

%description
A simple, cross-platform module for obtaining GUI information on and
controlling application's windows.

%prep
%setup -q -n PyGetWindow-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
