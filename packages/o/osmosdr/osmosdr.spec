#
# spec file for package osmosdr
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   0
%define libname lib%{name}%{sover}
Name:           osmosdr
Version:        0.1+git.20151211
Release:        0
Summary:        SDR (Software Defined Radio) project
# The primary code is GPL-2.0, but the following firmware files are licenced under GPL3.0+
# firmware/include/{si570.h,tuner_e4k.h,uart_cmd.h}
# firmware/src/{fast_source.c,logging.c,osdr_fpga.c,osdr_ssc.c,reg_field.c,si570.c,tuner_e4k.c,tuner_e4k_transport.c,uart_cmd.c}
License:        GPL-3.0
Group:          Productivity/Hamradio/Other
Url:            http://sdr.osmocom.org/trac/
Source:         %{name}-%{version}.tar.xz
Patch0:         osmosdr-cmake-libsuffix.diff
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
OsmoSDR is a software-based small form factor Software Defined Radio project.

%package -n %{libname}
Summary:        Libraries for OsmoSDR
Group:          System/Libraries

%description -n %{libname}
OsmoSDR is a software-based small form factor Software Defined Radio project.

%package devel
Summary:        Development files for OsmoSDR
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Library headers for OsmoSDR.
OsmoSDR is a software-based small form factor Software Defined Radio project.

%prep
%setup -q -n %{name}-%{version}/software/libosmosdr/
%patch0 -p3

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
rm -rf %{buildroot}%{_libdir}/libosmosdr.a

# install udev rules
install -m 0644 -D osmosdr.rules %{buildroot}%{_udevrulesdir}/10-osmosdr.rules

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/osmo_sdr
%{_udevrulesdir}/10-osmosdr.rules

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libosmosdr.so.%{sover}*

%files devel
%defattr(-,root,root)
%{_libdir}/libosmosdr.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/libosmosdr.pc

%changelog
