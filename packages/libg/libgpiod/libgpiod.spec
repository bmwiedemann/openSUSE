#
# spec file for package libgpiod
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


%define libgpiod_soversion 3
%define libgpiodbus_soversion 1
%define libgpiodcxx_soversion 2
%define libgpiodglib_soversion 1
%define libgpiosim_soversion 1
%define libgpiotools_soversion 1
# Enable tests on openSUSE only - bsc#1243926
%if 0%{?is_opensuse}
%bcond_without libgpiod_tests
%else
%bcond_with libgpiod_tests
%endif
# Enable python
%bcond_without libgpiod_python
Name:           libgpiod
Version:        2.3.1
Release:        0
Summary:        C library and tools for interacting with the linux GPIO character device
License:        LGPL-2.1-or-later
URL:            https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
Source0:        https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-%{version}.tar.gz
Source1:        gpiod-sysusers.conf
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.80
BuildRequires:  help2man
BuildRequires:  libgudev-1_0-devel >= 230
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  systemd
%if %{with libgpiod_python}
BuildRequires:  python3-devel >= 3.10
%endif
%if %{with libgpiod_tests}
BuildRequires:  Catch2-devel >= 3.0
BuildRequires:  kernel-devel >= 5.5
BuildRequires:  libkmod-devel
BuildRequires:  libmount-devel >= 2.33.1
BuildRequires:  pkgconfig(libudev)
%else
BuildRequires:  kernel-devel >= 4.8
%endif

%description
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

%package utils
Summary:        Tools for interacting with the linux GPIO character device

%description utils
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Command-line tools part.

%package -n libgpiod%{libgpiod_soversion}
Summary:        C library for interacting with the linux GPIO character device
Conflicts:      libgpiod1

%description -n libgpiod%{libgpiod_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

C library part.

%package -n libgpiodbus%{libgpiodbus_soversion}
Summary:        DBus for libgpiod
Conflicts:      libgpiod1

%description -n libgpiodbus%{libgpiodbus_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

DBus part.

%package -n libgpiodcxx%{libgpiodcxx_soversion}
Summary:        C++library for interacting with the linux GPIO character device
Conflicts:      libgpiod1

%description -n libgpiodcxx%{libgpiodcxx_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

C++ library part.

%package -n libgpiod-glib%{libgpiodglib_soversion}
Summary:        GLib2 binding for libgpiod
Conflicts:      libgpiod1

%description -n libgpiod-glib%{libgpiodglib_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Glib2 binding part.

%package -n libgpiosim%{libgpiosim_soversion}
Summary:        C library for controlling the gpio-sim kernel module
Conflicts:      libgpiod1

%description -n libgpiosim%{libgpiosim_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

GPIO sim library part. (This aims at replacing the old gpio-mockup)

%package -n libgpiotools%{libgpiotools_soversion}
Summary:        High-level helpers for building programs using libgpiod

%description -n libgpiotools%{libgpiotools_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

High-level helpers part (e.g. line name lookup), previously only
available internally to gpio-tools.

%package devel
Summary:        Devel files for libgpiod
Requires:       %{name} = %{version}
Requires:       libgpiod%{libgpiod_soversion} = %{version}
Requires:       libgpiodcxx%{libgpiodcxx_soversion} = %{version}
Requires:       libgpiotools%{libgpiotools_soversion} = %{version}
%if %{with libgpiod_tests}
Requires:       libgpiosim%{libgpiosim_soversion} = %{version}
%endif

%description devel
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Devel files part.

%if %{with libgpiod_python}
%package -n python3-gpiod
Summary:        Python binding for libgpiod
Provides:       python-libgpiod
Obsoletes:      python-libgpiod

%description -n python3-gpiod
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Python binding part.
%endif

%package        manager
Summary:        DBus manager for GPIO
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description manager
DBus manager for interacting with GPIO character devices.

%prep
%autosetup -p1

%build
%meson \
  -Ddbus=enabled \
  -Dsystemd=enabled \
  -Dtools=enabled \
  -Dbindings-cxx=enabled \
  -Dbindings-glib=enabled \
  -Dbindings-rust=disabled \
  -Dintrospection=disabled \
  -Dgpioset-interactive=disabled \
%if %{with libgpiod_tests}
  -Dtests=enabled \
%else
  -Dtests=disabled \
%endif
%if %{with libgpiod_python}
  -Dbindings-python=enabled
%else
  -Dbindings-python=disabled
%endif
%meson_build

%install
%meson_install
# Install sysusers file
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/gpiod.conf
# Fix udev rule location
%ifnarch %{ix86} %{arm}
mkdir -p %{buildroot}/%{_udevrulesdir}/
mv -f %{buildroot}/%{_libdir}/udev/rules.d/90-gpio.rules %{buildroot}/%{_udevrulesdir}/90-gpio.rules
%endif
# Remove libtool archives and static libraries.
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -name '*.a' -delete

%ldconfig_scriptlets -n libgpiod%{libgpiod_soversion}
%ldconfig_scriptlets -n libgpiodcxx%{libgpiodcxx_soversion}
%ldconfig_scriptlets -n libgpiodbus%{libgpiodbus_soversion}
%ldconfig_scriptlets -n libgpiod-glib%{libgpiodglib_soversion}
%ldconfig_scriptlets -n libgpiotools%{libgpiotools_soversion}

%if %{with libgpiod_tests}
%ldconfig_scriptlets -n libgpiosim%{libgpiosim_soversion}
%endif

%pre manager
%service_add_pre gpio-manager.service

%post manager
%service_add_post gpio-manager.service

%preun manager
%service_del_preun gpio-manager.service

%postun manager
%service_del_postun  gpio-manager.service

%files
%license COPYING
%doc README.md
%{_sysusersdir}/gpiod.conf
%{_udevrulesdir}/90-gpio.rules

%files utils
%{_bindir}/gpiodetect
%{_bindir}/gpioget
%{_bindir}/gpioinfo
%{_bindir}/gpiomon
%{_bindir}/gpionotify
%{_bindir}/gpioset
%{_mandir}/man1/gpiodetect.1%{?ext_man}
%{_mandir}/man1/gpioget.1%{?ext_man}
%{_mandir}/man1/gpioinfo.1%{?ext_man}
%{_mandir}/man1/gpiomon.1%{?ext_man}
%{_mandir}/man1/gpionotify.1%{?ext_man}
%{_mandir}/man1/gpioset.1%{?ext_man}

%files -n libgpiod%{libgpiod_soversion}
%{_libdir}/libgpiod.so.%{libgpiod_soversion}
%{_libdir}/libgpiod.so.%{libgpiod_soversion}.*

%files -n libgpiodbus%{libgpiodbus_soversion}
# Upstream builds gpiodbus with both_libraries() and no version, so the
# installed file is exactly the SONAME with no dotted version suffix.
%{_libdir}/libgpiodbus.so.%{libgpiodbus_soversion}

%files -n libgpiodcxx%{libgpiodcxx_soversion}
%{_libdir}/libgpiodcxx.so.%{libgpiodcxx_soversion}
%{_libdir}/libgpiodcxx.so.%{libgpiodcxx_soversion}.*

%files -n libgpiod-glib%{libgpiodglib_soversion}
%{_libdir}/libgpiod-glib.so.%{libgpiodglib_soversion}
%{_libdir}/libgpiod-glib.so.%{libgpiodglib_soversion}.*

%if %{with libgpiod_tests}
%files -n libgpiosim%{libgpiosim_soversion}
%{_libdir}/libgpiosim.so.%{libgpiosim_soversion}
%{_libdir}/libgpiosim.so.%{libgpiosim_soversion}.*
%endif

%files -n libgpiotools%{libgpiotools_soversion}
%{_libdir}/libgpiotools.so.%{libgpiotools_soversion}
%{_libdir}/libgpiotools.so.%{libgpiotools_soversion}.*

%files devel
%{_includedir}/*.h*
%dir %{_includedir}/gpiod-glib/
%{_includedir}/gpiod-glib/*.h
%dir %{_includedir}/gpiodcxx/
%{_includedir}/gpiodcxx/*.hpp
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgpiod.pc
%{_libdir}/pkgconfig/libgpiodcxx.pc
%{_libdir}/pkgconfig/libgpiotools.pc
%{_libdir}/pkgconfig/gpiod-glib.pc

%if %{with libgpiod_python}
%files -n python3-gpiod
%{python3_sitearch}/gpiod/
%{python3_sitelib}/gpiod/
%endif

%files manager
%{_bindir}/gpio-manager
%{_bindir}/gpiocli
%config %{_sysconfdir}/dbus-1/system.d/io.gpiod1.conf
%{_datadir}/dbus-1/interfaces/io.gpiod1.xml
%{_mandir}/man1/gpio-manager.1%{?ext_man}
%{_mandir}/man1/gpiocli*.1%{?ext_man}
%{_unitdir}/gpio-manager.service

%changelog
