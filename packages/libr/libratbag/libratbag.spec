#
# spec file for package libratbag
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Matthias Bach <marix@marix.org>.
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


Name:           libratbag
Version:        0.15
Release:        0
Summary:        Configuration library for gaming mice
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/libratbag/libratbag
Source:         %name-%version.tar.xz
Patch1:         shebang-env.diff
Patch2:         install-daemon-into-sbindir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  json-glib-devel
BuildRequires:  libunistring-devel
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  python3-evdev
BuildRequires:  python3-gobject
BuildRequires:  swig
BuildRequires:  systemd-rpm-macros
BuildRequires:  valgrind
BuildRequires:  pkgconfig(check) >= 0.9.10
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libsystemd) >= 227
BuildRequires:  pkgconfig(libudev) >= 196
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(systemd)

%description
libratbag is a configuration library for gaming mice. It provides a
generic way to access the various features exposed by these mice and
abstracts away hardware-specific and kernel-specific quirks.

%package -n liblur3
Summary:        Logitech Unifying Receiver configuration library
Group:          System/Libraries

%description -n liblur3
A library to configure and handle the /dev hidraw devices belonging
to the "Unifying" wireless receiver.

%package -n ratbagd
Summary:        Service granting access to the configuration options of gaming mice
Group:          Hardware/Other
Recommends:     libratbag-tools
Requires(pre):  group(games)

%description -n ratbagd
libratbag is a configuration library for gaming mice. It provides a
generic way to access the various features exposed by these mice and
abstracts away hardware-specific and kernel-specific quirks.

This subpackage contains the daemon managing access to the hardware.

%package devel
Summary:        Development files for the libratbag game mouse config library
Group:          Development/Libraries/C and C++
Requires:       liblur3 = %version

%description devel
libratbag is a configuration library for gaming mice. It provides a
generic way to access the various features exposed by these mice and
abstracts away hardware-specific and kernel-specific quirks.

This subpackage contains the files needed to build programs with
libratbag.

%package tools
Summary:        Utilities for configuring gaming mice
Group:          Hardware/Other
Requires:       python3-evdev
Requires:       ratbagd

%description tools
libratbag is a configuration library for gaming mice. It provides a
generic way to access the various features exposed by these mice and
abstracts away hardware-specific and kernel-specific quirks.

This subpackage contains the ratbag utilities allowing to inspect and configure
mice.

%prep
%setup -q
%patch -P 1 -P 2 -p1

%build
%meson -Ddocumentation=false -Ddbus-group=games \
	--includedir="%_includedir/%name"
%meson_build

%check
%meson_test

%install
%meson_install
mkdir -p "%buildroot/%_sbindir"
ln -s service "%buildroot/%_sbindir/rcratbagd"
chmod -x "%buildroot/%_datadir/%name/logitech-g402.device"  # Fix this file for some reaseon being executable
%fdupes %buildroot/%_prefix

%post   -n liblur3 -p /sbin/ldconfig
%postun -n liblur3 -p /sbin/ldconfig

%pre -n ratbagd
%service_add_pre ratbagd.service

%post -n ratbagd
%service_add_post ratbagd.service

%preun -n ratbagd
%service_del_preun ratbagd.service

%postun -n ratbagd
%service_del_postun ratbagd.service

%files -n liblur3
%defattr(-,root,root)
%_libdir/liblur.so.3*

%files devel
%defattr(-,root,root)
%_libdir/liblur.so
%_libdir/pkgconfig/*.pc
%_includedir/libratbag/

%files -n ratbagd
%defattr(-,root,root)
%_sbindir/ratbagd
%_sbindir/rcratbagd
%_unitdir/*.service
%_datadir/dbus-1/
%_datadir/%name/
%_mandir/man8/*

%files tools
%defattr(-,root,root)
%_bindir/lur-command
%_bindir/ratbagctl
%_mandir/man1/*

%changelog
