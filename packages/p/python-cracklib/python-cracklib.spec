#
# spec file for package python-cracklib
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cracklib
Version:        2.9.3
Release:        0
Url:            http://cracklib.sourceforge.net/
Summary:        A CPython extension module wrapping the libcrack library
License:        GPL-2.0+
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/c/cracklib/cracklib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:	python-rpm-macros
BuildRequires:  cracklib-devel
%python_subpackages

%description
This CPython extension provides Python bindings for cracklib. It
contains a pythonic interface to cracklib's functions and some Python
convenience functions.

%prep
%setup -q -n cracklib-%{version}

%build
export CFLAGS="%{optflags}"
%python_build 

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%{python_sitearch}/*

%changelog
