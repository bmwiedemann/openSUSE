#
# spec file for package librtas
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


%define sover 2

Name:           librtas
Version:        2.0.2
Release:        0
Summary:        Libraries to provide access to RTAS calls and RTAS events
License:        LGPL-2.1+
Group:          System/Libraries
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  ppc ppc64 ppc64le
Url:            https://github.com/ibm-power-utilities/librtas
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Source0:        https://github.com/ibm-power-utilities/librtas/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         librtas.fix_doc_path.patch

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
BuildRequires:  pkg-config
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
%setup -q
%patch0 -p1

%build
./autogen.sh
%configure
make CFLAGS="%optflags -fPIC -g -I $PWD/librtasevent_src" LIB_DIR="%{_libdir}" %{?_smp_mflags}

%install
rm -rf doc/*/latex
make install DESTDIR=%buildroot LIB_DIR="%{_libdir}"
# documents are in -doc subpackage
rm -rf %buildroot/%_docdir
/sbin/ldconfig -n %buildroot%{_libdir}
chmod -x %{buildroot}%{_libdir}/*.a
rm %{buildroot}/%{_libdir}/*.la

%post -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-, root, root)
%doc COPYING.LESSER Changelog README
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root)
%doc COPYING.LESSER
%{_libdir}/librtasevent.so
%{_libdir}/librtas.so
%{_includedir}/librtas.h
%{_includedir}/librtasevent.h
%{_includedir}/librtasevent_v4.h
%{_includedir}/librtasevent_v6.h
%{_libdir}/pkgconfig/*.pc

%files devel-static
%defattr(-,root,root)
%doc COPYING.LESSER
%{_libdir}/librtas.a
%{_libdir}/librtasevent.a

%changelog
