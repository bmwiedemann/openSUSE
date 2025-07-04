#
# spec file for package soapy-sdr
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017-2025, Martin Hauke <mardnh@gmx.de>
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


%define sover 0_8-3
Name:           soapy-sdr
Version:        0.8.1+git20250223.6e99da1
Release:        0
Summary:        Vendor and platform neutral SDR support library
License:        BSL-1.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/pothosware/SoapySDR.git
Source:         %{name}-%{version}.tar.xz
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  pkgconfig(python3)

%description
A vendor neutral and platform independent SDR support library.

%package -n libSoapySDR%{sover}
Summary:        Vendor and platform neutral SDR support library
Group:          System/Libraries
Obsoletes:      libSoapySDR0_8

%description -n libSoapySDR%{sover}
A vendor neutral and platform independent SDR support library.

%package -n python3-SoapySDR
Summary:        Python bindings for SoapySDR
Group:          Development/Languages/Python
Provides:       python-%{name}
Recommends:     python-numpy

%description -n python3-SoapySDR
Python Bindings for SoapySDR.
A vendor neutral and platform independent SDR support library.

%package devel
Summary:        Development files for the SoapySDR library
Group:          Development/Libraries/C and C++
Requires:       libSoapySDR%{sover} = %{version}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of libSoapySDR.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake \
  -DSOAPY_SDR_VERSION=%{version} \
  -DBUILD_PYTHON3=ON
%cmake_build

%install
%cmake_install

%check
# path needs to be exported otherwise unit tests will fail
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
%ctest

%ldconfig_scriptlets -n libSoapySDR%{sover}

%files
%{_bindir}/SoapySDRUtil

%files -n libSoapySDR%{sover}
%doc Changelog.txt README.md
%license LICENSE_1_0.txt
%{_libdir}/libSoapySDR.so.*

%files -n python3-SoapySDR
%{python3_sitearch}/SoapySDR.py
%{python3_sitearch}/*SoapySDR.so

%files devel
%doc docs/
%dir %{_includedir}/SoapySDR
%{_includedir}/SoapySDR/*.h
%{_includedir}/SoapySDR/*.hpp
%{_libdir}/libSoapySDR.so
%{_libdir}/pkgconfig/SoapySDR.pc
%dir %{_datadir}/cmake/SoapySDR
%{_datadir}/cmake/SoapySDR/SoapySDRConfig.cmake
%{_datadir}/cmake/SoapySDR/SoapySDRConfigVersion.cmake
%{_datadir}/cmake/SoapySDR/SoapySDRUtil.cmake
%{_datadir}/cmake/SoapySDR/SoapySDRExport-relwithdebinfo.cmake
%{_datadir}/cmake/SoapySDR/SoapySDRExport.cmake
%{_mandir}/man1/SoapySDRUtil.1%{ext_man}

%changelog
