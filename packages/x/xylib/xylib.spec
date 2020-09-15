#
# spec file for package xylib
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


%define somajor 4
Name:           xylib
Version:        1.5
Release:        0
Summary:        Library for reading x-y data from several file formats
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://xylib.sourceforge.net/
Source:         https://github.com/wojdyr/xylib/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Patch0:         0001-BOOST_BIG_ENDIAN-was-deprecated-and-replaced-by-BOOS.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  wxWidgets-devel >= 3
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)

%description
C++ library for reading files that contain x-y data from powder diffraction,
spectroscopy or other experimental methods. The supported formats include:
VAMAS, pdCIF, Bruker UXD and RAW, Philips UDF and RD, Rigaku DAT,
Sietronics CPI, DBWS/DMPLOT, Koalariet XDD and others.

%package -n     libxy%{somajor}
Summary:        Library for reading x-y data from several file formats
Group:          System/Libraries
Obsoletes:      xylib%{somajor}

%description -n libxy%{somajor}
C++ library for reading files that contain x-y data from powder diffraction,
spectroscopy or other experimental methods. The supported formats include:
VAMAS, pdCIF, Bruker UXD and RAW, Philips UDF and RD, Rigaku DAT,
Sietronics CPI, DBWS/DMPLOT, Koalariet XDD and others.

%package        devel
Summary:        Development files for xylib
Group:          Development/Libraries/C and C++
Requires:       libxy%{somajor} = %{version}

%description    devel
This package contains libraries and header files for developing
applications that use xylib.

%package -n     xyconv
Summary:        Command-line converter of files in formats supported by xylib
Group:          Productivity/Scientific/Other

%description -n xyconv
Command-line converter of files in formats supported by xylib:
- plain text, delimiter-separated values (e.g. CSV)
- Crystallographic Information File for Powder Diffraction (pdCIF)
- Siemens/Bruker UXD
- Siemens/Bruker RAW ver. 1/2/3
- Philips UDF
- Philips RD (raw scan) V3
- Rigaku DAT
- Sietronics Sieray CPI
- DBWS/DMPLOT data file
- Canberra CNF (from Genie-2000 software; aka CAM format)
- Canberra AccuSpec MCA
- XFIT/Koalariet XDD
- RIET7/LHPM/CSRIET/ILL\_D1A5/PSI\_DMC DAT
- Vamas ISO14976
  *(only experiment modes: SEM or MAPSV or MAPSVDP are supported;
  only REGULAR scan_mode is supported)*
- Princeton Instruments WinSpec SPE
  *(only 1-D data is supported)*
- χPLOT CHI_
- Ron Unwin's Spectra XPS format (VGX-900 compatible)

%package -n     xyconvert
Summary:        GUI converter of files in formats supported by xylib
Group:          Productivity/Scientific/Other

%description -n xyconvert
GUI converter of files in formats supported by xylib:
- plain text, delimiter-separated values (e.g. CSV)
- Crystallographic Information File for Powder Diffraction (pdCIF)
- Siemens/Bruker UXD
- Siemens/Bruker RAW ver. 1/2/3
- Philips UDF
- Philips RD (raw scan) V3
- Rigaku DAT
- Sietronics Sieray CPI
- DBWS/DMPLOT data file
- Canberra CNF (from Genie-2000 software; aka CAM format)
- Canberra AccuSpec MCA
- XFIT/Koalariet XDD
- RIET7/LHPM/CSRIET/ILL\_D1A5/PSI\_DMC DAT
- Vamas ISO14976
  *(only experiment modes: SEM or MAPSV or MAPSVDP are supported;
  only REGULAR scan_mode is supported)*
- Princeton Instruments WinSpec SPE
  *(only 1-D data is supported)*
- χPLOT CHI_
- Ron Unwin's Spectra XPS format (VGX-900 compatible)

%prep
%autosetup -p1

%build
autoreconf -f
%configure \
  --disable-static

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libxy%{somajor} -p /sbin/ldconfig
%postun -n libxy%{somajor} -p /sbin/ldconfig

%files -n libxy%{somajor}
%license COPYING
%doc README.rst
%{_libdir}/libxy.so.%{somajor}*

%files devel
%doc sample-urls
%{_includedir}/*
%{_libdir}/libxy.so

%files -n xyconv
%{_bindir}/xyconv
%{_mandir}/man1/xyconv.1%{?ext_man}

%files -n xyconvert
%{_bindir}/xyconvert

%changelog
