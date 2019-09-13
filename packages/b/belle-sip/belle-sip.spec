#
# spec file for package belle-sip
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Mariusz Fik <fisiu@opensuse.org>.
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


%define soname  libbellesip
%define sover   0
Name:           belle-sip
Version:        1.6.3
Release:        0
Summary:        C object-oriented SIP Stack
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://linphone.org/technical-corner/belle-sip/overview
Source:         https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
Source1:        http://antlr3.org/download/antlr-3.4-complete.jar
Source2:        baselibs.conf
# PATCH-FIX-OPENSUSE belle-sip-fix-pkgconfig.patch sor.alexei@meowr.ru -- Fix up pkgconfig.
Patch0:         belle-sip-fix-pkgconfig.patch
# PATCH-FIX-OPENSUSE belle-sip-fix-dns-build.patch -- Pass -Wno-override-init to the compiler while building dns.c (commit 99dda3d1).
Patch1:         belle-sip-fix-dns-build.patch
# PATCH-FIX-OPENSUSE fix-build.patch idoenmez@suse.de -- Remove reference to wakelock.h
Patch2:         fix-build.patch
BuildRequires:  antlr3c-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  java
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bctoolbox) >= 0.6.0
BuildRequires:  pkgconfig(zlib)

%description
Belle-sip is a SIP (RFC3261) implementation written in C, with an
object-oriented API.

%package -n %{soname}%{sover}
Summary:        C object-oriented SIP Stack
Group:          System/Libraries

%description -n %{soname}%{sover}
Belle-sip is a SIP (RFC3261) implementation written in C, with an
object-oriented API.

%package devel
Summary:        Headers and libraries for the belle-sip library
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}
Requires:       pkgconfig(bctoolbox)
Requires:       pkgconfig(zlib)

%description devel
Belle-sip is a SIP (RFC3261) implementation written in C, with an
object-oriented API.

This package contains header files and development libraries needed
to develop applications using the belle-sip library.

%prep
%autosetup -p1 -n %{name}-%{version}-0

cp -f %{SOURCE1} antlr3.jar

%build
antlr_jar="$PWD/antlr3.jar"
%cmake \
  -DANTLR3_JAR_PATH="$antlr_jar" \
  -DENABLE_STRICT=OFF            \
  -DENABLE_STATIC=OFF
%make_jobs

%install
%cmake_install

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%license COPYING
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/belle_sip_tester
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_datadir}/BelleSIP/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
