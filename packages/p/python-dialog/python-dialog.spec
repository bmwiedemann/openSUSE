#
# spec file for package python-dialog
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


Name:           python-dialog
BuildRequires:  python-devel
%define tarname python2-pythondialog
Summary:        A Python interface to the Unix dialog utility
License:        LGPL-2.1+
Group:          Development/Libraries/Python
Version:        3.3.0
Release:        0
Source0:        https://pypi.python.org/packages/source/p/%{tarname}/%{tarname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://pythondialog.sourceforge.net/
Requires:       dialog
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
A Python interface to the Unix dialog utility, designed to provide an
easy, pythonic and as complete as possible way to use the dialog
features from Python code.

%prep
%setup -n %{tarname}-%{version}

%build
rm setup.cfg
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS PKG-INFO TODO examples/demo.py COPYING README.rst ChangeLog
%{python_sitelib}/*

%changelog
