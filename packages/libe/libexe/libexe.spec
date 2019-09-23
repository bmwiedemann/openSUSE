#
# spec file for package libexe
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname	libexe1
%define timestamp 20181128
Name:           libexe
Version:        0~%{timestamp}
Release:        0
Summary:        Library to access the executable (EXE) format
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libexe/wiki
Source:         https://github.com/libyal/libexe/releases/download/%timestamp/%{name}-experimental-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libbfio)
BuildRequires:  pkgconfig(libcdata)
BuildRequires:  pkgconfig(libcerror)
BuildRequires:  pkgconfig(libcfile)
BuildRequires:  pkgconfig(libclocale)
BuildRequires:  pkgconfig(libcnotify)
BuildRequires:  pkgconfig(libcpath)
BuildRequires:  pkgconfig(libcsplit)
BuildRequires:  pkgconfig(libcstring)
BuildRequires:  pkgconfig(libcsystem)
BuildRequires:  pkgconfig(libcthreads)
BuildRequires:  pkgconfig(libfcache)
BuildRequires:  pkgconfig(libfdata)
BuildRequires:  pkgconfig(libfdatetime)
BuildRequires:  pkgconfig(libuna)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libexe is a library and related tools to access the executable (EXE) format.

At the moment the goal of this project is to provide functionality to parse EXE (PE/COFF) and the resources stored in them using libwrc. This functionality is used in libevt and libevx to parse EventLog messages from PE/COFF message files.

Part of the libyal family of libraries.

%package -n %{lname}
Summary:        Library to access the executable (EXE) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
libexe is a library and related tools to access the executable (EXE) format.

At the moment the goal of this project is to provide functionality to parse EXE (PE/COFF) and the resources stored in them using libwrc. This functionality is used in libevt and libevx to parse EventLog messages from PE/COFF message files.

Part of the libyal family of libraries.

%package tools
Summary:        Tools to access Microsoft executable (EXE) format files
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %lname = %version

%description tools
Tools to access Microsoft executable (EXE) format files including PE/COFF formats.

%package devel
Summary:        Development files for libexe
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide Microsoft EXE file support for the libyal family of libraries.  libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libexe.

%package -n python-%name
Summary:        Python bindings for libexe
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       python

%description -n python-%name
Python bindings for libexe.  Libexe is a part of the libyal family of libraries.

%prep
%setup -q -n libexe-%{timestamp}

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
%doc AUTHORS ChangeLog
%license COPYING 
%{_libdir}/libexe.so.*

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%_bindir/exeinfo
%_mandir/man1/exeinfo.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING 
%{_includedir}/libexe.h
%{_includedir}/libexe/
%{_libdir}/libexe.so
%{_libdir}/pkgconfig/libexe.pc
%{_mandir}/man3/libexe.3*

%files -n python-%name
%defattr(-,root,root)
%python_sitearch/pyexe.so

%changelog
