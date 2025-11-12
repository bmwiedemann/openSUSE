#
# spec file for package libosmo-dsp
#
# Copyright (c) 2025 SUSE LLC and contributors
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
# Copyright (c) 2017 Walter Fey DL8FCL
#
# This file is under MIT license


%define libname libosmodsp0
Name:           libosmo-dsp
Version:        0.5.0
Release:        0
Summary:        Osmocom DSP utility functions
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://osmocom.org/projects/libosmo-dsp
Source:         %{name}-%{version}.tar.xz
Patch0:         HTML_TIMESTAMP.diff
BuildRequires:  automake >= 1.6
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig
BuildRequires:  texlive-latex
BuildRequires:  pkgconfig(fftw3f) >= 3.2

%description
libosmo-dsp is a C language library for common DSP (Digital
Signal Processing) primitives for SDR (Software Defined Radio).

%package -n %{libname}
Summary:        SDR DSP primitives
Group:          System/Libraries

%description -n %{libname}
libosmo-dsp is a C language library for common DSP (Digital
Signal Processing) primitives for SDR (Software Defined Radio).

%package devel
Summary:        Headers for the Osmocom SDR DSP primitives
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libosmo-dsp is a C language library for common DSP (Digital
Signal Processing) primitives for SDR (Software Defined Radio).
This subpackage contains the header files.

%package doc
Summary:        Documentation for the Osmocom SDR DSP primitives
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
libosmo-dsp is a C language library for common DSP (Digital
Signal Processing) primitives for SDR (Software Defined Radio).
This subpackage contains the API documentation.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf --force --install
%configure --disable-static --includedir="%{_includedir}/%{name}"
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING
%doc AUTHORS
%{_libdir}/libosmodsp.so.*

%files devel
%{_libdir}/libosmodsp.so
%{_includedir}/%name/
%{_libdir}/pkgconfig/libosmodsp.pc

%files doc
%doc %{_datadir}/doc/libosmodsp
%exclude %{_datadir}/doc/libosmodsp/html/*.log

%changelog
