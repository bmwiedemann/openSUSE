#
# spec file for package pcapplusplus
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%define _oname PcapPlusPlus
Name:           pcapplusplus
Version:        26.07
Release:        0
Summary:        C++ network sniffing and packet parsing and crafting framework
License:        Unlicense
Group:          Productivity/Networking/Other
URL:            https://pcapplusplus.github.io/
Source0:        https://github.com/seladb/PcapPlusPlus/archive/v%{version}.tar.gz#/%{_oname}-%{version}.tar.gz
# Part of Patch5 https://github.com/seladb/PcapPlusPlus/raw/8672f766fd2fdcabff53323ecf23b55d67146c09/Tests/Fuzzers/RegressionTests/regression_samples/crash-pcapng-epb-unbounded-length
Source5:        CVE-2026-13587.bin
# PATCH-FIX-UPSTREAM CVE-2026-13587.patch
Patch5:         CVE-2026-13587.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel >= 1.5
BuildRequires:  pkgconfig

%description
PcapPlusPlus is a C++ network sniffing and packet parsing and
manipulation framework.

%package        devel
Summary:        C++ network sniffing and packet parsing and crafting framework
Group:          Development/Libraries/C and C++
Requires:       libpcap-devel

%description    devel
PcapPlusPlus is a C++ network sniffing and packet parsing and
manipulation framework.

%prep
%autosetup -p1 -n %{_oname}-%{version}
install -m0644 %{SOURCE5} Tests/Fuzzers/RegressionTests/regression_samples/crash-pcapng-epb-unbounded-length
find . -type f -name ".gitignore" -delete

%build
%cmake \
 -DPCAPPP_BUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}

%files devel
%license LICENSE
%doc README.md Examples
%{_includedir}/pcapplusplus
%{_libdir}/libCommon++.so
%{_libdir}/libPacket++.so
%{_libdir}/libPcap++.so
%{_libdir}/libCommon++.so.%{version}
%{_libdir}/libPacket++.so.%{version}
%{_libdir}/libPcap++.so.%{version}
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/PcapPlusPlus.pc

%changelog
