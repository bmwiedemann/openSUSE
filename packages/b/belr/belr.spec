#
# spec file for package belr
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


%define soname  libbelr
%define sover   1
Name:           belr
Version:        0.1.3
Release:        0
Summary:        Language recognition library
License:        GPL-3.0-or-later
URL:            https://linphone.org/
Source:         https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE belr-fix-pkgconfig.patch sor.alexei@meowr.ru -- Install belr.pc.
Patch0:         belr-fix-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bctoolbox) >= 0.6.0

%description
Belr parses input formatted according to a language defined by an
ABNF grammar, such as the protocols standardised at IETF.

%package -n %{soname}%{sover}
Summary:        Language recognition library

%description -n %{soname}%{sover}
Belr parses input formatted according to a language defined by an
ABNF grammar, such as the protocols standardised at IETF.

%package devel
Summary:        Headers and libraries for the belr library
Requires:       %{soname}%{sover} = %{version}

%description devel
Belr parses input formatted according to a language defined by an
ABNF grammar, such as the protocols standardised at IETF.

This package contains header files and development libraries needed
to develop applications using the belr library.

%prep
%setup -q -n %{name}-%{version}-0
%autopatch -p1

%build
%cmake \
  -DENABLE_STRICT=OFF \
  -DENABLE_STATIC=OFF
%cmake_build

%install
%cmake_install

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%license COPYING
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%license COPYING
%doc NEWS README.md
%{_bindir}/belr-parse
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_datadir}/Belr/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
