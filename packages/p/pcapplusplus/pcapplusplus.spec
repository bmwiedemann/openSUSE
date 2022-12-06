#
# spec file for package pcapplusplus
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


%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%define _oname PcapPlusPlus
Name:           pcapplusplus
Version:        22.11
Release:        0
Summary:        C++ network sniffing and packet parsing and crafting framework
License:        Unlicense
Group:          Productivity/Networking/Other
URL:            https://pcapplusplus.github.io/
Source0:        https://github.com/seladb/PcapPlusPlus/archive/v%{version}.tar.gz#/%{_oname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE pcap++-paths.patch
Patch2:         pcap++-paths.patch
BuildRequires:  dos2unix
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
%setup -q -n %{_oname}-%{version}
%patch2 -p1
dos2unix Examples/*/* README.md
chmod -x Examples/Tutorials/Tutorial-DpdkL2Fwd/WorkerThread.*

%build
export CXXFLAGS="%{optflags}"
./configure-linux.sh \
   --use-immediate-mode \
   --default

# it looks like the build is not parallel-safe
make libs

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIB=%{_lib} \
     INCLUDEDIR=%{_includedir} libs install
%fdupes -s %{buildroot}

%files devel
%license LICENSE
%doc README.md Examples
%{_libdir}/libCommon++.a
%{_libdir}/libPacket++.a
%{_libdir}/libPcap++.a
%{_libdir}/pkgconfig/PcapPlusPlus.pc
%{_includedir}/pcapplusplus

%changelog
