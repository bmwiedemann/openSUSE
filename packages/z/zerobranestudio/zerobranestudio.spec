#
# spec file for package zerobranestudio
#
# Copyright (c) 2024 SUSE LLC
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

%define luaver 54
Name:           zerobranestudio
Version:        2.01
Release:        0
Summary:        Lightweight Lua IDE
License:        MIT
Group:          Development/Tools/IDE
URL:            https://studio.zerobrane.com/
Source:         https://github.com/pkulchenko/ZeroBraneStudio/archive/%{version}.tar.gz
# PATCH-FIX-OPENSUSE use system Lua
Patch0:         zbstudio.patch
# PATCH-FIX-UPSTREAM opensuse-build.patch gh#pkulchenko/ZeroBraneStudio!1198 mcepl@suse.com
# fix dependency on wxLua
Patch1:         opensuse-build.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconf
BuildRequires:  hicolor-icon-theme
# BuildRequires:  lua%%{luaver}-bit32
BuildRequires:  lua%{luaver}-copas
BuildRequires:  lua%{luaver}-devel
BuildRequires:  lua%{luaver}-lpeg
BuildRequires:  lua%{luaver}-luafilesystem
BuildRequires:  lua%{luaver}-luasec
BuildRequires:  lua%{luaver}-luasocket
BuildRequires:  lua-macros
BuildRequires:  wxlua-devel
Requires:       Lua(API) = %{lua_version}
# Yes, we have to include this explicit Require
Requires:       libwxlua
Requires:       lua%{luaver}-copas
Requires:       lua%{luaver}-lpeg
Requires:       lua%{luaver}-luafilesystem
Requires:       lua%{luaver}-luasec
Requires:       lua%{luaver}-luasocket
Recommends:     luajit
Provides:       zbstudio
Provides:       zerobrane-studio
BuildArch:      noarch

%description
ZeroBrane Studio is a lightweight cross-platform Lua IDE with code completion,
syntax highlighting, remote debugger, code analyzer, live coding, and debugging
support for several Lua engines (LuaJIT, Love 2D, Moai, Gideros, Corona,
Marmalade Quick, Cocos2d-x, GSL-shell, Adobe Lightroom, OpenResty/Nginx and
others). It originated from the Estrela Editor.

%prep
%autosetup -p1 -n ZeroBraneStudio-%{version}

# remove pre-built binaries
rm -rf bin zbstudio/ZeroBraneStudio.app zbstudio.exe

%build
cd build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DLUA_EXECUTABLE=%{_bindir}/lua \
    -DLUA_INCLUDE_DIR:PATH=$(pkgconf --variable=includedir lua)
%cmake_build

%install
( cd build
%cmake_install
)

cat >> %{buildroot}%{_datadir}/zbstudio/cfg/user.lua <<EOF
path.lua = '%{_bindir}/lua%{lua_version}'
path.lua52 = '%{_bindir}/lua5.2'
EOF

cp lualibs/lua_parser_loose.lua %{buildroot}%{_datadir}/zbstudio/lualibs/
cp lualibs/lua_lexer_loose.lua %{buildroot}%{_datadir}/zbstudio/lualibs/

# unbundle system provided libraries
rm -rf %{buildroot}%{_datadir}/zbstudio/lualibs/{copas,coxpcall}

# use the doc macro to put it in the right location
rm -rf %{buildroot}%{_datadir}/doc

%fdupes %{buildroot}%{_prefix}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/zbstudio
%{_datadir}/zbstudio
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop
%dir %{_datadir}/appdata/
%{_datadir}/appdata/zbstudio.appdata.xml

%changelog
