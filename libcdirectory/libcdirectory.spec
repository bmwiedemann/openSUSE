#
# spec file for package libcdirectory
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


%define lname	libcdirectory1
%define timestamp 20170104
Name:           libcdirectory
Version:        0~%{timestamp}
Release:        0
Summary:        Library for Windows NT data types
License:        LGPL-3.0+ and GFDL-1.3+
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libcdirectory/wiki
Source:         https://github.com/libyal/libcdirectory/releases/download/%timestamp/%{name}-experimental-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libcerror) >= 20150101
BuildRequires:  pkgconfig(libclocale) >= 20150101
BuildRequires:  pkgconfig(libcstring) >= 20150101
BuildRequires:  pkgconfig(libuna) >= 20150101
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package -n %{lname}
Summary:        Library for Windows NT data types
License:        LGPL-3.0+
Group:          System/Libraries

%description -n %{lname}
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package devel
Summary:        Development files for libcdirectory
License:        LGPL-3.0+ and GFDL-1.3+
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide Windows NT data type support for the libyal family of libraries.  libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libcdirectory.

%prep
%setup -q -n libcdirectory-%{timestamp}

%build
%configure --disable-static --enable-wide-character-type --enable-python
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libcdirectory.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING README ChangeLog
%{_includedir}/libcdirectory.h
%{_includedir}/libcdirectory/
%{_libdir}/libcdirectory.so
%{_libdir}/pkgconfig/libcdirectory.pc
%{_mandir}/man3/libcdirectory.3*

%changelog
