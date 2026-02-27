#
# spec file for package lttng-tools
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


%define _version 2.14.0
%define soname_ctl liblttng-ctl
%define sover_ctl 6
Name:           lttng-tools
Version:        2.14.0
Release:        0
Summary:        Linux Trace Toolkit Next Generation userspace tools
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Tools/Other
URL:            https://lttng.org/
Source:         https://lttng.org/files/lttng-tools/%{name}-%{version}.tar.bz2
Source1:        https://lttng.org/files/lttng-tools/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
# PATCH-FIX-OPENSUSE lttng-tools-fix-pkgconfig.patch sor.alexei@meowr.ru -- Add missing dependencies to lttng-ctl.pc.
Patch0:         lttng-tools-fix-pkgconfig.patch
Patch1:         lttng-tools-soname-ctl6.patch
Patch2:         lttng-tools-position-independent.patch
Patch3:         0001-Restore-setup-of-consumer-related-setup-by-build-sys.patch
BuildRequires:  automake
BuildRequires:  babeltrace2-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc13-c++
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lttng-ust) >= %{_version}
BuildRequires:  pkgconfig(uuid)
Recommends:     lttng-modules-kmp
ExclusiveArch:  %ix86 x86_64 armv7l aarch64 loongarch64 riscv64 ppc64 ppc64le

%description
This package provides the userspace tools for controlling the LTTng
subsystem from userspace.

%package -n %{soname_ctl}%{sover_ctl}
Summary:        Linux Trace Toolkit Next Generation control and utility library
Group:          System/Libraries

%description -n %{soname_ctl}%{sover_ctl}
This package provides a userspace library for controlling the LTTng
subsystem. It is primarily intended for use by the lttng-tools
package.

%package devel
Summary:        Linux Trace Toolkit Next Generation userspace tools
Group:          Development/Languages/C and C++
Requires:       %{soname_ctl}%{sover_ctl} >= %{_version}-%{release}

%description devel
This package provides the userspace tools for controlling the LTTng
subsystem from userspace.

%prep
%autosetup -p1
autoreconf

# lttng-tools 2.14 fails due to LTO mismatch with g++-15 and g++-13 objects, either set g++-15 as compiler or disable LTO. Let's do the latter here.
%define _lto_cflags %{nil}

%build
export CXX=g++-13
export CXXFLAGS="-fPIE ${CXXFLAGS}"
export LDFLAGS="-fPIE ${LDFLAGS}"

# for 32bit support, see https://lttng.org/docs/v2.13/#doc-instrumenting-32-bit-app-on-64-bit-system
%configure \
  --docdir=%{_docdir}/%{name} \
  --disable-static \
  --with-consumerd32-libdir=/usr/lib \
  --with-consumerd32-bin=/usr/lib/lttng/libexec/lttng-consumerd
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname_ctl}%{sover_ctl} -p /sbin/ldconfig

%postun -n %{soname_ctl}%{sover_ctl} -p /sbin/ldconfig

%files
%doc %{_docdir}/%{name}/
%license LICENSE
%{_bindir}/lttng
%{_bindir}/lttng-crash
%{_bindir}/lttng-relayd
%{_libdir}/lttng/libexec/lttng-consumerd
%{_bindir}/lttng-sessiond
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man3/*.3%{?ext_man}
%{_mandir}/man7/*.7%{?ext_man}
%{_mandir}/man8/*.8%{?ext_man}
%dir %{_libdir}/lttng/
%dir %{_libdir}/lttng/libexec/
%dir %{_datadir}/xml/lttng/
%{_datadir}/xml/lttng/session.xsd

%files -n %{soname_ctl}%{sover_ctl}
%license LICENSE
%{_libdir}/%{soname_ctl}.so.%{sover_ctl}*

%files devel
%{_includedir}/lttng/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lttng-ctl.pc

%changelog
