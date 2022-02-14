#
# spec file for package librime-lua
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


Name:           librime-lua
Version:        0.0.0+git20211220.8b37d55
Release:        0
Summary:        Lua plugin for librime
License:        SUSE-Permissive
URL:            https://github.com/hchunhui/librime-lua
Source:         %{name}-%{version}.tar.xz
Patch:          boost_signals2.patch
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  darts
BuildRequires:  gcc-c++
BuildRequires:  librime-private-devel
BuildRequires:  lua54-devel
BuildRequires:  marisa-devel
BuildRequires:  pkgconfig(libglog)
BuildRequires:  pkgconfig(opencc)
BuildRequires:  xorgproto-devel

%description
Lua plugin for librime.

%prep
%setup -q
%patch -p1

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
c++ -fPIC %{optflags} -DNDEBUG -std=c++14 -flto=auto -Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -shared -Wl,-soname,librime-lua.so -o librime-lua.so \
  $(find build/CMakeFiles/rime-lua-objs.dir/src -type f -name "*.o" | sort) \
  -llua5.4 -lm -lrime \
  -lglog -lopencc \
  -lpthread -lmarisa
# librime will check the permission and will skip the plugin if the file is not executable, so set 755 here.
install -Dm755 librime-lua.so %{buildroot}%{_libdir}/rime-plugins/librime-lua.so

%files
%doc README.md
%dir %{_libdir}/rime-plugins
%{_libdir}/rime-plugins/librime-lua.so

%changelog

