#
# spec file for package python-xdg
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
Name:           python-xdg
Version:        4.0.1
Release:        0
Summary:        Variables defined by the XDG Base Directory Specification
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/srstevenson/xdg
Source:         https://files.pythonhosted.org/packages/source/x/xdg/xdg-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/srstevenson/xdg/master/test/test_xdg.py
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
xdg is a Python module which provides the variables defined by the
XDG Base Directory Specification, to save you from duplicating the
same snippet of logic in every Python utility you write that deals
with user cache, configuration, or data files. It has no external
dependencies.

%prep
%setup -q -n xdg-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%{python_sitelib}/*

%changelog
