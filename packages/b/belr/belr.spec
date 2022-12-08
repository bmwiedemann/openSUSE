#
# spec file for package belr
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


%define soname  libbelr
%define sover   1
Name:           belr
Version:        5.1.72
Release:        0
Summary:        Language recognition library
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://linphone.org/
Source:         https://gitlab.linphone.org/BC/public/belr/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE belr-fix-pkgconfig.patch sor.alexei@meowr.ru -- Install belr.pc.
Patch0:         belr-fix-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libudev-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bctoolbox) >= 5.0.0

%description
Belr parses input formatted according to a language defined by an
ABNF grammar, such as the protocols standardised at IETF.

%package -n %{soname}%{sover}
Summary:        Language recognition library
Group:          Development/Tools/Other

%description -n %{soname}%{sover}
Belr parses input formatted according to a language defined by an
ABNF grammar, such as the protocols standardised at IETF.

%package devel
Summary:        Headers and libraries for the belr library
Group:          Development/Tools/Other
Requires:       %{soname}%{sover} = %{version}

%description devel
Belr parses input formatted according to a language defined by an
ABNF grammar, such as the protocols standardised at IETF.

This package contains header files and development libraries needed
to develop applications using the belr library.

%prep
%autosetup -p1

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
%license LICENSE.txt
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_bindir}/%{name}*
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_libdir}/cmake/%{name}/
%{_datadir}/%{name}/
%{_datadir}/%{name}-tester/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
