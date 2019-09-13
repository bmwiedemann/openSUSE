#
# spec file for package sblim-sfcCommon (Version 1.0.1)
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild

Name:           sblim-sfcCommon
BuildRequires:  gcc-c++ sblim-cmpi-devel
BuildRequires:  pkgconfig
Url:            http://sourceforge.net/projects/sblim
License:        EPL-1.0
Group:          System/Libraries

Version:        1.0.1
Release:        1
Summary:        Library of utility functions shared between sfcb and sfcc
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch1:         type-punned-pointer.patch

%description
This package provides a common library for functions 
shared between sfcb and sfcc.


%define libname libsfcUtil0

%package -n %libname
Summary:        Library of utility functions shared between sfcb and sfcc
Group:          System/Libraries

%description -n %libname
This package provides a common library for functions 
shared between sfcb and sfcc.

%package devel
License:        EPL-1.0
Summary:        Library of utility functions shared between sfcb and sfcc
Group:          Development/Libraries/C and C++
Requires:       sblim-cmpi-devel
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
Requires:  pkgconfig
%else
%if 0%{?suse_version} < 920
Requires:  pkgconfig
%else
Requires:  pkg-config
%endif
%endif
Requires:       %libname = %{version}-%{release}

%description devel
This package provides development files to compile and link against
libsblim-sfccommon.

%prep
%setup -q
%patch1 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS"
%configure --enable-static=no
make

%install
%makeinstall
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-, root, root, -)
%{_libdir}/lib*.so.*
%doc COPYING
%doc AUTHORS
%doc NEWS

%files devel
%defattr(-, root, root, -)
%{_libdir}/lib*.so
%dir %{_includedir}/sfcCommon
%{_includedir}/sfcCommon/*.h
#%%{_libdir}/pkgconfig/libsblim-sfccommon.pc
%doc README

%changelog
