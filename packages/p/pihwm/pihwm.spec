#
# spec file for package pihwm
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define version_unconverted 0.0.0+git.20131231
Name:           pihwm
Version:        0.0.0+git.20131231
Release:        0
Summary:        A collection of lightweight drivers for Raspberry Pi peripherals
License:        Apache-2.0
Group:          Hardware/Other
Url:            http://omerk.github.io/pihwm
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE disable-doxygen-timestamp.patch - matwey.kornilov@gmail.com
Patch1:         disable-doxygen-timestamp.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  groff
BuildRequires:  i2c-tools
BuildRequires:  kernel-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{arm} aarch64

%description
pihwm is a collection of lightweight drivers for the hardware peripherals
on the Raspberry Pi computer.

%package -n libpihwm0
Summary:        A lightweight C library for Raspberry Pi hardware modules
Group:          System/Libraries

%description -n libpihwm0
pihwm is a collection of lightweight drivers for the hardware peripherals
on the Raspberry Pi computer.

This package contains shared library.

%package devel
Summary:        Development libraries and header files for pihwm
Group:          Development/Languages/C and C++
Requires:       i2c-tools
Requires:       libpihwm0 = %{version}

%description devel
pihwm is a collection of lightweight drivers for the hardware peripherals
on the Raspberry Pi computer.

This package contains devel files.

%prep
%setup -q
%patch1 -p1

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags} CFLAGS="%{optflags}" V=1 all pdf

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install install-pdf
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print
%fdupes -s doc/html

%post -n libpihwm0 -p /sbin/ldconfig
%postun -n libpihwm0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/board_info
%{_bindir}/check_kernel_modules
%{_bindir}/gpio_int
%{_bindir}/gpio_ledborg
%{_bindir}/gpio_test
%{_bindir}/i2c_ads1015
%{_bindir}/i2c_hmc6352
%{_bindir}/i2c_mcp23008
%{_bindir}/pwm_demo
%{_bindir}/spi_bb_mcp3202
%{_bindir}/spi_mcp3002
%{_bindir}/spi_test

%files -n libpihwm0
%defattr(-,root,root)
%{_libdir}/libpihwm.so.0
%{_libdir}/libpihwm.so.0.0.0

%files devel
%defattr(-,root,root)
%doc doc/html
%{_libdir}/libpihwm.so
%{_includedir}/pi_gpio.h
%{_includedir}/pihwm.h
%{_includedir}/pi_i2c.h
%{_includedir}/pi_pwm.h
%{_includedir}/pi_spi.h

%changelog
