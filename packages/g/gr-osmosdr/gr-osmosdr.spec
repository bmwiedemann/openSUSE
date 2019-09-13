#
# spec file for package gr-osmosdr
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

%define sover 0_1_5git0_0_0
%if 0%{?suse_version} >= 1500
%bcond_without xtrx
%endif
Name:           gr-osmosdr
Version:        0.1.4+git.20180815
Release:        0
Summary:        Gnuradio Source for OsmoSDR
License:        GPL-3.0-or-later
# grc/gen_osmosdr_blocks.py => GPL2.0+
# swig/osmosdr_swig.i       => no license specified
Group:          Productivity/Hamradio/Other
URL:            http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
#Git-Clone:     https://git.osmocom.org/gr-osmosdr
Source:         %{name}-%{version}.tar.xz
Patch0:         0001-add-xtrx-support.patch
Patch1:         0002-cmake-use-CMAKE_CURRENT_SOURCE_DIR-instead-of-CMAKE_.patch
Patch2:         0003-add-antenna-AUTO-selection.patch
Patch3:         0004-Add-XTRX-to-README-and-help-output.patch
Patch4:         0005-XTRX-add-ability-to-specify-device-and-DSP-freq.patch
Patch5:         0001-update-for-new-API-and-multi-XTRX-support.patch
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  freesrp-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  python-wxWidgets
BuildRequires:  swig
BuildRequires:  udev
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(gnuradio-fcdproplus)
BuildRequires:  pkgconfig(gnuradio-iqbalance)
BuildRequires:  pkgconfig(gnuradio-runtime)
BuildRequires:  pkgconfig(libairspy)
BuildRequires:  pkgconfig(libbladeRF)
BuildRequires:  pkgconfig(libhackrf)
BuildRequires:  pkgconfig(libmirisdr)
BuildRequires:  pkgconfig(libosmosdr)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.19
BuildRequires:  pkgconfig(uhd)
Requires:       gnuradio-wxgui
Requires:       python-gr-osmosdr = %{version}
%if 0%{?suse_version} > 1500
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%endif
%if 0%{with xtrx}
BuildRequires:  pkgconfig(libxtrx)
%endif

%description
OsmoSDR Gnuradio Source supports the OsmoSDR hardware, but it also offers a
wrapper functionality for FunCube Dongle, Ettus UHD and rtl-sdr radios.

%package -n libgnuradio-osmosdr-%{sover}
Summary:        Library for gr-osmosdr
Group:          System/Libraries

%description -n libgnuradio-osmosdr-%{sover}
OsmoSDR Gnuradio Source supports the OsmoSDR hardware, but it also offers a
wrapper functionality for FunCube Dongle, Ettus UHD and rtl-sdr radios.

%package -n python-gr-osmosdr
Summary:        Python bindings for gr-osmosdr
Group:          Development/Libraries/Other

%description -n python-gr-osmosdr
Python Bindings for gr-osmosdr.
OsmoSDR Gnuradio Source supports the OsmoSDR hardware, but it also offers a
wrapper functionality for FunCube Dongle, Ettus UHD and rtl-sdr radios.

%package devel
Summary:        Development files for gr-osmosdr
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       libgnuradio-osmosdr-%{sover}

%description devel
Library headers for gr-osmosdr.
OsmoSDR Gnuradio Source supports the OsmoSDR hardware, but it also offers a
wrapper functionality for FunCube Dongle, Ettus UHD and rtl-sdr radios.

%package devel-doc
Summary:        Documentation for gnuradio-osmosdr
Group:          Documentation/Other
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description devel-doc
Documentation for gr-osmosdr module for GNU Radio.

%prep
%setup -q
%if 0%{with xtrx}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%endif

%build
%cmake \
    -DENABLE_DOXYGEN=1 \
    -DCMAKE_SHARED_LINKER_FLAGS=""

make %{?_smp_mflags}

%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}/%{_datadir}/doc/%{name} %{buildroot}%{_docdir}
%fdupes %{buildroot}/%{_prefix}

%post -n libgnuradio-osmosdr-%{sover} -p /sbin/ldconfig
%postun -n libgnuradio-osmosdr-%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/osmocom_*
%{_datadir}/gnuradio/grc/blocks/*.xml
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml

%files -n python-gr-osmosdr
%{python_sitearch}/osmosdr

%files -n libgnuradio-osmosdr-%{sover}
%{_libdir}/libgnuradio-osmosdr*.so.*

%files devel
%{_libdir}/libgnuradio-osmosdr*.so
%{_includedir}/osmosdr
%{_libdir}/pkgconfig/gnuradio-osmosdr.pc

%files devel-doc
%{_docdir}/%{name}/html
%{_docdir}/%{name}/xml

%changelog
