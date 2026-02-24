#
# spec file for package intel-lpmd
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


Name:           intel-lpmd
Version:        0.1.0
Release:        0
Summary:        Intel Low Power Mode Daemon
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            https://github.com/intel/intel-lpmd
Source:         https://github.com/intel/intel-lpmd/archive/refs/tags/v%version.tar.gz
Patch1:         install.patch
BuildRequires:  automake
BuildRequires:  gtk-doc >= 1.11
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.22
BuildRequires:  pkgconfig(glib-2.0) >= 2.10.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4
BuildRequires:  pkgconfig(upower-glib)
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

%pre
%service_add_pre intel_lpmd.service

%post
%service_add_post intel_lpmd.service

%preun
%service_del_preun intel_lpmd.service

%postun
%service_del_postun intel_lpmd.service

%files
%_bindir/intel*
%_sbindir/intel*
%_mandir/man*/*.[0-9]*
%_unitdir/*.service
%_datadir/dbus-1/
%_datadir/intel_lpmd/
%doc data/intel_lpmd_config.xml data/intel_lpmd_config_F6_M170.xml README.md
%license COPYING

%changelog
