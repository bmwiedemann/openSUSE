#
# spec file for package libperseus-sdr
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define sover 0
%define libname %{name}%{sover}
%define perseussdr_group perseususb
Name:           libperseus-sdr
Version:        0.8.1
Release:        0
Summary:        Perseus Software Defined Radio Control Library
License:        GPL-3.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/Microtelecom/libperseus-sdr
#Git-Clone:     https://github.com/Microtelecom/libperseus-sdr.git
Source:         https://github.com/Microtelecom/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  vim
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
Perseus Software Defined Radio Control Library.

%package devel
Summary:        Development files for libperseus-sdr
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Libraries and header files for developing applications that want to
make use of libperseus-sdr.

%package -n %{libname}
Summary:        Library for Perseus SDR
Group:          System/Libraries
Requires:       %{name}-udev

%description -n %{libname}
Perseus Software Defined Radio Control Library.

%package -n perseus-sdr-tools
Summary:        Tools for Perseus SDR
Group:          Hardware/Other

%description -n perseus-sdr-tools
Tools for Perseus SDR devices.

%package udev
Summary:        Udev rules for Perseus SDR
Group:          Hardware/Other
Requires(pre):  pwdutils

%description udev
Udev rules for Perseus SDR hardware

%prep
%setup -q
#
%build
# Do not optimize for current cpu
sed -i "s|-march=native||g" configure.ac
autoreconf -iv
%configure
make #%{?_smp_mflags} # parallel build is broken

%install
%make_install
install -Dm0644 95-perseus.rules %{buildroot}%{_udevrulesdir}/95-perseus.rules
# delete unnecessary files
rm %{buildroot}/%{_bindir}/95-perseus.rules
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print

%pre udev
getent group %{perseussdr_group} >/dev/null || groupadd -r %{perseussdr_group}

%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%post -n %{libname} -p /sbin/ldconfig
%postun  -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc AUTHORS README.md
%license COPYING.LESSER
%{_libdir}/libperseus-sdr.so.*

%files -n perseus-sdr-tools
%{_bindir}/perseustest
%{_bindir}/perseustest_dyn

%files udev
%{_udevrulesdir}/95-perseus.rules

%files devel
%{_libdir}/libperseus-sdr.so
%{_includedir}/perseus-sdr.h
#%%{_includedir}/perseus-in.h
#%%{_includedir}/perseus-sdr.h
#%%{_includedir}/perseuserr.h
#%%{_includedir}/perseusfx2.h

%changelog
