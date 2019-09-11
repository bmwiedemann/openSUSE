#
# spec file for package libxtrxll
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define xtrx_group xtrx
%define sover   0
%define libname libxtrxll%{sover}
Name:           libxtrxll
Version:        0.0.0+git.20190113
Release:        0
Summary:        XTRX Low-level API library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://xtrx.io
#Git-Clone:     https://github.com/xtrx-sdr/libxtrxll.git
Source:         %{name}-%{version}.tar.xz
Patch0:         libxtrxll-fix-udev-permissions.patch
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(libusb3380)

%description
Low level XTRX hardware abstraction library.

%package -n %{libname}
Summary:        XTRX Low-level API library
Group:          System/Libraries
Requires:       xtrx-usb-udev

%description -n %{libname}
Low level XTRX hardware abstraction library.

%package devel
Summary:        XTRX Low-level API library - devel
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Low level XTRX hardware abstraction library.

This subpackage contains libraries and header files for developing
applications that want to make use of libxtrxll.

%package -n xtrxll-tools
Summary:        Low level tools for XTRX
Group:          Hardware/Other

%description -n xtrxll-tools
Low level tools for XTRX SDR devices.

%package -n xtrx-usb-udev
Summary:        Udev rules for XTRX USB devices
Group:          Hardware/Other
Requires(pre):  pwdutils
Provides:       xtrx-udev = %{version}
Obsoletes:      xtrx-udev < %{version}
BuildArch:      noarch

%description -n xtrx-usb-udev
Udev rules for XTRX USB devices.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS="" \
%ifarch %{ix86} x86_64
    -DFORCE_ARCH=x86_64 \
%endif
%ifarch %{arm} aarch64
    -DFORCE_ARCH=arm \
%endif
    -DENABLE_PCIE=ON \
    -DENABLE_USB3380=ON \
    -DINSTALL_UDEV_RULES=ON \
    -DUDEV_RULES_PATH=%{_udevrulesdir}
%make_jobs

%install
%cmake_install
install -d %{buildroot}/%{_bindir}
mv %{buildroot}%{_libdir}/xtrxll/test_xtrxflash %{buildroot}/%{_bindir}
mv %{buildroot}%{_libdir}/xtrxll/test_xtrxll %{buildroot}/%{_bindir}

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%pre -n xtrx-usb-udev
getent group %{xtrx_group} >/dev/null || groupadd -r %{xtrx_group}

%post -n xtrx-usb-udev
%udev_rules_update

%postun -n xtrx-usb-udev
%udev_rules_update

%files -n xtrx-usb-udev
%{_udevrulesdir}/50-xtrx.rules

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libxtrxll.so.%{sover}*

%files devel
%{_includedir}/xtrxll_*.h
%{_libdir}/libxtrxll.so
%{_libdir}/pkgconfig/libxtrxll.pc

%files -n xtrxll-tools
%{_bindir}/test_xtrxflash
%{_bindir}/test_xtrxll

%files -n xtrx-usb-udev
%{_udevrulesdir}/50-xtrx-usb3380.rules

%changelog
