#
# spec file for package python-tsk
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


%define timestamp 	20170802
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-tsk
Version:        0~%{timestamp}
Release:        0
Summary:        Python bindings for tsk - The SleuthKit
# the included talloc library is LGPL 3
License:        Apache-2.0 AND LGPL-3.0+
Group:          Development/Languages/Python
Url:            https://github.com/py4n6/pytsk/
Source0:        https://github.com/py4n6/pytsk/releases/download/%{timestamp}/pytsk3-%{timestamp}.tar.gz
Patch1:         pytsk_20170128_remove_talloc_build.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtalloc-devel
BuildRequires:  python-rpm-macros
BuildRequires:  sleuthkit-devel >= 4.4.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%python_subpackages

%description
The Sleuthkit is a forensic filesystem analysis framework (http://www.sleuthkit.org/). This project is a python 2 binding for the sleuthkit. 

%prep
%setup -q -n pytsk3-%{timestamp}
# remove unused libraries with incompatible license, use libtalloc from main repositories
# rm -rf pytsk talloc
# rm -rf pytsk talloc.new
# %patch1 -p1

%build
CFLAGS="%{optflags}"
%python_build

%install
%python_install
%fdupes %{buildroot}

%files %{python_files}
%defattr(-,root,root)
%doc LICENSE README
%{python_sitearch}/*

%changelog
