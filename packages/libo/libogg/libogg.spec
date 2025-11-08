#
# spec file for package libogg
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define _SO_nr 0
Name:           libogg
Version:        1.3.6
Release:        0
Summary:        Ogg Bitstream Library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://xiph.org/vorbis/
Source:         https://downloads.xiph.org/releases/ogg/%{name}-%{version}.tar.xz
Source2:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  xz

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
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n libogg%{_SO_nr}

%files -n libogg%{_SO_nr}
%doc AUTHORS CHANGES README.md
%license COPYING
%{_libdir}/libogg.so.%{_SO_nr}*

%files devel
%{_docdir}/%{name}
%{_includedir}/ogg
%{_libdir}/libogg.so
%{_libdir}/cmake/Ogg
%{_libdir}/pkgconfig/ogg.pc

%changelog
