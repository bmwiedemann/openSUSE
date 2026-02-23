#
# spec file for package ublksrv
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover 0

Name:           ublksrv
Version:        1.6
Release:        0
Summary:        Userspace daemon part (ublksrv) of the ublk framework
License:        MIT
URL:            https://github.com/ublk-org/ublksrv
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(liburing) >= 2.2

%description
This is the userspace daemon part(ublksrv) of the ublk framework.

%package -n libublksrv%{sover}
Summary:        A library to integrate ublk into existing projects
Group:          System/Libraries

%description -n libublksrv%{sover}
A helper library to integrate ublk into existing projects.

%package devel
Summary:        Development files for libublksrv
Group:          Development/Libraries/C and C++
Requires:       libublksrv%{sover} = %{version}-%{release}

%description devel
This package contains headers and libraries required to build applications that
make use of the ublk framework.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.a" -delete -print

%post   -n libublksrv%{sover} -p /sbin/ldconfig
%postun -n libublksrv%{sover} -p /sbin/ldconfig

%files
%license COPYING* LICENSE
%doc README.rst
%{_sbindir}/ublk
%{_sbindir}/ublk.loop
%{_sbindir}/ublk.nbd
%{_sbindir}/ublk.null
%{_sbindir}/ublk_chown.sh
%{_sbindir}/ublk_chown_docker.sh
%{_sbindir}/ublk_user_id
%{_mandir}/man1/ublk.1%{?ext_man}

%files -n libublksrv%{sover}
%{_libdir}/libublksrv.so.%{sover}
%{_libdir}/libublksrv.so.%{sover}.*

%files devel
%{_includedir}/ublk_cmd.h
%{_includedir}/ublksrv*.h
%{_libdir}/pkgconfig/ublksrv.pc
%{_libdir}/libublksrv.so

%changelog
