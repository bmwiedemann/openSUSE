#
# spec file for package libgpiod
#
# Copyright (c) 2025 SUSE LLC and contributors
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
# Enable tests on openSUSE only - bsc#1243926
%if 0%{?is_opensuse}
%bcond_without libgpiod_tests
%else
%bcond_with libgpiod_tests
%endif
# Enable python
%bcond_without libgpiod_python
Name:           libgpiod
Version:        2.2.2
Release:        0
Summary:        C library and tools for interacting with the linux GPIO character device
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
Source0:        https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-%{version}.tar.gz
Source1:        gpiod-sysusers.conf
BuildRequires:  autoconf >= 2.71
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libgudev-1_0-devel >= 230
BuildRequires:  libkmod-devel
BuildRequires:  libtool
BuildRequires:  make
%if %{with libgpiod_python}
BuildRequires:  python3-devel >= 3.5
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
%endif
%if %{with libgpiod_tests}
BuildRequires:  Catch2-devel
BuildRequires:  glib2-devel >= 2.50
BuildRequires:  kernel-devel >= 5.5
BuildRequires:  pkgconfig(libudev)
%else
BuildRequires:  kernel-devel >= 4.8
%endif
BuildRequires:  systemd

%description
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

%package utils
Summary:        Tools for interacting with the linux GPIO character device
Group:          Development/Libraries/C and C++

%description utils
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Command-line tools part.

%package -n libgpiod%{libgpiod_soversion}
Summary:        C library for interacting with the linux GPIO character device
Group:          System/Libraries
Conflicts:      libgpiod1

%description -n libgpiod%{libgpiod_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

C library part.

%package -n libgpiodbus%{libgpiodbus_soversion}
Summary:        DBus for libgpiod
Group:          System/Libraries
Conflicts:      libgpiod1

%description -n libgpiodbus%{libgpiodbus_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

DBus part.

%package -n libgpiodcxx%{libgpiodcxx_soversion}
Summary:        C++library for interacting with the linux GPIO character device
Group:          System/Libraries
Conflicts:      libgpiod1

%description -n libgpiodcxx%{libgpiodcxx_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

C++ library part.

%package -n libgpiod-glib%{libgpiodglib_soversion}
Summary:        GLib2 binding for libgpiod
Group:          System/Libraries
Conflicts:      libgpiod1

%description -n libgpiod-glib%{libgpiodglib_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Glib2 binding part.

%package -n libgpiosim%{libgpiosim_soversion}
Summary:        C library for controlling the gpio-sim kernel module
Group:          System/Libraries
Conflicts:      libgpiod1

%description -n libgpiosim%{libgpiosim_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

GPIO sim library part. (This aims at replacing the old gpio-mockup)

%package devel
Summary:        Devel files for libgpiod
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Requires:       libgpiod%{libgpiod_soversion} = %{version}
Requires:       libgpiodcxx%{libgpiodcxx_soversion} = %{version}
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
Group:          Development/Languages/Python
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
# python bindings build is set to use isolation. Remove this for distro build so it uses the
# system installed dependencies instead of trying to use pip to install from the network
sed -i 's/-m build/-m pip wheel --wheel-dir dist --no-build-isolation ./' bindings/python/Makefile*
# Once the following commit is merged, replace the above line with the command below:
# https://lore.kernel.org/linux-gpio/20250407181116.1070816-1-yselkowi@redhat.com/T/#u
#sed -i 's/-m pip wheel/& --no-build-isolation/' bindings/python/Makefile*

%build
./autogen.sh
%configure \
  --enable-dbus \
  --enable-systemd \
%if %{with libgpiod_tests}
  --enable-tests \
%endif
  --enable-tools=yes \
%if %{with libgpiod_python}
  --enable-bindings-python \
%else
  --disable-bindings-python \
%endif
  --enable-bindings-glib \
  --enable-bindings-cxx \
  --disable-bindings-rust \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
# Install sysusers file
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/gpiod.conf
# Fix udev rule location
%ifnarch %{ix86} %{arm}
mkdir -p %{buildroot}/%{_udevrulesdir}/
mv -f %{buildroot}/%{_libdir}/udev/rules.d/90-gpio.rules %{buildroot}/%{_udevrulesdir}/90-gpio.rules
%endif
# Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%post -n libgpiod%{libgpiod_soversion} -p /sbin/ldconfig
%postun -n libgpiod%{libgpiod_soversion} -p /sbin/ldconfig
%post -n libgpiodcxx%{libgpiodcxx_soversion} -p /sbin/ldconfig
%postun -n libgpiodcxx%{libgpiodcxx_soversion} -p /sbin/ldconfig
%post -n libgpiodbus%{libgpiodbus_soversion} -p /sbin/ldconfig
%postun -n libgpiodbus%{libgpiodbus_soversion} -p /sbin/ldconfig
%post -n libgpiod-glib%{libgpiodglib_soversion} -p /sbin/ldconfig
%postun -n libgpiod-glib%{libgpiodglib_soversion} -p /sbin/ldconfig

%if %{with libgpiod_tests}
%post -n libgpiosim%{libgpiosim_soversion} -p /sbin/ldconfig
%postun -n libgpiosim%{libgpiosim_soversion} -p /sbin/ldconfig
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
#%%{_mandir}/man*/gpio*

%files -n libgpiod%{libgpiod_soversion}
%{_libdir}/libgpiod.so.%{libgpiod_soversion}
%{_libdir}/libgpiod.so.%{libgpiod_soversion}.*

%files -n libgpiodbus%{libgpiodbus_soversion}
%{_libdir}/libgpiodbus.so.%{libgpiodbus_soversion}
%{_libdir}/libgpiodbus.so.%{libgpiodbus_soversion}.*

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

%files devel
%{_includedir}/*.h*
%dir %{_includedir}/gpiod-glib/
%{_includedir}/gpiod-glib/*.h
%dir %{_includedir}/gpiodcxx/
%{_includedir}/gpiodcxx/*.hpp
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgpiod.pc
%{_libdir}/pkgconfig/libgpiodcxx.pc
%{_libdir}/pkgconfig/gpiod-glib.pc

%if %{with libgpiod_python}
%files -n python3-gpiod
%{python3_sitearch}/gpiod/
%{python3_sitearch}/gpiod-*.dist-info
%endif

%files manager
%{_bindir}/gpio-manager
%{_bindir}/gpiocli
%config %{_sysconfdir}/dbus-1/system.d/io.gpiod1.conf
%{_datadir}/dbus-1/interfaces/io.gpiod1.xml
%{_unitdir}/gpio-manager.service

%changelog
