#
# spec file for package gensio
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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
%global libname libgensio%{sover}
%if 0%{?suse_version} > 1500
%bcond_without openipmi
%else
%bcond_with    openipmi
%endif
Name:           gensio
Version:        2.1.7
Release:        0
Summary:        Library to abstract stream and packet I/O
# examples/* is licenced under Apache-2.0
License:        GPL-2.0-only AND LGPL-2.1-only AND Apache-2.0
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

%package devel
Summary:        Library to abstract stream and packet I/O
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

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

%files
%license COPYING COPYING.LIB
%doc AUTHORS ChangeLog NEWS README.rst
%{_bindir}/gensiot
%{_bindir}/gtlssh
%{_bindir}/gtlssh-keygen
%{_bindir}/gtlssync
%{_mandir}/man1/gensiot.1%{?ext_man}
%{_mandir}/man1/gtlssh-keygen.1%{?ext_man}
%{_mandir}/man1/gtlssh.1%{?ext_man}
%{_mandir}/man1/gtlssync.1%{?ext_man}
%{_mandir}/man5/gensio.5%{?ext_man}
%{_mandir}/man5//sergensio.5%{?ext_man}

%files -n %{libname}
%{_libdir}/libgensio.so.%{sover}*

%files devel
%dir %{_includedir}/gensio
%{_includedir}/gensio/*.h
%{_libdir}/libgensio.so
%{_libdir}/pkgconfig/libgensio.pc
%{_mandir}/man3/gensio_*3%{?ext_man}
%{_mandir}/man3/sergensio_*3%{?ext_man}
%{_mandir}/man3/str_to_gensio*.3%{?ext_man}

%files -n python3-gensio
%{python3_sitelib}/*

%changelog
