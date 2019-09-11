#
# spec file for package libogg
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _SO_nr 0

Name:           libogg
Version:        1.3.3
Release:        0
Summary:        Ogg Bitstream Library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.vorbis.com/
Source:         http://downloads.xiph.org/releases/ogg/%{name}-%{version}.tar.xz
Source2:        baselibs.conf
Patch1:         lib64.dif
Patch2:         m4.diff
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libogg is a library for manipulating Ogg bitstreams.  It handles both
making Ogg bitstreams and getting packets from Ogg bitstreams.

Ogg is the native bitstream format of libvorbis (Ogg Vorbis audio
codec) and libtheora (Theora video codec).

%package -n libogg%{_SO_nr}
Summary:        Ogg Bitstream Library
Group:          System/Libraries

%description -n libogg%{_SO_nr}
Libogg is a library for manipulating Ogg bitstreams.  It handles both
making Ogg bitstreams and getting packets from Ogg bitstreams.

Ogg is the native bitstream format of libvorbis (Ogg Vorbis audio
codec) and libtheora (Theora video codec).

%package devel
Summary:        Include Files and Libraries for Ogg Development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libogg%{_SO_nr} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libogg.

%prep
%setup -q
%patch2
if [ "%{_lib}" == "lib64" ]; then
%patch1
fi

%build
# Fix optimization level
sed -i s,-O20,-O3,g configure

%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} docdir=%{_docdir}/%{name}-devel install
# remove unneeded files
rm -f %{buildroot}%{_libdir}/*.la

%check
make check

%post -n libogg%{_SO_nr} -p /sbin/ldconfig

%postun -n libogg%{_SO_nr} -p /sbin/ldconfig

%files -n libogg%{_SO_nr}
%defattr(0644,root,root,0755)
%doc AUTHORS CHANGES README.md
%license COPYING
%{_libdir}/libogg.so.%{_SO_nr}*

%files devel
%defattr(0644,root,root,0755)
%{_docdir}/%{name}-devel
%{_includedir}/ogg
%{_libdir}/libogg.so
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/ogg.m4
%{_libdir}/pkgconfig/ogg.pc

%changelog
