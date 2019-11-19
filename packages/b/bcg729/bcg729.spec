#
# spec file for package bcg729
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
Name:           bcg729
Version:        1.0.4
Release:        0
Summary:        Encoder and decoder of the ITU G.729 Annex A/B speech codec
License:        GPL-2.0-or-later
URL:            https://www.linphone.org/technical-corner/bcg729/overview
Source:         https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE bcg729-fix-pkgconfig.patch sor.alexei@meowr.ru -- Install libbcg729.pc.
Patch0:         bcg729-fix-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig

%description
Bcg729 is an implementation of both encoder and decoder of the ITU
G.729 Annex A/B speech codec. It supports concurrent channels
encoding/decoding for multi call application such as conferencing.

%package -n lib%{name}-%{sover}
Summary:        Encoder and decoder of the ITU G.729 Annex A/B speech codec

%description -n lib%{name}-%{sover}
Bcg729 is an implementation of both encoder and decoder of the ITU
G.729 Annex A/B speech codec. It supports concurrent channels
encoding/decoding for multi call application such as conferencing.

%package devel
Summary:        Development files for libbcg729
Requires:       lib%{name}-%{sover} = %{version}

%description devel
This package includes the files necessary for compiling and linking
application which will use libbcg729.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
  -DENABLE_TESTS=ON   \
  -DENABLE_STATIC=OFF \
  -DENABLE_STRICT=OFF
%cmake_build

%install
%cmake_install

%post -n lib%{name}-%{sover} -p /sbin/ldconfig
%postun -n lib%{name}-%{sover} -p /sbin/ldconfig

%files -n lib%{name}-%{sover}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_datadir}/Bcg729/
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
