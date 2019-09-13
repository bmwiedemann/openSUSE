#
# spec file for package libhmac
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libhmac
%define lname	libhmac1
%define timestamp 20150104
Version:        0~%timestamp
Release:        0
Summary:        Library to support various HMACs
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libhmac/wiki
Source:         https://github.com/libyal/libhmac/releases/download/%timestamp/%{name}-alpha-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcfile)   >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify)  >= 20130609
BuildRequires:  pkgconfig(libcpath)    >= 20130609
BuildRequires:  pkgconfig(libcsplit)   >= 20130609
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libuna)     >= 20120425
BuildRequires:  pkgconfig(openssl)     >= 1.0
# These packages from factory cause build failures, use the internal version instead
#verified 1/8/2015
#BuildRequires:  pkgconfig(libcerror)  >= 20120425
#BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library and tools to support various Hash-based Message Authentication Codes (HMAC).

%package -n %lname
Summary:        Library to support various HMACs
Group:          System/Libraries

%description -n %lname
A library to support various Hash-based Message Authentication Codes (HMAC).

%package devel
Summary:        Development files for libhmac
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
Development files for libhmac, a library to support various Hash-based Message Authentication Codes (HMAC).

This subpackage contains libraries and header files for developing
applications that want to make use of %{name}.

%package tools
Summary:        Utilities for HMACs
Group:          Productivity/File utilities

%description tools
Use hmacsum to calculate a Hash-based Message Authentication Code (HMAC) of the data in a file.

%prep
%setup -qn libhmac-%timestamp

%build
%configure --disable-static --enable-wide-character-type
make %{?_smp_mflags}

%install
%make_install
rm -f "%{buildroot}/%{_libdir}"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libhmac.so.1*

%files devel
%defattr(-,root,root)
%{_includedir}/libhmac*
%{_libdir}/libhmac.so
%{_libdir}/pkgconfig/libhmac.pc
%{_mandir}/man3/libhmac.3*

%files tools
%defattr(-,root,root)
%{_bindir}/hmacsum
%{_mandir}/man1/hmacsum.1*

%changelog
