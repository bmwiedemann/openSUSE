#
# spec file for package gr-iqbal
#
# Copyright (c) 2020 SUSE LLC
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


%define libname libgnuradio-iqbalance3_8_0
Name:           gr-iqbal
Version:        0.38.1
Release:        0
Summary:        GNU Radio I/Q balancing
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://git.osmocom.org/gr-iqbal/
Source:         %{name}-%{version}.tar.gz
Patch0:         0001-boost-qualify-placeholders-with-their-full-namespace.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libosmo-dsp-devel
BuildRequires:  orc
BuildRequires:  pkgconfig
BuildRequires:  python3-six
BuildRequires:  swig
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(gnuradio-runtime) >= 3.8.0
BuildRequires:  pkgconfig(python3)

%description
I/Q balancing for GNU Radio

%package -n %{libname}
Summary:        Libraries for gr-iqbal
Group:          System/Libraries

%description -n %{libname}
I/Q balancing for GNU Radio

%package -n %{name}-grc
Summary:        GRC blocks for gr-iqbal
Group:          Productivity/Hamradio/Other
Requires:       %{libname} = %{version}
# GRC yaml files where in the library package previously
Conflicts:      libgnuradio-iqbalance0_37_2git
Provides:       libgnuradio-iqbalance0_37_2git:%{_datadir}/gnuradio/grc/blocks/iqbalance_fix_cc.block.yml
BuildArch:      noarch

%description -n %{name}-grc
GNU Radio Companion (GRC) definitions for the
gr-iqbal I/Q balancing block.

%package -n python3-gr-iqbal
Summary:        Python bindings for gr-iqbal
Group:          Development/Libraries/Python
Requires:       %{libname} = %{version}

%description -n python3-gr-iqbal
The Python Bindings for gr-iqbal.

%package -n libgnuradio-iqbalance-devel
Summary:        Development files for gr-iqbal
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Conflicts:      libgnuradio-iqbalance <= 0.37.2+git.20151121

%description -n libgnuradio-iqbalance-devel
Library headers for gr-iqbal, I/Q balancing for GNU Radio

%package devel-doc
Summary:        Documentation for gr-iqbal
Group:          Documentation/HTML
Recommends:     libgnuradio-iqbalance-devel = %{version}
BuildArch:      noarch

%description devel-doc
Documentation for gr-iqbal module for GNU Radio.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
  -Wno-dev
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}/%{_datadir}/doc/gr-iqbalance %{buildroot}%{_docdir}/

%fdupes %{buildroot}%{python3_sitearch}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc AUTHORS
%license COPYING
%{_libdir}/libgnuradio-iqbalance.so.*

%files -n %{name}-grc
%{_datadir}/gnuradio

%files -n python3-gr-iqbal
%{python3_sitearch}/gnuradio/iqbalance

%files -n libgnuradio-iqbalance-devel
%{_includedir}/gnuradio/iqbalance
%{_includedir}/gnuradio/swig
%{_libdir}/libgnuradio-iqbalance.so
%{_libdir}/cmake/gnuradio/gnuradio-iqbalance*

%files devel-doc
%dir %{_docdir}/gr-iqbalance
%{_docdir}/gr-iqbalance/html
%{_docdir}/gr-iqbalance/xml

%changelog
