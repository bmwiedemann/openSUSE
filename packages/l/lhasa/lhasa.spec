#
# spec file for package lhasa
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           lhasa
%define lname	liblhasa0
Version:        0.3.1
Release:        0
Summary:        Program to unpack LHARC archives
License:        ISC
Group:          Productivity/Archiving/Compression
Url:            http://fragglet.github.com/lhasa/

#Git-Clone:	git://github.com/fragglet/lhasa
Source:         http://www.soulsphere.org/projects/lhasa/lhasa-%version.tar.gz
Source2:        http://www.soulsphere.org/projects/lhasa/lhasa-%version.tar.gz.asc
Source3:        %name.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkg-config
BuildRequires:  xz

%description
Lhasa is a replacement for the Unix LHA tool, for decompressing
".lzh" (LHA/LHarc) and ".lzs" (LArc) archives.

%package -n %lname
Summary:        A decompression library for the LHARC data format
Group:          System/Libraries

%description -n %lname
liblhasa is the backend to the Lhasa tool, offering decompressing for
".lzh" (LHA/LHarc) and ".lzs" (LArc) archives.

%package devel
Summary:        Development files for liblhasa, a LHARC decompression library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
liblhasa is the backend to the Lhasa tool, offering decompressing for
".lzh" (LHA/LHarc) and ".lzs" (LArc) archives.

This package contains the development headers for the library found 
in %lname.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags};

%install
b="%buildroot";
%make_install
rm -f "$b/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%_bindir/lha
%_mandir/man1/lha.1*

%files -n %lname
%defattr(-,root,root)
%_libdir/liblhasa.so.0*

%files devel
%defattr(-,root,root)
%_includedir/liblhasa-1.0
%_libdir/liblhasa.so
%_libdir/pkgconfig/liblhasa.pc

%changelog
