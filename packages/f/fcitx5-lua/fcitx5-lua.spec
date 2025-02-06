#
# spec file for package fcitx5-lua
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


Name:           fcitx5-lua
Version:        5.0.14
Release:        0
Summary:        Lua support for fcitx
License:        LGPL-2.1-or-later
URL:            https://github.com/fcitx/fcitx5-lua
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  gcc-c++
BuildRequires:  zstd
Supplements:    fcitx5
%if 0%{?suse_version} >= 1550
BuildRequires:  lua54-devel
%else
BuildRequires:  lua53-devel
%endif
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
Lua support for fcitx

%package devel
Summary:        Development files for fcitx5-lua
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package provides development files for fcitx5-lua.

%prep
%setup -q

%build
%cmake
%make_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES
%doc README.md
%dir %{_fcitx5_datadir}/lua
%dir %{_fcitx5_datadir}/lua/imeapi
%{_fcitx5_libdir}/libluaaddonloader.so
%{_fcitx5_addondir}/imeapi.conf
%{_fcitx5_addondir}/luaaddonloader.conf
%{_fcitx5_datadir}/lua/imeapi/imeapi.lua
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Lua.metainfo.xml

%files devel
%dir %{_includedir}/Fcitx5/Module
%dir %{_includedir}/Fcitx5/Module/fcitx-module
%dir %{_includedir}/Fcitx5/Module/fcitx-module/luaaddonloader
%dir %{_libdir}/cmake/Fcitx5ModuleLuaAddonLoader
%{_includedir}/Fcitx5/Module/fcitx-module/luaaddonloader/luaaddon_public.h
%{_libdir}/cmake/Fcitx5ModuleLuaAddonLoader/Fcitx5ModuleLuaAddonLoaderConfig.cmake
%{_libdir}/cmake/Fcitx5ModuleLuaAddonLoader/Fcitx5ModuleLuaAddonLoaderConfigVersion.cmake

%changelog
