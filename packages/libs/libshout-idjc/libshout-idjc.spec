#
# spec file for package libshout-idjc
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

%define libname libshout-idjc3
%define inner_version 2.4.6
Name:           libshout-idjc
Version:        2.4.6.r2
Release:        0
Summary:        Modified version of libshout for Internet DJ Console
License:        LGPL-2.0-only
URL:            https://idjc.sourceforge.net
#Git-Web:	https://sourceforge.net/p/idjc/libshoutidjc/code/ci/master/tree/
#Git-Clone:	https://git.code.sf.net/p/idjc/libshoutidjc/code
Source:         http://downloads.sf.net/libshoutidjc.idjc.p/%{name}-2.4.6-r2.tar.gz
BuildRequires:  c_compiler
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(libssl)

%description
Modified version of libshout for IDJC.

%package -n %{libname}
Summary:        Modified version of libshout for Internet DJ Console

%description -n %{libname}
Modified version of libshout for Internet DJ Console (IDJC).
libshout-idjc supports the transfer of AAC, AAC+ streams
and MPEG ADTS.

%package devel
Summary:        Headers for Industrial I/O library -- development files
Requires:       %{name} = %{version}-%{release}

%description devel
Modified version of libshout

This sub-package contains the development files.

%prep
%autosetup -p1 -n %{name}-%{inner_version}

%build
%configure --disable-static --with-openssl
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{libname}

%files
%license COPYING
%{_bindir}/shoutidjc
%dir %{_libdir}/ckport
%dir %{_libdir}/ckport/db
%{_libdir}/ckport/db/libshout-idjc.ckport

%files -n %{libname}
%{_libdir}/libshout-idjc.so.*

%files devel
%{_libdir}/libshout-idjc.so
%{_libdir}/pkgconfig/shout-idjc.pc
%dir %{_includedir}/shoutidjc
%{_includedir}/shoutidjc/shout.h
%{_mandir}/man1/shoutidjc.1%{?ext_man}
%dir %{_datadir}/doc/libshout-idjc
%{_datadir}/doc/libshout-idjc/*

%changelog
