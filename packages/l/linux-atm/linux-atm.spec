#
# spec file for package linux-atm
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


Name:           linux-atm
Version:        2.5.2
Release:        0
%global sover   1
Summary:        Tools for ATM
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/Other

Url:            http://linux-atm.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM linux-atm-2.5.2_fdleak.patch
Patch0:         linux-atm-2.5.2_fdleak.patch
# PATCH-FIX-UPSTREAM linux-atm-2.5.2_implicit-fortify-decl.patch -- fix implicit declarations
Patch1:         linux-atm-2.5.2_implicit-fortify-decl.patch
# PATCH-FIX-UPSTREAM linux-atm-2.5.2-fix-header-conflict.patch -- avoid conflict with kernel headers
Patch2:         linux-atm-2.5.2-fix-header-conflict.patch
# PATCH-FIX-UPSTREAM linux-atm-2.5.2-remove-headers-crude-hack.patch -- Remove headers crude hack
Patch3:         linux-atm-2.5.2-remove-headers-crude-hack.patch
# PATCH-FIX-UPSTREAM fix-build-after-y2038-changes-in-glibc.patch -- fix build after y2038 changes in glibc
Patch4:         fix-build-after-y2038-changes-in-glibc.patch

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  glibc-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tools to support ATM (Asynchronous Transfer Mode) networking.


%package -n libatm%{sover}

Summary:        Libraries for ATM
Group:          System/Libraries

%description -n libatm%{sover}
Libraries for ATM (Asynchronous Transfer Mode) networking.


%package devel
Summary:        Development for ATM
Group:          Development/Libraries/C and C++
Requires:       libatm%{sover} = %{version}

%description devel
Libraries and header files for ATM (Asynchronous Transfer Mode)
networking.


%prep
%setup -q
%autopatch -p1

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR=%{buildroot}
%{__rm} -rf %{buildroot}%{_libdir}/*.la

%post -n libatm%{sover} -p /sbin/ldconfig

%postun -n libatm%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/atmsigd.conf
%config(noreplace) %{_sysconfdir}/hosts.atm
%{_bindir}/*
%{_sbindir}/*
/lib/firmware/*
%doc README AUTHORS ChangeLog NEWS THANKS BUGS
%license COPYING COPYING.GPL COPYING.LGPL
%doc %{_mandir}/man*/*.gz

%files -n libatm%{sover}
%defattr(-,root,root)
%{_libdir}/libatm.so.%{sover}*

%files devel
%defattr(-,root,root)
%{_includedir}/atm*.h
%{_libdir}/libatm.so

%changelog
