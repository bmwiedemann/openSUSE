#
# spec file for package python-cangjie
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


%{?!python_module:%define python_module() python-%{1} python3-%{1}}
%global src_name cangjie
Name:           python-cangjie
Version:        1.2
Release:        0
Summary:        A python wrapper to libcangjie
License:        LGPL-3.0+
Url:            http://cangjians.github.io/projects/pycangjie
Source:         https://github.com/Cangjians/pycangjie/releases/download/v%{version}/%{src_name}-%{version}.tar.xz
Patch0:         fix_core.pxd_not_found.patch
BuildRequires:  %{python_module devel}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libcangjie-devel
BuildRequires:  libtool
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Cython
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%python_subpackages

%description
Python wrapper to libcangjie, the library implementing the Cangjie input method.

%prep
%setup -q -n %{src_name}-%{version}
%patch0 -p1

%build
./autogen.sh --prefix=%{_prefix}/
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes -s %{buildroot}/%{_libdir}/

%files %{python_files}
%defattr(-,root,root)
%doc AUTHORS COPYING README.md docs/*
%python3_only %{python_sitearch}/%{src_name}
%python3_only %pycache_only %{python_sitearch}/%{src_name}/__pycache__

%changelog
