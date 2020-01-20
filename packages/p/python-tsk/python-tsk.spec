#
# spec file for package python-tsk
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


%define timestamp 	20200117
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-tsk
Version:        0~%{timestamp}
Release:        0
Summary:        Python bindings for tsk - The SleuthKit
# the included talloc library is LGPL 3
License:        Apache-2.0 AND LGPL-3.0-or-later
URL:            https://github.com/py4n6/pytsk/
Source0:        https://files.pythonhosted.org/packages/source/p/pytsk3/pytsk3-%{timestamp}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libtalloc-devel
BuildRequires:  postgresql-devel
BuildRequires:  python-rpm-macros
BuildRequires:  sleuthkit-devel >= 4.6.7
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libvhdi)
BuildRequires:  pkgconfig(libvmdk)

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
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# pytest is NOT suppoerted (see gh#py4n6/pytsk#48)
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python ./run_tests.py
}

%files %{python_files}
%defattr(-,root,root)
%doc README
%license LICENSE 
%{python_sitearch}/*

%changelog
