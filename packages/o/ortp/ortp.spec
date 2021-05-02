#
# spec file for package ortp
#
# Copyright (c) 2021 SUSE LLC
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
Name:           ortp
Version:        4.5.10
Release:        0
Summary:        Real-time Transport Protocol Stack
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://linphone.org/technical-corner/ortp/
Source:         https://github.com/BelledonneCommunications/ortp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE deps.diff
Patch0:         deps.diff
BuildRequires:  cmake >= 3.0
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bctoolbox) >= 4.5.0

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
%cmake -DENABLE_STATIC=OFF
%make_build

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}/
# manually keeping the version here because upstream doesn't (usually) update the patch version
mv -T %{buildroot}%{_datadir}/doc/%{name}-4.5.0/ \
  %{buildroot}%{_docdir}/%{name}/

mv %{buildroot}%{_datadir}/doc/%{name}-./LICENSE.txt %{buildroot}%{_docdir}/%{name}/
mv %{buildroot}%{_datadir}/doc/%{name}-./AUTHORS.md %{buildroot}%{_docdir}/%{name}/
mv %{buildroot}%{_datadir}/doc/%{name}-./README.md %{buildroot}%{_docdir}/%{name}/
mv %{buildroot}%{_datadir}/doc/%{name}-./CHANGELOG.md %{buildroot}%{_docdir}/%{name}/

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%doc %{_docdir}/%{name}/
%license %{_docdir}/%{name}/LICENSE.txt
%{_docdir}/%{name}/README.md
%{_docdir}/%{name}/CHANGELOG.md
%{_docdir}/%{name}/AUTHORS.md

%files -n %{soname}%{sover}
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%dir %{_libdir}/cmake/ortp
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/ortp/*

%changelog
