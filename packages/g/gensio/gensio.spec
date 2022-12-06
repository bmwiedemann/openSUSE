#
# spec file for package gensio
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020-2022, Martin Hauke <mardnh@gmx.de>
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


%global sover   0
%global sover_cpp 4
%global libname libgensio4
%global libname_cpp libgensiocpp%{sover_cpp}
%if 0%{?suse_version} > 1500
%bcond_without openipmi
%else
%bcond_with    openipmi
%endif
Name:           gensio
Version:        2.6.1
Release:        0
Summary:        Library to abstract stream and packet I/O
# examples/* is licenced under Apache-2.0
License:        Apache-2.0 AND GPL-2.0-only AND LGPL-2.1-only
Group:          Productivity/Networking/Other
URL:            https://github.com/cminyard/gensio
#Git-Clone:     https://github.com/cminyard/gensio.git
Source:         https://github.com/cminyard/gensio/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  lksctp-tools-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(avahi-client)
%if %{with openipmi}
BuildRequires:  pkgconfig(OpenIPMI)
%endif

%description
This is gensio (pronounced gen'-see-oh), a framework for giving a
consistent view of various stream (and packet) I/O types. You
create a gensio object (or a gensio), and you can use that gensio
without having to know too much about what is going on underneath.
You can stack gensio on top of another one to add protocol
funcionality. For instance, you can create a TCP gensio, stack SSL
on top of that, and stack Telnet on top of that. It supports a
number of network I/O and serial ports. gensios that stack on
other gensios are called filters.

%package -n %{libname}
Summary:        Library to abstract stream and packet I/O
Group:          System/Libraries

%description -n %{libname}
This is gensio (pronounced gen'-see-oh), a framework for giving a
consistent view of various stream (and packet) I/O types. You
create a gensio object (or a gensio), and you can use that gensio
without having to know too much about what is going on underneath.
You can stack gensio on top of another one to add protocol
funcionality. For instance, you can create a TCP gensio, stack SSL
on top of that, and stack Telnet on top of that. It supports a
number of network I/O and serial ports. gensios that stack on
other gensios are called filters.

%package -n libgensioosh%{sover}
Summary:        Library to abstract stream and packet I/O
Group:          System/Libraries

%description -n libgensioosh%{sover}
This is gensio (pronounced gen'-see-oh), a framework for giving a
consistent view of various stream (and packet) I/O types - osh support

%package -n libgensiomdns%{sover}
Summary:        Library to abstract stream and packet I/O
Group:          System/Libraries

%description -n libgensiomdns%{sover}
This is gensio (pronounced gen'-see-oh), a framework for giving a
consistent view of various stream (and packet) I/O types - mdns support

%package -n libgensio_python_swig%{sover}
Summary:        Library to abstract stream and packet I/O
Group:          System/Libraries
Provides:       libgensio0:/usr/lib/libgensio_python_swig.so.0.0.0
Obsoletes:      libgensio0 < %{version}

%description -n libgensio_python_swig%{sover}
This is gensio (pronounced gen'-see-oh), a framework for giving a
consistent view of various stream (and packet) I/O types - python support

%package -n %{libname_cpp}
Summary:        Library to abstract stream and packet I/O
Group:          System/Libraries

%description -n %{libname_cpp}
This is gensio (pronounced gen'-see-oh), a framework for giving a
consistent view of various stream (and packet) I/O types. You
create a gensio object (or a gensio), and you can use that gensio
without having to know too much about what is going on underneath.
You can stack gensio on top of another one to add protocol
funcionality. For instance, you can create a TCP gensio, stack SSL
on top of that, and stack Telnet on top of that. It supports a
number of network I/O and serial ports. gensios that stack on
other gensios are called filters.

%package devel
Summary:        Library to abstract stream and packet I/O
Group:          Development/Libraries/C and C++
Requires:       %{libname_cpp} = %{version}
Requires:       %{libname} = %{version}
Requires:       lksctp-tools-devel
Requires:       pkgconfig(avahi-client)
%if %{with openipmi}
Requires:       pkgconfig(OpenIPMI)
%endif

%description devel
This is gensio (pronounced gen'-see-oh), a framework for giving a
consistent view of various stream (and packet) I/O types. You
create a gensio object (or a gensio), and you can use that gensio
without having to know too much about what is going on underneath.
You can stack gensio on top of another one to add protocol
funcionality. For instance, you can create a TCP gensio, stack SSL
on top of that, and stack Telnet on top of that. It supports a
number of network I/O and serial ports. gensios that stack on
other gensios are called filters.

This subpackage contains libraries and header files for developing
applications that want to make use of libgensio.

%package -n python3-gensio
Summary:        Python bindings for libgensio
Group:          System/Libraries

%description -n python3-gensio
Python bindings for libgensio, a library for stream and packet I/O
abscration.

%prep
%setup -q

%build
export CFLAGS="%optflags -fcommon"
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%post -n libgensioosh%{sover} -p /sbin/ldconfig
%postun -n libgensioosh%{sover} -p /sbin/ldconfig
%post -n libgensiomdns%{sover} -p /sbin/ldconfig
%postun -n libgensiomdns%{sover} -p /sbin/ldconfig
%post -n libgensio_python_swig%{sover} -p /sbin/ldconfig
%postun -n libgensio_python_swig%{sover} -p /sbin/ldconfig
%post -n %{libname_cpp} -p /sbin/ldconfig
%postun -n %{libname_cpp} -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB
%doc AUTHORS ChangeLog NEWS README.rst
%{_bindir}/gensiot
%{_bindir}/gmdns
%{_bindir}/greflector
%{_bindir}/gsound
%{_bindir}/gtlssh
%{_bindir}/gtlssh-keygen
%{_bindir}/gtlssync
%{_mandir}/man1/gensiot.1%{?ext_man}
%{_mandir}/man1/gmdns.1%{?ext_man}
%{_mandir}/man1/greflector.1%{?ext_man}
%{_mandir}/man1/gsound.1%{?ext_man}
%{_mandir}/man1/gtlssh-keygen.1%{?ext_man}
%{_mandir}/man1/gtlssh.1%{?ext_man}
%{_mandir}/man1/gtlssync.1%{?ext_man}
%{_mandir}/man5/gensio.5%{?ext_man}
%{_mandir}/man5/sergensio.5%{?ext_man}

%files -n %{libname}
%{_libdir}/libgensio.so.%{sover_cpp}*
%{_libexecdir}/gensio-%{version}

%files -n libgensioosh%{sover}
%{_libdir}/libgensioosh.so.%{sover}*
%{_libdir}/libgensiooshcpp.so.%{sover}*

%files -n libgensiomdns%{sover}
%{_libdir}/libgensiomdns.so.%{sover}*
%{_libdir}/libgensiomdnscpp.so.%{sover}*

%files -n libgensio_python_swig%{sover}
%{_libdir}/libgensio_python_swig.so.%{sover}*

%files -n %{libname_cpp}
%{_libdir}/libgensiocpp.so.%{sover_cpp}*

%files devel
%{_includedir}/gensio/
%{_libdir}/libgensio*.so
%{_libdir}/pkgconfig/libgensio*.pc
%{_mandir}/man3/gensio_*3%{?ext_man}
%{_mandir}/man3/sergensio_*3%{?ext_man}
%{_mandir}/man3/str_to_gensio*.3%{?ext_man}

%files -n python3-gensio
%{python3_sitelib}/*

%changelog
