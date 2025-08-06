#
# spec file for package librime
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


Name:           librime
Version:        1.14.0
Release:        0
Summary:        Rime Input Method Engine
License:        BSD-3-Clause
Group:          System/I18n/Chinese
URL:            https://github.com/rime/librime
Source:         https://github.com/rime/%{name}/archive/refs/tags/%{version}.tar.gz
#PATCH-FIX-OPENSUSE librime-boost166.patch i@marguerite.su -- leap's gcc7 has no <filesystem>
Patch0:         librime-boost166.patch
BuildRequires:  capnproto >= 0.7.0
BuildRequires:  cmake >= 3.1.0
BuildRequires:  gcc-c++
BuildRequires:  glog-devel
BuildRequires:  googletest-devel
BuildRequires:  leveldb-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libcapnp-devel >= 0.7.0
BuildRequires:  libkyotocabinet-devel
BuildRequires:  marisa-devel
BuildRequires:  opencc-devel >= 1.0.2
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  zlib-devel

%description
Rime is an Traditional Chinese input method engine.
Its idea comes from ancient Chinese brush and carving art.
Mainly it's about to express your thinking with your keystrokes.

%package -n rime
Summary:        Rime Input Method Engine
Group:          System/I18n/Chinese

%description -n rime
Rime is an Traditional Chinese input method engine.
Its idea comes from ancient Chinese brush and carving art.
Mainly it's about to express your thinking with your keystrokes.

%package -n librime1
Summary:        Rime Input Method Engine
# dictionaries
Group:          System/Libraries
Recommends:     brise
# configuration manager
Recommends:     rime-plum

%description -n librime1
Rime is an Traditional Chinese input method engine.
Its idea comes from ancient Chinese brush and carving art.
Mainly it's about to express your thinking with your keystrokes.

This package is the runtime libraries of Rime.

%package devel
Summary:        Development files of Rime
Group:          Development/Libraries/C and C++
Requires:       rime = %{version}

%description devel
Rime is an Traditional Chinese input method engine.
Its idea comes from ancient Chinese brush and carving art.
Mainly it's about to express your thinking with your keystrokes.

This package is the development headers of Rime.

%package private-devel
Summary:        Private headers for rime
Group:          Development/Libraries/C and C++
Requires:       librime-devel = %{version}

%description private-devel
This package provides private headers of Rime to build plugins.

%prep
%setup -q
%if 0%{?suse_version} == 1500
%patch -P 0 -p 1
%endif

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
  -DINSTALL_PRIVATE_HEADERS=On \
  -DENABLE_EXTERNAL_PLUGINS=On \
  -DBUILD_MERGED_PLUGINS=On \
  -DENABLE_LOGGING=On
%cmake_build

%install
%cmake_install

%post -n librime1 -p /sbin/ldconfig
%postun -n librime1 -p /sbin/ldconfig

%files -n rime
%license LICENSE
%doc README.md
%{_bindir}/rime_deployer
%{_bindir}/rime_dict_manager
%{_bindir}/rime_patch
%{_bindir}/rime_table_decompiler

%files -n librime1
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.%{version}

%files devel
%{_includedir}/rime_api.h
%{_includedir}/rime_levers_api.h
%{_includedir}/rime_api_deprecated.h
%{_includedir}/rime_api_stdbool.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/rime.pc
%{_datadir}/cmake/rime/

%files private-devel
%{_includedir}/rime

%changelog
