#
# spec file for package gr-iqbal
#
# Copyright (c) 2020-2022 SUSE LLC
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


%define libname libgnuradio-iqbalance
%define soname 3_9_0

Name:           gr-iqbal
Version:        0.39.0git20210108
Release:        0
Summary:        GNU Radio I/Q balancing
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://git.osmocom.org/gr-iqbal/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  gnuradio-devel >= 3.9.0
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libosmo-dsp-devel
BuildRequires:  libunwind-devel
BuildRequires:  orc
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-pybind11-devel
%if 0%{?suse_version} <= 1500
BuildRequires:  python3-six
%endif

%description
I/Q balancing for GNU Radio

%package -n %{libname}%{soname}
Summary:        Libraries for gr-iqbal
Group:          System/Libraries

%description -n %{libname}%{soname}
I/Q balancing for GNU Radio

%package -n %{name}-grc
Summary:        GRC blocks for gr-iqbal
Group:          Productivity/Hamradio/Other
Requires:       %{libname}%{soname} = %{version}
# GRC yaml files were in the library package previously
Conflicts:      libgnuradio-iqbalance0_37_2git
BuildArch:      noarch

%description -n %{name}-grc
GNU Radio Companion (GRC) definitions for the
gr-iqbal I/Q balancing block.

%package -n python3-gr-iqbal
Summary:        Python bindings for gr-iqbal
Group:          Development/Libraries/Python
Requires:       %{libname}%{soname} = %{version}

%description -n python3-gr-iqbal
The Python Bindings for gr-iqbal.

%package -n %{libname}-devel
Summary:        Development files for gr-iqbal
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{soname} = %{version}
Conflicts:      libgnuradio-iqbalance <= 0.37.2+git.20151121

%description -n %{libname}-devel
Library headers for gr-iqbal, I/Q balancing for GNU Radio

%package devel-doc
Summary:        Documentation for gr-iqbal
Group:          Documentation/HTML
Recommends:     libgnuradio-iqbalance-devel = %{version}
BuildArch:      noarch
Obsoletes:      %{name}-doc

%description devel-doc
Documentation for gr-iqbal module for GNU Radio.

%prep
%setup -q -n %{name}

%build
%cmake \
  -Wno-dev
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}/%{_datadir}/doc/gr-iqbalance %{buildroot}%{_docdir}/

%fdupes %{buildroot}%{python3_sitearch}

%post -n %{libname}%{soname} -p /sbin/ldconfig
%postun -n %{libname}%{soname} -p /sbin/ldconfig

%files -n %{libname}%{soname}
%doc AUTHORS
%license COPYING
%{_libdir}/%{libname}.so.*

%files -n %{name}-grc
%{_datadir}/gnuradio

%files -n python3-gr-iqbal
%{python3_sitearch}/gnuradio/iqbalance

%files -n %{libname}-devel
%{_includedir}/gnuradio/iqbalance
%{_libdir}/%{libname}.so
%{_libdir}/cmake/gnuradio/gnuradio-iqbalance*

%files devel-doc
%dir %{_docdir}/gr-iqbalance
%{_docdir}/gr-iqbalance/html
%{_docdir}/gr-iqbalance/xml

%changelog
