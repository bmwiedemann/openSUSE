#
# spec file for package modemu2k
#
# Copyright (c) 2026 SUSE LLC
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

%define soname 0
%define libname lib%{name}%{soname}
%define devname lib%{name}%{soname}-devel

Name:           modemu2k
Version:        0.2.4
Release:        0
Summary:        Hayes-style AT-command modem emulator bridging serial-style I/O to TCP/Telnet
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://theimpossibleastronaut.github.io/modemu2k/
Source:         https://github.com/theimpossibleastronaut/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  groff
BuildRequires:  meson >= 0.56.0
Suggests:       minicom
Suggests:       picocom

%description
modemu2k is a Hayes-style AT-command modem emulator bridging a
serial-style interface to TCP/Telnet ("dials" out and answers incoming
connections). It ships as a C library (libmodemu2k) exposing the modem
state machine, plus a small CLI built on top that allocates a PTY and
either reads stdin/stdout directly, forks a comm program (minicom,
picocom) on the slave, or accepts an incoming TCP connection as the
TTY. IPv4 and IPv6.

modemu2k is based on modemu, originally developed by Toru Egashira.

This package contains the CLI binary and the m2k-minicom / m2k-picocom
helper scripts.

%package -n %{libname}
Summary:        Shared library for the modemu2k modem emulator
Group:          System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n %{devname}
This package contains the development files (headers, pkg-config file,
and unversioned shared library symlink) for %{name}.

%prep
%autosetup -p1

%build
%meson \
	--buildtype=release \
	-Dstrip=true \
	-Ddocdir=%{_docdir}/%{name} \
	-Dgen-docs=true \
	-Dhelper-scripts=true
%meson_build

%install
%meson_install

rm %{buildroot}%{_docdir}/%{name}/COPYING
%fdupes %{buildroot}%{_docdir}/%{name}/html

%check
%meson_test

%ldconfig_scriptlets -n %{libname}

%files
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/modemu2k
%{_bindir}/m2k-minicom
%{_bindir}/m2k-picocom
%{_mandir}/man1/modemu2k.1%{?ext_man}

%files -n %{libname}
%license COPYING
%{_libdir}/lib*.so.[0-9]*

%files -n %{devname}
%{_libdir}/libmodemu2k.so
%{_libdir}/pkgconfig/modemu2k.pc
%dir %{_includedir}/modemu2k
%{_includedir}/modemu2k/modemu2k.h
%{_includedir}/modemu2k/modemu2k_version.h

%changelog
