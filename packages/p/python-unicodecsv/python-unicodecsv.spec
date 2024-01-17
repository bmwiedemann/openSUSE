#
# spec file for package python-unicodecsv
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-unicodecsv
Version:        0.14.1
Release:        0
Summary:        Drop-in replacment for python's csv module with unicode support
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/jdunck/python-unicodecsv
Source:         https://pypi.io/packages/source/u/unicodecsv/unicodecsv-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%python_subpackages

%description
Python 2's csv module doesn't easily deal with unicode strings,
leading to the dreaded "'ascii' codec can't encode characters
in position ..." exception.

The unicodecsv is a drop-in replacement for Python 2's csv module
which supports unicode strings without a hassle.

%prep
%setup -q -n unicodecsv-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*

%changelog
