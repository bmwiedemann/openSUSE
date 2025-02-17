#
# spec file for package bctoolbox
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


%define sover   1
Name:           bctoolbox
Version:        5.3.105
Release:        0
Summary:        Utility library for software from Belledonne Communications
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://linphone.org/
Source:         https://gitlab.linphone.org/BC/public/bctoolbox/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE bctoolbox-fix-pkgconfig.patch
Patch0:         bctoolbox-fix-pkgconfig.patch
Patch2:         set_curret_version.patch
BuildRequires:  bcunit-devel >= 5.3.0
%if 0%{?suse_version} >= 1600
# At the time of writing (11/Dec/2023), decaf is only available on Tumbleweed.
BuildRequires:  decaf-devel
%endif
BuildRequires:  chrpath
BuildRequires:  cmake >= 3.22
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bcunit) >= 5.3.0
%if 0%{?suse_version} > 1600
BuildRequires:  pkgconfig(mbedtls) < 3.0.0
BuildRequires:  pkgconfig(mbedtls) >= 2.0.0
%else
BuildRequires:  mbedtls-devel
%endif
BuildRequires:  pkgconfig(zlib)

%description
Utilities library used by Belledonne Communications softwares like
belle-sip, mediastreamer2 and linphone.

%package devel
Summary:        Development files for %{name}, a utility library for linphone/belle-sip/etc
Group:          Development/Libraries/C and C++
Requires:       cmake
Requires:       lib%{name}%{sover} = %{version}
Requires:       lib%{name}-tester%{sover} = %{version}
Requires:       mbedtls-devel < 3

%description devel
Utilities library used by Belledonne Communications softwares like
belle-sip, mediastreamer2 and linphone.

This package contains development files.

%package -n lib%{name}%{sover}
Summary:        Utility library for software from Belledonne Communications
Group:          Development/Libraries/C and C++

%description -n lib%{name}%{sover}
Utilities library used by Belledonne Communications softwares like
belle-sip, mediastreamer2 and linphone.

This package the contains shared library.

%package -n lib%{name}-tester%{sover}
Summary:        Utility library for software from Belledonne Communications
Group:          Development/Libraries/C and C++

%description -n lib%{name}-tester%{sover}
Utilities library used by Belledonne Communications softwares like
belle-sip, mediastreamer2 and linphone.

This package the contains shared library for testing component.

%prep
%autosetup -p1

%build
export CFLAGS=$(echo "$CFLAGS -Wno-error=maybe-uninitialized -Wno-error=unused-parameter")
export CXXFLAGS=$(echo "$CXXFLAGS -Wno-error=maybe-uninitialized -Wno-error=unused-parameter")
%cmake \
  -DENABLE_STATIC=OFF
%cmake_build

%install
%cmake_install
chrpath -d %{buildroot}%{_libdir}/lib%{name}.so.%{sover}* %{buildroot}%{_libdir}/lib%{name}-tester.so.%{sover}* %{buildroot}%{_bindir}/bctoolbox-tester

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig
%post -n lib%{name}-tester%{sover} -p /sbin/ldconfig
%postun -n lib%{name}-tester%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license LICENSE.txt
%{_libdir}/lib%{name}.so.%{sover}*

%files -n lib%{name}-tester%{sover}
%license LICENSE.txt
%{_bindir}/bctoolbox-tester
%{_libdir}/lib%{name}-tester.so.%{sover}*

%files devel
%license LICENSE.txt
%doc README.md
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/lib%{name}-tester.so
%{_libdir}/pkgconfig/bctoolbox-tester.pc
%dir %{_datadir}/BCToolbox
%dir %{_datadir}/BCToolbox/cmake
%{_datadir}/BCToolbox/cmake/*.cmake
%{_datadir}/BCToolbox/cmake/gitversion.h.in

%changelog
