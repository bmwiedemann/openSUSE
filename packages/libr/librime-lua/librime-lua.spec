#
# spec file for package librime-lua
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


Name:           librime-lua
Version:        0.0.0+git20250809.68f9c36
Release:        0
Summary:        Lua plugin for librime
License:        SUSE-Permissive
Group:          System/Libraries
URL:            https://github.com/hchunhui/librime-lua
Source:         %{name}-%{version}.tar.gz
Patch0:         glog.patch
Patch1:         cmake.patch
BuildRequires:  cmake
BuildRequires:  darts
%if 0%{?suse_version} < 1600
BuildRequires:  gcc15-c++
BuildRequires:  libboost_filesystem1_75_0-devel
BuildRequires:  libboost_regex1_75_0-devel
BuildRequires:  xorg-x11-devel
%else
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
%endif
BuildRequires:  librime-private-devel
BuildRequires:  lua54-devel
BuildRequires:  marisa-devel
BuildRequires:  opencc-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  pkgconfig(libglog)
BuildRequires:  pkgconfig(opencc)

%description
Lua plugin for librime.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_C_COMPILER=%{_bindir}/gcc-15 -DCMAKE_CXX_COMPILER=%{_bindir}/g++-15
%else
%cmake -DBUILD_SHARED_LIBS=ON
%endif
%cmake_build

%install
%if 0%{?suse_version} < 1600
g++-15 \
%else
c++ \
%endif
  -fPIC %{optflags} -DNDEBUG -std=c++14 -flto=auto -Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -shared -Wl,-soname,librime-lua.so -o librime-lua.so \
  $(find build/CMakeFiles/rime-lua-objs.dir/src -type f -name "*.o" | sort) \
  -llua5.4 -lm -lrime \
  -lglog -lopencc \
%if 0%{?suse_version} < 1600
  -lpthread -lmarisa \
  -lboost_filesystem \
  -lboost_regex
%else
  -lpthread -lmarisa
%endif
# librime will check the permission and will skip the plugin if the file is not executable, so set 755 here.
install -Dm755 librime-lua.so %{buildroot}%{_libdir}/rime-plugins/librime-lua.so

%files
%doc README.md
%dir %{_libdir}/rime-plugins
%{_libdir}/rime-plugins/librime-lua.so

%changelog
