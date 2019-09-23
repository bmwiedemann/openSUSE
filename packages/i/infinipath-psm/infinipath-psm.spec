#
# spec file for package infinipath-psm
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


%define git_ver .26.604758e

Name:           infinipath-psm
Version:        3.3
Release:        0
Summary:        QLogic PSM Libraries
License:        BSD-2-Clause OR GPL-2.0-only
Group:          Productivity/Networking/System
Url:            http://www.qlogic.com/
Source0:        %{name}-%{version}%{git_ver}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM infinipath-psm-cflags.patch pth@suse.de
Patch0:         infinipath-psm-cflags.patch
# PATCH-FIX-UPSTREAM infinipath-psm-no_werror.patch pth@suse.de
Patch1:         infinipath-psm-no_werror.patch
# PATCH-FIX-UPSTREAM infinipath-psm-executable_headers.patch pth@suse.de
Patch3:         infinipath-psm-executable_headers.patch
# PATCH-FIX-UPSTREAM bmwiedemann https://github.com/intel/psm/pull/16 boo#1047218
Patch4:         reproducible.patch
# PATCH-FIX-UPSTREAM Include <sys/sysmacros.h> for minor
Patch5:         sysmacros.patch
BuildRequires:  libuuid-devel
Conflicts:      infinipath-libs
ExclusiveArch:  %ix86 x86_64

%define so_major 4
%define psm_so_major 1
%define lname libinfinipath%{so_major}
%define lnamepsm libpsm_infinipath%{psm_so_major}

%description
The PSM Messaging API, or PSM API, is QLogic's low-level
user-level communications interface for the Truescale
family of products. PSM users are enabled with mechanisms
necessary to implement higher level communications
interfaces in parallel environments.

%package        devel
Summary:        Development files for QLogic PSM
Group:          Development/Libraries/C and C++
Requires:       %{lnamepsm} = %{version}
Requires:       %{lname} = %{version}
Requires:       libuuid-devel
Conflicts:      infinipath-devel

%description devel
Development files for the libpsm_infinipath library

%package     -n %{lnamepsm}
Summary:        Development files for QLogic PSM
Group:          System/Libraries
Obsoletes:      infinipath-psm < %{version}
Provides:       infinipath-psm = %{version}
Conflicts:      libpsm2-compat
# PSM1 library does not actually obsolete psm2-compat, BUT
# both RPM provide the same library leaving a choice for
# zypper/OBS. psm2-compat is to be used in extremely rare
# occasions by a knowing user wanting to try out their PSM1 application
# against PSM2 HW. Marking PSM1 as obsoleting psm2-compat
# fixes the issue and match RHEL behaviour. See bsc#1080773
Obsoletes:      libpsm2-compat

%description -n %{lnamepsm}
The PSM Messaging API, or PSM API, is QLogic's low-level
user-level communications interface for the Truescale
family of products. PSM users are enabled with mechanisms
necessary to implement higher level communications
interfaces in parallel environments.

%package     -n %{lname}
Summary:        Development files for QLogic PSM
Group:          System/Libraries

%description -n %{lname}
The PSM Messaging API, or PSM API, is QLogic's low-level
user-level communications interface for the Truescale
family of products. PSM users are enabled with mechanisms
necessary to implement higher level communications
interfaces in parallel environments.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}
%patch0
%patch1
%patch3
%patch4 -p1
%patch5 -p1

%build
%define _lto_cflags %{nil}
export RPM_OPT_FLAGS="%{optflags} -Wno-unused-but-set-variable"
make libdir=%{_libdir} %{?_smp_mflags} 

%install
make libdir=%{_libdir} DESTDIR=%{buildroot} install

%post -n %{lname} -p /sbin/ldconfig
%post -n %{lnamepsm} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%postun -n %{lnamepsm} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root,-)
%{_libdir}/libinfinipath.so.*

%files -n %{lnamepsm}
%defattr(-,root,root,-)
%{_libdir}/libpsm_infinipath.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libpsm_infinipath.so
%{_libdir}/libinfinipath.so
%{_includedir}/psm.h
%{_includedir}/psm_mq.h

%changelog
