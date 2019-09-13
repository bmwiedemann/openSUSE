#
# spec file for package libosmo-dsp
#
# Copyright (c) 2017 Walter Fey DL8FCL
#
# This file is under MIT license

%define libname libosmodsp0
Name:           libosmo-dsp
Version:        0.4.0
Release:        0
Summary:        SDR DSP primitives
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
A library with SDR DSP primitives

%package -n %{libname}
Summary:        SDR DSP primitives
Group:          System/Libraries

%description -n %{libname}
A library with SDR DSP primitives

%package devel
Summary:        SDR DSP primitives
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
A library with SDR DSP primitives headers

%package doc
Summary:        SDR DSP primitives - Documentation
Group:          Documentation/HTML
Requires:       %{libname} = %{version}
BuildArch:      noarch

%description doc
A library with SDR DSP primitives headers - Documentation

%prep
%setup -q
%patch0 -p1

%build
echo "%version" >.tarball-version
autoreconf --force --install
%configure --disable-static --includedir="%{_includedir}/%{name}"
make %{?_smp_mflags}

%install
%make_install
rm -f "%{buildroot}/%{_libdir}"/*.la
%fdupes -s %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/libosmodsp.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libosmodsp.so
%{_includedir}/%name/
%{_libdir}/pkgconfig/libosmodsp.pc

%files doc
%defattr(-,root,root)
%doc %{_datadir}/doc/libosmodsp
%exclude %{_datadir}/doc/libosmodsp/html/*.log

%changelog
