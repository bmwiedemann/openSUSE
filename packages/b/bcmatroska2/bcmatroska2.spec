#
# spec file for package bcmatroska2
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


%define sover   0
Name:           bcmatroska2
Version:        0.23
Release:        0
Summary:        C Library to Deal with Matroska Files
License:        BSD-3-Clause AND Zlib AND GPL-2.0-or-later
URL:            https://linphone.org/
Source:         https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE bcmatroska2-include-subdir.patch sor.alexei@meowr.ru -- Resolve a conflict with libebml and libmatroska.
Patch0:         bcmatroska2-include-subdir.patch
BuildRequires:  cmake

%description
Bcmatroska2 is a C library to parse Matroska files (.mkv and .mka).

%package -n lib%{name}-%{sover}
Summary:        C Library to Deal with Matroska Files

%description -n lib%{name}-%{sover}
Bcmatroska2 is a C library to parse Matroska files (.mkv and .mka).

%package devel
Summary:        Development files for bcmatroska2
Requires:       lib%{name}-%{sover} = %{version}

%description devel
This package includes the files necessary for compiling and linking
applications which will use libbcmatroska2.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
  -DENABLE_STATIC=OFF \
  -DENABLE_STRICT=OFF
%cmake_build

%install
%cmake_install

%post -n lib%{name}-%{sover} -p /sbin/ldconfig
%postun -n lib%{name}-%{sover} -p /sbin/ldconfig

%files -n lib%{name}-%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%dir %{_datadir}/bcmatroska2/
%{_datadir}/bcmatroska2/cmake/

%changelog
