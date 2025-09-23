#
# spec file for package ilbc
#
# Copyright (c) 2025 SUSE LLC
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


%define sover 3
%define libname libilbc%{sover}

Name:           ilbc
Summary:        Internet Low Bitrate Codec
License:        BSD-3-Clause
Group:          System/Libraries
Version:        3.0.4
Release:        0
URL:            https://github.com/TimothyGu/libilbc
Source:         https://github.com/TimothyGu/libilbc/archive/refs/tags/v%{version}.tar.gz#/libilbc-%{version}.tar.gz
Patch0:         ilbc-cmake-cflags.patch
Patch1:         ilbc-cmake-cpp17.patch
BuildRequires:  abseil-cpp-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for
robust voice communication over IP. The codec is designed for narrow
band speech and results in a payload bit rate of 13.33 kbit/s with an
encoding frame length of 30 ms and 15.20 kbps with an encoding length
of 20 ms. The iLBC codec enables graceful speech quality degradation in
the case of lost frames, which occurs in connection with lost or
delayed IP packets.

%package -n %{libname}
Summary:        Internet Low Bitrate Codec
Group:          System/Libraries
Provides:       ilbc = %{version}
Obsoletes:      ilbc <= %{version}

%description -n %{libname}
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for
robust voice communication over IP. The codec is designed for narrow
band speech and results in a payload bit rate of 13.33 kbit/s with an
encoding frame length of 30 ms and 15.20 kbps with an encoding length
of 20 ms. The iLBC codec enables graceful speech quality degradation in
the case of lost frames, which occurs in connection with lost or
delayed IP packets.

%package devel
Summary:        Libraries and Header Files to Develop Programs with iLBC Support
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Libraries and Header Files to Develop Programs with iLBC Support.

%prep
%autosetup -p1 -n libilbc-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
rm -Rv %{buildroot}%{_docdir}/ilbc

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING
%doc README.md NEWS.md
%{_libdir}/libilbc.so.%{sover}*

%files devel
%{_bindir}/ilbc_test
%{_includedir}/ilbc.h
%{_includedir}/ilbc_export.h
%{_libdir}/libilbc.so
%{_libdir}/pkgconfig/libilbc.pc

%changelog
