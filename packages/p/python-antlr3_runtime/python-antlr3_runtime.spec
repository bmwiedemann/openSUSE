#
# spec file for package python-antlr3_runtime
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-antlr3_runtime
Version:        3.1.3
Release:        0
Summary:        ANTLR3 parser
License:        BSD-3-Clause
Group:          Development/Libraries/Python
Url:            http://antlr3.org/download/Python
Source0:        antlr_python_runtime-%{version}.tar.gz
BuildRequires:  python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
Python implementation of ANTLR, ANother Tool for Language Recognition.
ANTLR is a language tool that provides a framework for constructing
recognizers, interpreters, compilers, and translators from grammatical
descriptions.

%prep
%setup -q -n antlr_python_runtime-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README
%dir %{python_sitelib}/antlr3
%dir %{python_sitelib}/antlr_python_runtime-%{version}-py%{py_ver}.egg-info
%{python_sitelib}/antlr3/*
%{python_sitelib}/antlr_python_runtime-%{version}-py%{py_ver}.egg-info/*

%changelog
