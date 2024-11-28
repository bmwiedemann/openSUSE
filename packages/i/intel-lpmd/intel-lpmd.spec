#
# spec file for package intel-lpmd
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


Name:           intel-lpmd
Version:        0.0.8
Release:        0
Summary:        Intel Low Power Mode Daemon
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            https://github.com/intel/intel-lpmd
Source:         https://github.com/intel/intel-lpmd/archive/refs/tags/v%version.tar.gz
Patch0:         fix_cpuid_double_include.patch
BuildRequires:  automake
BuildRequires:  pkg-config
BuildRequires:  gtk-doc >= 1.11
BuildRequires:  pkgconfig(glib-2.0) >= 2.10.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.22
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4
ExclusiveArch:  %ix86 x86_64

%description
A daemon used to optimize active idle power. It selects a set of most
power efficient CPU cores based on configuration file or CPU
topology. Based on system utilization and other hints, it puts the
system into Low Power Mode by activating the power efficient CPUs and
disabling the rest, and restores the system from Low Power Mode by
activating all CPUs.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-werror
%make_build

%install
%make_install
find | grep xml
rm -Rf "%buildroot/etc"

%files
%_bindir/intel*
%_sbindir/intel*
%_mandir/man*/*.[0-9]*
%doc data/intel_lpmd_config.xml data/intel_lpmd_config_F6_M170.xml README.md
%license COPYING

%changelog
