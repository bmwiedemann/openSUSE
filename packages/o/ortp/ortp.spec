#
# spec file for package ortp
#
# Copyright (c) 2023 SUSE LLC
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


%define soname  libortp
%define sover   15
%define docuver 5.2.0

Name:           ortp
Version:        5.2.6
Release:        0
Summary:        Real-time Transport Protocol Stack
License:        GPL-3.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://linphone.org/technical-corner/ortp/
Source:         https://gitlab.linphone.org/BC/public/ortp/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE deps.diff
Patch0:         deps.diff
BuildRequires:  chrpath
BuildRequires:  cmake >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bctoolbox) >= 5.2.0

%description
oRTP is a C library implementing the RTP protocol (RFC 1889).

%package -n %{soname}%{sover}
Summary:        Real-time Transport Protocol Stack
Group:          System/Libraries

%description -n %{soname}%{sover}
oRTP is a C library implementing the RTP protocol (RFC 1889).

%package devel
Summary:        Headers, libraries and docs for the oRTP library
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}
Requires:       cmake
Provides:       %{soname}-devel = %{version}
Obsoletes:      %{soname}-devel < %{version}

%description devel
oRTP is a C library implementing the RTP protocol (RFC 1889).

This package contains header files and development libraries needed to
develop programs using the oRTP library.

%prep
%autosetup -p1

%build
%cmake \
  -DENABLE_STATIC=OFF \
  -DENABLE_DOC=OFF
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}
# manually keeping the version here because upstream doesn't (usually) update the patch version
mv -T %{buildroot}%{_datadir}/doc/%{name}-%{docuver} %{buildroot}%{_docdir}/%{name}

# for some reason, pkgconfig file contains wrong libdir
sed -i "s,-L/usr/lib,-L%{_libdir}," %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc

chrpath -d %{buildroot}%{_libdir}/%{soname}.so.%{sover}*

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%doc %{_docdir}/%{name}/
%{_bindir}/ortp_tester

%files -n %{soname}%{sover}
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%dir %{_libdir}/cmake/ortp
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/ortp/*

%changelog
