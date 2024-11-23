#
# spec file for package seatd
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


Name:           seatd
Version:        0.9.1
Release:        0
Summary:        Seat management daemon
License:        MIT
Group:          System/Base
URL:            https://git.sr.ht/~kennylevinsen/seatd
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.56.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(systemd)
Requires:       libseat1 = %{version}
BuildRequires:  pkgconfig(libsystemd) >= 237

%description
Seat management takes care of mediating access to shared devices (graphics, input), without requiring the applications needing access to be root.

%package -n libseat1
Summary:        Seat management library
Group:          Development/Libraries/C and C++

%description -n libseat1
A seat management library allowing applications to use whatever seat management is available.
Supports: seatd, (e)logind, embedded seatd for standalone operation

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libseat1 = %{version}

%description devel
Development files for %{name}.

%prep
%autosetup -p1

%build
%meson -Dlibseat-logind=systemd

%meson_build

%install
%meson_install

%post -n libseat1 -p /sbin/ldconfig
%postun -n libseat1 -p /sbin/ldconfig

%files
%doc README*
%{_bindir}/%{name}
%{_bindir}/seatd-launch
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/seatd-launch.1%{?ext_man}

%files -n libseat1
%license LICENSE
%{_libdir}/libseat.so.*

%files devel
%{_includedir}/libseat.h
%{_libdir}/pkgconfig/libseat.pc
%{_libdir}/libseat.so

%changelog
