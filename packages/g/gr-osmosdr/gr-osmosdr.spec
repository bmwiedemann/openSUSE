#
# spec file for package gr-osmosdr
#
# Copyright (c) 2024 SUSE LLC
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


%define with_sdrplay 0
%define libname libgnuradio-osmosdr
%define sover 0_2_0
Name:           gr-osmosdr
Version:        0.2.6
Release:        0
Summary:        Gnuradio Source for OsmoSDR
License:        GPL-3.0-or-later
# grc/gen_osmosdr_blocks.py => GPL2.0+
# swig/osmosdr_swig.i       => no license specified
Group:          Productivity/Hamradio/Other
URL:            https://sdr.osmocom.org/trac/wiki/GrOsmoSDR
#Git-Clone:     https://git.osmocom.org/gr-osmosdr
Source:         %{name}-%{version}.tar.gz
BuildRequires:  airspy-devel
BuildRequires:  airspyhf-devel
BuildRequires:  bladeRF-devel
BuildRequires:  cmake >= 3.13
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  freesrp-devel
BuildRequires:  gcc-c++
BuildRequires:  gnuradio-devel
BuildRequires:  hackrf-devel
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libgnuradio-funcube-devel
BuildRequires:  libgnuradio-iqbalance-devel
BuildRequires:  libmirisdr-devel
BuildRequires:  libosmo-dsp-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libunwind-devel
BuildRequires:  libusb-1_0-devel >= 1.0.19
BuildRequires:  orc
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-pybind11-devel
BuildRequires:  python3-six
BuildRequires:  rtl-sdr-devel
BuildRequires:  soapy-sdr-devel
BuildRequires:  udev
BuildRequires:  uhd-devel
Requires:       python3-gr-osmosdr = %{version}
%if 0%{with_sdrplay}
# SDRplay support via libsdrplay2 from
# https://github.com/willcode/gr-osmosdr/tree/sdrplay2
Source1:        gr-osmosdr-sdrplay2-support-git20180914.tar.gz
Patch2:         gr-osmosdr-add-sdrplay2-support-git20180914-gr38.patch
Patch7:         gr-osmosdr-0007-sdrplay-use-std-ptr.patch
%endif
%ifarch i586 x86_64 aarch64 armv7hl
BuildRequires:  libxtrx-devel
%endif
%if 0%{with_sdrplay}
BuildRequires:  sdrplay-devel
%endif

%description
OsmoSDR Gnuradio Source supports the OsmoSDR hardware, but it also offers a
wrapper functionality for FunCube Dongle, Ettus UHD and rtl-sdr radios.

%package -n %{libname}%{sover}
Summary:        Library for gr-osmosdr
Group:          System/Libraries

%description -n %{libname}%{sover}
OsmoSDR Gnuradio Source supports the OsmoSDR hardware, but it also offers a
wrapper functionality for FunCube Dongle, Ettus UHD and rtl-sdr radios.

%package -n python3-gr-osmosdr
Summary:        Python bindings for gr-osmosdr
Group:          Development/Libraries/Other

%description -n python3-gr-osmosdr
Python Bindings for gr-osmosdr.
OsmoSDR Gnuradio Source supports the OsmoSDR hardware, but it also offers a
wrapper functionality for FunCube Dongle, Ettus UHD and rtl-sdr radios.

%package devel
Summary:        Development files for gr-osmosdr
Group:          Development/Libraries/Other
Requires:       %{libname}%{sover} = %{version}-%{release}
Requires:       %{name} = %{version}

%description devel
Library headers for gr-osmosdr.
OsmoSDR Gnuradio Source supports the OsmoSDR hardware, but it also offers a
wrapper functionality for FunCube Dongle, Ettus UHD and rtl-sdr radios.

%package doc
Summary:        Documentation for gnuradio-osmosdr
Group:          Documentation/Other
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for gr-osmosdr module for GNU Radio.

%prep
%setup -q

%if 0%{with_sdrplay}
tar -xzf %{SOURCE1}
%patch -P 2 -p 1
%patch -P 7 -p 1
%endif

%build
%cmake \
%if 0%{with_sdrplay}
    -DENABLE_NONFREE=1 \
%endif
    -DENABLE_FREESRP=0 \
    -DENABLE_XTRX=0 \
    -DENABLE_DOXYGEN=1 \
    -DCMAKE_SHARED_LINKER_FLAGS=""

%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}/%{_datadir}/doc/%{name} %{buildroot}%{_docdir}
%fdupes %{buildroot}/%{_prefix}

%post -n %{libname}%{sover} -p /sbin/ldconfig
%postun -n %{libname}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/osmocom_*
%{_datadir}/gnuradio/grc/blocks/*.yml
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml

%files -n python3-gr-osmosdr
%{python3_sitearch}/osmosdr

%files -n %{libname}%{sover}
%{_libdir}/%{libname}*.so.*

%files devel
%{_libdir}/%{libname}*.so
%{_includedir}/osmosdr
%{_libdir}/cmake/osmosdr

%files doc
%{_docdir}/%{name}/html
%{_docdir}/%{name}/xml

%changelog
