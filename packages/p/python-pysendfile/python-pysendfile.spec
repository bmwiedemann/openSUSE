#
# spec file for package python-pysendfile
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
%define mod_name pysendfile

Name:           python-pysendfile
Version:        2.0.1
Release:        0
Summary:        A Python interface to sendfile(2)
License:        MIT
Group:          Development/Languages/Python
Url:            http://code.google.com/p/pysendfile/
Source:         https://files.pythonhosted.org/packages/source/p/pysendfile/pysendfile-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%python_subpackages

%description
A python interface to sendfile(2) system call.

%prep
%setup -q -n %{mod_name}-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc LICENSE README.rst
%{python_sitearch}/*

%changelog
