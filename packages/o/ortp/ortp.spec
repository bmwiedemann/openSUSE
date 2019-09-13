#
# spec file for package ortp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname  libortp
%define sover   13
Name:           ortp
Version:        1.0.2
Release:        0
Summary:        Real-time Transport Protocol Stack
License:        GPL-2.0+
Group:          Productivity/Telephony/Utilities
Url:            https://linphone.org/technical-corner/ortp/overview
Source:         https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE deps.diff
Patch0:         deps.diff
BuildRequires:  cmake >= 3.0
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bctoolbox) >= 0.6.0

%description
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889).

%package -n %{soname}%{sover}
Summary:        Real-time Transport Protocol Stack
Group:          System/Libraries

%description -n %{soname}%{sover}
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889).

%package devel
Summary:        Headers, libraries and docs for the oRTP library
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}
Requires:       cmake
Provides:       %{soname}-devel = %{version}
Obsoletes:      %{soname}-devel < %{version}

%description devel
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889).

This package contains header files and development libraries needed to
develop programs using the oRTP library.

%prep
%setup -q -n %{name}-%{version}-0
%patch0 -p1

%build
%cmake \
  -DENABLE_TESTS=ON   \
  -DENABLE_STATIC=OFF \
  -DENABLE_STRICT=OFF
make %{?_smp_mflags} V=1

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}/
mv -T %{buildroot}%{_datadir}/doc/%{name}-%{version}/ \
  %{buildroot}%{_docdir}/%{name}/

sed -i "s|%{_prefix}/lib|%{_libdir}|g" %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%doc %{_docdir}/%{name}/
%{_bindir}/mrtprecv
%{_bindir}/mrtpsend
%{_bindir}/rtprecv
%{_bindir}/rtpsend
%{_bindir}/rtpsend_stupid
%{_bindir}/test_timer
%{_bindir}/tevrtprecv
%{_bindir}/tevrtpsend

%files -n %{soname}%{sover}
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so
%{_datadir}/oRTP/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
