#
# spec file for package libcsplit
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


Name:           libcsplit
%define lname	libcsplit1
%define timestamp 20190102
Version:        0~%timestamp
Release:        0
Summary:        Library for cross-platform C split string functions
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libcsplit/wiki
Source:         https://github.com/libyal/libcsplit/releases/download/%timestamp/%{name}-beta-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20130904
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library for cross-platform C split string functions.

This package is part of the libyal library collection and is used by other libraries in the collection

%package -n %lname
Summary:        Library for cross-platform C split string functions
Group:          System/Libraries

%description -n %lname
Library for cross-platform C split string functions.

Part of the libyal family of libraries.

Also see:

    libcdata; generic data functions
    libcdatetime; date and time functions
    libcerror; error functions
    libclocale; locale functions
    libcnotify; notification functions
    libcfile; file functions
    libcpath; path functions
    libcthreads; threads functions 

%package devel
Summary:        Development files for libcsplit, a cross-platform C split string library
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
A library for cross-platform C split string functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcsplit.

%prep
%setup -qn libcsplit-%timestamp

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
%{_libdir}/libcsplit.so.1*

%files devel
%defattr(-,root,root)
%{_includedir}/libcsplit*
%{_libdir}/libcsplit.so
%{_libdir}/pkgconfig/libcsplit.pc
%{_mandir}/man3/libcsplit.3*

%changelog
