#
# spec file for package librtas
#
# Copyright (c) 2025 SUSE LLC
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


%define sover 2
Name:           librtas
Version:        2.0.6
Release:        0
Summary:        Libraries to provide access to RTAS calls and RTAS events
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://github.com/ibm-power-utilities/librtas
Source0:        https://github.com/ibm-power-utilities/librtas/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        activate-firmware-regress
Source3:        vpdupdate-regress
Patch0:         librtas.fix_doc_path.patch
Patch7:         0001-librtas-Move-platform-dump-rtas-call-code-to-separat.patch
Patch8:         0002-librtas-platform-dump-prefer-dev-papr-platform-dump-.patch
Patch9:         0003-librtas-move-get-set-indices-RTAS-calls-code-to-sepa.patch
Patch10:        0004-librtas-Add-kernel-uapi-header-papr-indices.h.patch
Patch11:        0005-librtas-Use-dev-papr-indices-when-available-for-ibm-.patch
Patch12:        0006-librtas-Use-dev-papr-indices-when-available-for-get-.patch
Patch13:        0007-librtas-Use-dev-papr-indices-when-available-for-set-.patch
Patch14:        0008-librtas-Move-physical-attestation-rtas-call-code-to-.patch
Patch15:        0009-librtas-Use-kernel-interface-when-available-for-ibm-.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
ExclusiveArch:  ppc ppc64 ppc64le

%description
The librtas shared library provides userspace with an interface through
which certain RTAS calls can be made.  The library uses either of the
RTAS User Module or the RTAS system call to direct the kernel in making
these calls.

The librtasevent shared library provides users with a set of
definitions and common routines useful in parsing and dumping the
contents of RTAS events.

%package        devel
Summary:        Devel librtas files
Group:          Development/Libraries/C and C++
BuildRequires:  pkgconfig
Requires:       %{name}%{sover} = %{version}

%description devel
This package provides devel files of librtas

%package        devel-static
Summary:        Static librtas files
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel-static
This package provides devel files of librtas

%package     -n %{name}%{sover}
Summary:        Libraries to provide access to RTAS calls and RTAS events
Group:          System/Libraries

%description -n %{name}%{sover}
The librtas shared library provides userspace with an interface through
which certain RTAS calls can be made.  The library uses either of the
RTAS User Module or the RTAS system call to direct the kernel in making
these calls.

The librtasevent shared library provides users with a set of
definitions and common routines useful in parsing and dumping the
contents of RTAS events.

%prep
%autosetup -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
./autogen.sh
%configure
make -O V=1 VERBOSE=1 CFLAGS="%{optflags} -fPIC -g -I $PWD/librtasevent_src" LIB_DIR="%{_libdir}" %{?_smp_mflags}

%install
rm -rf doc/*/latex
make install DESTDIR=%{buildroot} LIB_DIR="%{_libdir}"
# documents are in -doc subpackage
rm -rf %{buildroot}%{_docdir}
/sbin/ldconfig -n %{buildroot}%{_libdir}
chmod -x %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f -name "*.la" -delete -print
install -v -m 755 -D -t %{buildroot}%{_docdir}/%{name} %{SOURCE2} %{SOURCE3}

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING.LESSER
%doc Changelog README
%{_libdir}/lib*.so.*

%files devel
%license COPYING.LESSER
%{_docdir}/%{name}
%{_libdir}/librtasevent.so
%{_libdir}/librtas.so
%{_includedir}/librtas.h
%{_includedir}/librtasevent.h
%{_includedir}/librtasevent_v4.h
%{_includedir}/librtasevent_v6.h

%files devel-static
%license COPYING.LESSER
%{_libdir}/librtas.a
%{_libdir}/librtasevent.a

%changelog
