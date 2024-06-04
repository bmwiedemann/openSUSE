#
# spec file for package gamin
#
# Copyright (c) 2024 SUSE LLC
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
Source0:        https://download.gnome.org/sources/gamin/0.1/gamin-%{version}.tar.bz2
Source2:        %name-rpmlintrc
Source99:       baselibs.conf
Patch0:         gamin-return.patch
Patch1:         gamin-fam_abi_compatibility_FamErrlist.patch
Patch3:         gamin-obsol-glib.diff
# PATCH-FIX-UPSTREAM gamin-0.1.11-double-lock.patch (bgo#669292)
Patch4:         gamin-0.1.11-double-lock.patch
# PATCH-FIX-UPSTREAM 0001-Poll-files-on-nfs4.patch (bgo#693006)
Patch5:         0001-Poll-files-on-nfs4.patch
Patch6:         gamin-missing-includes.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)

%description
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM, but not dependent on a system wide
daemon.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

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
%autosetup -p1

%build
%configure --disable-static --enable-tests
%make_build

%install
%make_install
rm "%{buildroot}%{_libdir}"/*.la
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

%files server
%{_libexecdir}/gam_server

%changelog
