#
# spec file for package libratbag
#
# Copyright (c) 2024 SUSE LLC
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
Version:        0.18
Release:        0
Summary:        Configuration library for gaming mice
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/libratbag/libratbag
Source0:        %{name}-%{version}.tar.xz
Source1:        README.SUSE
Patch1:         shebang-env.diff
Patch3:         harden_ratbagd.service.patch
Patch4:         use-python-3.6.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  json-glib-devel
BuildRequires:  libunistring-devel
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  python3-evdev
BuildRequires:  python3-gobject
BuildRequires:  swig
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
Requires(pre):  group(games)
Recommends:     libratbag-tools

%description -n ratbagd
libratbag is a configuration library for gaming mice. It provides a
generic way to access the various features exposed by these mice and
abstracts away hardware-specific and kernel-specific quirks.

This subpackage contains the daemon managing access to the hardware.
It enables any user that is a member of the group "games" to configure
supported mice via ratbagctl or Piper.

%package devel
Summary:        Development files for the libratbag game mouse config library
Group:          Development/Libraries/C and C++
Requires:       liblur3 = %{version}

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
%patch -P1 -p1
%patch -P3 -p1
%if 0%{?suse_version} < 1550
%patch -P4 -p1
%endif
cp %{SOURCE1} .

%build
%meson -Ddocumentation=false -Ddbus-group=games \
	--includedir="%{_includedir}/%{name}"
%meson_build

%check
%meson_test

%install
%meson_install
mkdir -p "%{buildroot}/%{_sbindir}"
ln -s service "%{buildroot}/%{_sbindir}/rcratbagd"
chmod -x "%{buildroot}/%{_datadir}/%{name}/logitech-g402.device"  # Fix this file for some reaseon being executable
%fdupes %{buildroot}/%{_prefix}

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
%{_libdir}/liblur.so.3*

%files devel
%{_libdir}/liblur.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libratbag/

%files -n ratbagd
%{_sbindir}/ratbagd
%{_sbindir}/rcratbagd
%{_unitdir}/*.service
%{_datadir}/dbus-1/
%{_datadir}/%{name}/
%{_mandir}/man8/*
%doc README.SUSE

%files tools
%{_bindir}/lur-command
%{_bindir}/ratbagctl
%{_mandir}/man1/*

%changelog
