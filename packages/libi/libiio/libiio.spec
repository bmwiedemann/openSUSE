#
# spec file for package libiio
#
# Copyright (c) 2022 SUSE LLC
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


%define so_ver  0
Name:           libiio
Version:        0.24
Release:        0
Summary:        Industrial I/O tools
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://wiki.analog.com/resources/tools-software/linux-software/libiio
Source:         https://github.com/analogdevicesinc/libiio/archive/v%{version}.tar.gz#/libiio-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  libaio-devel
BuildRequires:  libavahi-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  libxml2-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}

%description
Library for industrial I/O.

%package -n libiio%{so_ver}
Summary:        Industrial I/O library
Group:          System/Libraries

%description -n libiio%{so_ver}
Library for industrial I/O.

%package devel
Summary:        Industrial I/O library -- development files
Group:          Development/Libraries/C and C++
Requires:       libiio%{so_ver} = %{version}-%{release}
Recommends:     libiio = %{version}-%{release}

%description devel
Library for industrial I/O.

This sub-package contains the development files.

%package -n python3-pylibiio
Summary:        Industrial I/O library -- Python bindings
Group:          System/Libraries
Obsoletes:      libiio-python < %{version}-%{release}
Provides:       libiio-python = %{version}-%{release}

%description -n python3-pylibiio
Library for industrial I/O.

This sub-package contains the Python bindings.

%package daemon
Summary:        Industrial I/O library -- iiod
Group:          System/Libraries

%description daemon
Library for industrial I/O.

This sub-package contains the iiod daemon.

%package usb-udev-rules
Summary:        Industrial I/O library -- iiod
Group:          System/Libraries

%description usb-udev-rules
Library for industrial I/O.

This sub-package contains a udev rule for granting access to IIO targets
using the USB transport/backend.


%prep
%setup -q
sed -i '1s|#!/usr/bin/env python|#!/usr/bin/python3|g' bindings/python/iio.py

%build
%cmake \
  -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
  -DUDEV_RULES_INSTALL_DIR=%{_udevrulesdir} \
  -DWITH_SYSTEMD=1 \
  -DPYTHON_BINDINGS=ON \
  -DSYSTEMD_UNIT_INSTALL_DIR=%{_unitdir}
%cmake_build

%install
%cmake_install
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rciiod

%check
%ctest

%post -n libiio%{so_ver} -p /sbin/ldconfig
%postun -n libiio%{so_ver} -p /sbin/ldconfig

%pre daemon
%service_add_pre iiod.service

%post daemon
%service_add_post iiod.service

%preun daemon
%service_del_preun iiod.service

%postun daemon
%service_del_postun iiod.service

%files
%license COPYING.txt
%doc README.md
%{_bindir}/iio_adi_xflow_check
%{_bindir}/iio_attr
%{_bindir}/iio_genxml
%{_bindir}/iio_info
%{_bindir}/iio_readdev
%{_bindir}/iio_reg
%{_bindir}/iio_stresstest
%{_bindir}/iio_writedev

%files -n libiio%{so_ver}
%{_libdir}/libiio.so.%{so_ver}*


%files -n libiio-devel
%{_includedir}/iio.h
%{_libdir}/libiio.so
%{_libdir}/pkgconfig/libiio.pc

%files -n python3-pylibiio
%{python3_sitelib}/*

%files daemon
%{_sbindir}/iiod
%{_sbindir}/rciiod
%{_unitdir}/iiod.service

%files usb-udev-rules
%{_udevrulesdir}

%changelog
