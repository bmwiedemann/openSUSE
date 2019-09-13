#
# spec file for package libcfile
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libcfile
%define lname	libcfile1
%define timestamp 20190314
Version:        0~%timestamp
Release:        0
Summary:        Library for cross-platform C file functions
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libcfile/wiki
Source:         https://github.com/libyal/libcfile/releases/download/%timestamp/%{name}-alpha-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20130103
BuildRequires:  pkgconfig(libcstring) >= 20150101
# This can cause a build loop.  The internal version should be used.
#BuildRequires:  pkgconfig(libuna) >= 20120425
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library and devel package for cross-platform C file functions.

%package -n %lname
Summary:        Library for cross-platform C file functions
Group:          System/Libraries

%description -n %lname
A library for cross-platform C file functions. Part of the libyal library collection.

%package devel
Summary:        Development files for libcfile, a cross-platform C file library
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
A library for cross-platform C file functions.
 
This subpackage contains libraries and header files for developing
applications that want to make use of libcfile.

%prep
%setup -qn libcfile-%timestamp

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
%{_libdir}/libcfile.so.1*

%files devel
%defattr(-,root,root)
%{_includedir}/libcfile*
%{_libdir}/libcfile.so
%{_libdir}/pkgconfig/libcfile.pc
%{_mandir}/man3/libcfile.3*

%changelog
