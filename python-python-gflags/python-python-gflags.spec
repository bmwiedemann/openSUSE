#
# spec file for package python-python-gflags
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-python-gflags
Version:        3.1.2
Release:        0
Url:            http://code.google.com/p/python-gflags
Summary:        Google Commandline Flags Module
License:        BSD-3-Clause
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/python-gflags/python-gflags-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%ifpython2
Provides:       %{oldpython}-gflags = %{version}
Obsoletes:      %{oldpython}-gflags < %{version}
%endif
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(preun):  update-alternatives
%python_subpackages

%description
This project is the python equivalent of google-gflags, a Google commandline
flag implementation for C++. It is intended to be used in situations where a
project wants to mimic the command-line flag handling of a C++ app that uses
google-gflags, or for a Python app that, via swig or some other means, is
linked with a C++ app that uses google-gflags.

The gflags package contains a library that implements commandline flags
processing. As such it's a replacement for getopt(). It has increased
flexibility, including built-in support for Python types, and the ability to
define flags in the source file in which they're used. (This last is its major
difference from OptParse.)

%prep
%setup -q -n python-gflags-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mv %{buildroot}%{_bindir}/gflags2man.py %{buildroot}%{_bindir}/gflags2man
%python_clone -a %{buildroot}%{_bindir}/gflags2man

%post
%python_install_alternative gflags2man

%preun
%python_uninstall_alternative gflags2man

%files %{python_files}
%defattr(-,root,root,-)
%license COPYING
%doc AUTHORS ChangeLog README.md
%python_alternative %{_bindir}/gflags2man
%{python_sitelib}/*

%changelog
