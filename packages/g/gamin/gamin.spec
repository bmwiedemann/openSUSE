#
# spec file for package gamin
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


%define sonum   0
%define vernum  1
%define packnum %{vernum}-%{sonum}
%define famnum  0
Name:           gamin
Version:        0.1.10
Release:        0
Summary:        Library providing the FAM File Alteration Monitor API
License:        LGPL-2.1-only
Group:          System/Daemons
URL:            http://www.gnome.org/~veillard/%{name}/
Source:         http://www.gnome.org/~veillard/%{name}/sources/%{name}-%{version}.tar.gz
Source2:        %name-rpmlintrc
Source99:       baselibs.conf
Patch0:         gamin-return.patch
Patch1:         gamin-fam_abi_compatibility_FamErrlist.patch
Patch2:         gamin-fix_python_main.patch
Patch3:         gamin-obsol-glib.diff
# PATCH-FIX-UPSTREAM gamin-0.1.11-double-lock.patch (bgo#669292)
Patch4:         gamin-0.1.11-double-lock.patch
# PATCH-FIX-UPSTREAM 0001-Poll-files-on-nfs4.patch (bgo#693006)
Patch5:         0001-Poll-files-on-nfs4.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  pkgconfig(glib-2.0)

%description
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM, but not dependent on a system wide
daemon.

%package -n python-%{name}
Summary:        Python bindings for the %{name} library
Group:          Development/Libraries/Python
Requires:       lib%{name}-%{packnum} = %{version}
Provides:       %{name}-python = %{version}-%{release}
Obsoletes:      %{name}-python < %{version}-%{release}

%description -n python-%{name}
The python-%{name} package contains a module that allow monitoring of
files and directories from the Python language based on the support
of the %{name} package.

%package doc
Summary:        Documentation for %{name}
Group:          Development/Libraries/C and C++

%description doc
Documentation and help files for %{name}.

%package server
Summary:        Server for the Library providing the FAM File Alteration Monitor API
Group:          System/Daemons
Provides:       fam-server = %{version}-%{release}
Obsoletes:      fam-server < %{version}-%{release}

%description server
This package contains the daemon for %{name}.
It is split off into its own subpackage to void file conflicts when both
%{name} and %{name}-32bit are installed on a multiarch platform.

%prep
%setup -q
%patch0 -p0
%patch1
%patch2
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%configure --disable-static --enable-tests
make %{?_smp_mflags}

%install
%make_install
rm "%{buildroot}%{_libdir}"/*.la
mkdir -p .rpmdoc/python
mv doc/python.html .rpmdoc/python/doc.html
%fdupes %{buildroot}

# drop files which are build via libgamin spec file
rm %buildroot%{_includedir}/fam.h              \
   %buildroot%{_libdir}/lib%{name}_shared.a    \
   %buildroot%{_libdir}/pkgconfig/gamin.pc     \
   %buildroot%{_libdir}/libgamin-%{vernum}.so* \
   %buildroot%{_libdir}/libfam.so*

%check
# tests are currently broken :/
make tests || echo "**** WARNING TESTSUITE FAILS ****"

%files -n python-%{name}
%defattr(-,root,root)
%doc .rpmdoc/python/*
%{python_sitearch}/gamin.py*
%{python_sitearch}/_gamin*

%files server
%defattr(-, root, root)
%{_libexecdir}/gam_server

%changelog
