#
# spec file for package libmatroska
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 7
Name:           libmatroska
Version:        1.7.1
Release:        0
Summary:        Library to Deal with Matroska Files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.matroska.org/
#Git-Clone:	git://github.com/Matroska-Org/libmatroska
#Git-Web:	https://github.com/Matroska-Org/libmatroska
Source0:        https://dl.matroska.org/downloads/libmatroska/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
Source99:       %{name}.changes
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libebml) >= 1.4.4

%description
Libmatroska is a C++ library to parse Matroska files (.mkv and .mka).
It depends on libebml to work. You only need this package to compile
your own applications.

%package -n libmatroska%{sover}
Summary:        Library to Deal with Matroska Files
Group:          System/Libraries

%description -n libmatroska%{sover}
Libmatroska is a C++ library to parse Matroska files (.mkv and .mka).
It depends on libebml to work. You only need this package to compile
your own applications.

%package devel
Summary:        Library to Deal with Matroska Files
Group:          Development/Libraries/C and C++
Requires:       libmatroska%{sover} = %{version}
Requires:       pkgconfig(libebml) >= 1.4.2

%description devel
Libmatroska is a C++ library to parse Matroska files (.mkv and .mka).
It depends on libebml to work. You only need this package to compile
your own applications.

%prep
%autosetup

%build
# mkvmerge-9.3.0 built against libmatroska-1.4.5 running against
# libmatroska-1.4.4: symbol lookup error: mkvmerge: undefined symbol:
# _ZN11libmatroska14KaxVideoColour10ClassInfosE
# Force some additional versioning, since upstream did not track the ABI
# changes.
# Tag with the version of the most recent !!incompatible!! change.
echo "V_1.7.0 { global: *; };" > libmatroska.sym
export LDFLAGS="-Wl,--version-script=$PWD/libmatroska.sym"
%cmake \
	-DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS -Wl,--as-needed -Wl,--no-undefined -Wl,-z,now"
%cmake_build

%install
%cmake_install

%post -n libmatroska%{sover} -p /sbin/ldconfig
%postun -n libmatroska%{sover} -p /sbin/ldconfig

%files -n libmatroska%{sover}
%{_libdir}/libmatroska.so.%{sover}*

%files devel
%{_libdir}/libmatroska.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/Matroska
%{_includedir}/matroska

%changelog
