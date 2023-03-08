#
# spec file for package libusrp
#
# Copyright (c) 2021-2023 SUSE LLC
# Copyright (c) 2018-2021, Martin Hauke <mardnh@gmx.de>
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


%define sover   1
%define libname libusrp%{sover}
Name:           libusrp
Version:        3.4.7
Release:        0
Summary:        Stand-alone libusrp for USRP1 from old gnuradio.git
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://git.osmocom.org/libusrp
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  sdcc
BuildRequires:  pkgconfig(libusb-1.0)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel
%endif

%description
Stand-alone libusrp for USRP1 from old gnuradio.git.

%package -n %{libname}
Summary:        Stand-alone libusrp for USRP1 from old gnuradio.git
Group:          System/Libraries

%description -n %{libname}
Stand-alone libusrp for USRP1 from old gnuradio.git.

%package devel
Summary:        Development files for libusrp
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Stand-alone libusrp for USRP1 from old gnuradio.git.

This subpackage contains libraries and header files for developing
applications that want to make use of libusrp.

%package -n usrp-tools
Summary:        Tools for the URSP1 SDR
Group:          Hardware/Other

%description -n usrp-tools
Tools for the URSP1 SDR.

%package -n usrp-firmware
Summary:        Firmware files for the URSP1 SDR
Group:          Hardware/Other
Requires:       usrp-tools = %{version}
BuildArch:      noarch

%description -n usrp-firmware
Firmware files for the USRP1 SDR.

%prep
%setup -q

%build
echo "%{version}" >.tarball-version
autoreconf -fiv
%configure
# parallel build is br0ken
# -> https://osmocom.org/issues/3970#change-15556
make V=1 # %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/libusrp.la
# FIXME: gnuradio swig stuff shouldn't be there
rm -rf %{buildroot}%{_includedir}/gnuradio/
%fdupes %{buildroot}%{_datadir}/usrp

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n usrp-tools
%{_bindir}/usrp_cal_dc_offset
%{_bindir}/usrper

%files -n %{libname}
%{_libdir}/libusrp*.so.*

%files -n usrp-firmware
%dir %{_datadir}/usrp
%{_datadir}/usrp/rev2
%{_datadir}/usrp/rev4

%files devel
%{_includedir}/usrp
%{_libdir}/libusrp.so
%{_libdir}/pkgconfig/usrp.pc

%changelog
