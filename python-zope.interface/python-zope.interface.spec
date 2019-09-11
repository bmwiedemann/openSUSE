#
# spec file for package python-zope.interface
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%global modname zope.interface
%define oldpython python
Name:           python-zope.interface
Version:        4.6.0
Release:        0
Summary:        Interfaces for Python
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            http://pypi.python.org/pypi/zope.interface
Source:         https://files.pythonhosted.org/packages/source/z/zope.interface/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.event}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%ifpython2
Provides:       %{oldpython}-zopeinterface = %{version}
Obsoletes:      %{oldpython}-zopeinterface < %{version}
Provides:       %{oldpython}-zope-interface = %{version}
Obsoletes:      %{oldpython}-zope-interface < %{version}
%endif
%python_subpackages

%description
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

This package provides an implementation of object interfaces for Python.
Interfaces are a mechanism for labeling objects as conforming to a given
API or contract. So, this package can be considered as implementation of
the Design By Contract methodology support in Python.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand rm %{buildroot}%{$python_sitearch}/zope/interface/_zope_interface_coptimizations.c
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt COPYRIGHT.txt
%doc CHANGES.rst README.rst
%{python_sitearch}/*

%changelog
