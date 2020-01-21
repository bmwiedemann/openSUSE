#
# spec file for package python-pythondialog
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pythondialog
Version:        3.5.1
Release:        0
Summary:        A Python interface to the UNIX dialog utility and mostly-compatible programs
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            http://pythondialog.sourceforge.net/
Source:         https://files.pythonhosted.org/packages/source/p/pythondialog/pythondialog-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       dialog
BuildArch:      noarch
%python_subpackages

%description
Python wrapper for the UNIX "dialog" utility
Easy writing of graphical interfaces for terminal-based applications

%prep
%setup -q -n pythondialog-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*
%license COPYING
%doc README.rst ChangeLog AUTHORS

%changelog
