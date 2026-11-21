#
# spec file for package libiio
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


%define so_ver  1
Name:           libiio
Version:        1.0.0
Release:        0
Summary:        Industrial I/O tools
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            https://wiki.analog.com/resources/tools-software/linux-software/libiio
Source:         https://github.com/analogdevicesinc/libiio/archive/v%{version}.tar.gz#/libiio-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  cmake >= 3.13
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libaio-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(libserialport)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
%{?systemd_requires}

%description
libiio is used to interface to the Linux Industrial Input/Output
(IIO) Subsystem, which provides support for devices that in some
sense are analog to digital or digital to analog converters (ADCs,
DACs), e.g. sensors, amplifiers, RF transceivers, etc.

%package -n libiio%{so_ver}
Summary:        Industrial I/O library

%description -n libiio%{so_ver}
libiio is used to interface to the Linux Industrial Input/Output
(IIO) Subsystem, which provides support for devices that in some
sense are analog to digital or digital to analog converters (ADCs,
DACs), e.g. sensors, amplifiers, RF transceivers, etc.

%package devel
Summary:        Development files for the Industrial I/O library
Requires:       libiio%{so_ver} = %{version}-%{release}
Recommends:     libiio = %{version}-%{release}

%description devel
Library for industrial I/O.

This sub-package contains the development files.

%package -n python3-pylibiio
Summary:        Python bindings for the Industrial I/O library
Requires:       libiio%{so_ver} = %{version}-%{release}
Obsoletes:      libiio-python < %{version}-%{release}
Provides:       libiio-python = %{version}-%{release}

%description -n python3-pylibiio
Library for industrial I/O.

This sub-package contains the Python bindings.

%package daemon
Summary:        Industrial I/O library device sharing daemon

%description daemon
iiod's purpose is to share local IIO hardware devices over a network,
USB, or serial connection so they can be accessed remotely by other
machines

%package usb-udev-rules
Summary:        udev rules for the Industrial I/O library

%description usb-udev-rules
Library for industrial I/O.

This sub-package contains a udev rule for granting access to IIO targets
using the USB transport/backend.

%prep
%autosetup -p1
# __init__.py is imported, never executed: drop the shebang so rpmlint
# does not flag it as a non-executable script
sed -i '1{/^#!/d}' bindings/python/iio/__init__.py

%build
# The 0.x compatibility library has no SONAME, so it is not shipped.
%cmake \
  -DWITH_SYSTEMD=1 \
  -DWITH_TESTS=ON \
  -DLIBIIO_COMPAT=OFF \
  -DUDEV_RULES_INSTALL_DIR=%{_udevrulesdir} \
  -DSYSTEMD_UNIT_INSTALL_DIR=%{_unitdir}
%cmake_build
# The Python bindings are no longer installed by CMake, build a wheel instead
# NOTE: %%cmake_build leaves cwd in build/, hence ../
cd ../bindings/python
%python3_pyproject_wheel

%install
%cmake_install
# Upstream leaves the build-tree RUNPATH in the installed utils; drop it
chrpath --delete %{buildroot}%{_bindir}/iio*
# NOTE: each section starts in the source dir, unlike %%build above
cd bindings/python
%python3_pyproject_install

%check
# tests/hardware/test_ad9364 exits 0 without URI_AD9361 set (no hardware)
%ctest

%ldconfig_scriptlets -n libiio%{so_ver}

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
%{_bindir}/iio_attr
%{_bindir}/iio_event
%{_bindir}/iio_genxml
%{_bindir}/iio_info
%{_bindir}/iio_ping
%{_bindir}/iio_reg
%{_bindir}/iio_rwdev
%{_bindir}/iio_stresstest

%files -n libiio%{so_ver}
%{_libdir}/libiio.so.%{so_ver}*

%files -n libiio-devel
%{_includedir}/iio/
%{_libdir}/libiio.so
%{_libdir}/pkgconfig/libiio.pc

%files -n python3-pylibiio
%{python3_sitelib}/iio
%{python3_sitelib}/pylibiio-*-info

%files daemon
%{_sbindir}/iiod
%{_unitdir}/iiod.service

%files usb-udev-rules
%{_udevrulesdir}/90-libiio.rules

%changelog
