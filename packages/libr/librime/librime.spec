#
# spec file for package librime
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.6.2~git20200921.4e518b9
Release:        0
Summary:        Rime Input Method Engine
License:        BSD-3-Clause
Group:          System/I18n/Chinese
URL:            https://github.com/rime/librime
Source:         %{name}-%{version}.tar.xz
Source99:       baselibs.conf
#PATCH-FIX-OPENSUSE workaround for gcc bug 53613 on 12.3 and lower
Patch1:         librime-1.1-gcc53613.patch
#PATCH-FIX-OPENSUSE fix boost 1.49 filesystem linking on 12.3 and lower
Patch2:         librime-1.2-BOOST_NO_SCOPED_ENUMS.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glog-devel
BuildRequires:  googletest-devel
BuildRequires:  leveldb-devel
BuildRequires:  libkyotocabinet-devel
BuildRequires:  marisa-devel
BuildRequires:  opencc-devel >= 1.0.2
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  zlib-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
%endif

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
Requires:       rime-plum

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

%prep
%setup -q
%if 0%{?suse_version} <= 1230
%patch1 -p1
%patch2 -p1
%endif

%build
# build internal capnproto
mkdir -p thirdparty/src/capnproto/build
pushd thirdparty/src/capnproto/build
cmake -DCMAKE_INSTALL_PREFIX=../../../ -DCMAKE_CXX_FLAGS="%{optflags} -fPIC" ..
make
make install
popd

%cmake -DCapnProto_DIR=thirdparty/src/%{_lib}/cmake/CapnProto
make %{?_smp_mflags}

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

%files -n librime1
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.6.1

%files devel
%{_includedir}/rime_api.h
%{_includedir}/rime_levers_api.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/rime.pc
%{_datadir}/cmake/rime/

%changelog
