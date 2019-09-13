#
# spec file for package a52dec
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


%define major     0
%define lib       liba52
%define libname   %{lib}-%{major}
%define mandir    %{_mandir}
Name:           a52dec
Version:        0.7.5+svn613
Release:        0
Summary:        ATSC A/52 stream decoder library
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://liba52.sourceforge.net/
Source:         %{name}-%{version}.tar.gz
Source2:        baselibs.conf
Patch:          altivec.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires:       %{libname} = %{version}
Provides:       a52 = %{version}
Obsoletes:      a52 < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
liba52 is a library for decoding ATSC A/52 streams.

%package -n %{libname}
Summary:        ATSC A/52 stream decoder library
Group:          System/Libraries
Provides:       %{lib} = %{version}
Obsoletes:      %{lib} < %{version}
Provides:       liba52dec0 = %{version}
Obsoletes:      liba52dec0 < %{version}

%description -n %{libname}
liba52 is a library for decoding ATSC A/52 streams.
Shared library part of a52dec.

%package -n %{lib}-devel
Summary:        Header files for the a52dec library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Provides:       a52dec-devel = %{version}
Obsoletes:      a52dec-devel < %{version}
Provides:       liba52dec-devel = %{version}
Obsoletes:      liba52dec-devel < %{version}

%description -n %{lib}-devel
Header files and static library for the a52dec library.
Install this package if you want to compile programs using the library.

%prep
%setup -q
%patch -p1

%build
autoreconf -fi
%configure --disable-static --enable-shared
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README ChangeLog AUTHORS HISTORY NEWS TODO COPYING
%{_bindir}/*
%{mandir}/man1/*

%files -n %{libname}
%defattr(0644,root,root)
%{_libdir}/*.so.*

%files -n %{lib}-devel
%defattr(-,root,root)
%{_includedir}/a52dec/
%{_libdir}/*.so
%{_libdir}/pkgconfig/liba52.pc

%changelog
