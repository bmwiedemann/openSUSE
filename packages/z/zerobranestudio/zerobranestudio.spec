#
# spec file for package zerobranestudio
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

%if 0%{suse_version} < 1550
%define lua_version 5.1
%define lua_version_nodots 51
%else
%define lua_version_nodots %{nil}
%endif
Name:           zerobranestudio
Version:        1.90
Release:        0
Summary:        Lightweight Lua IDE
License:        MIT
Group:          Development/Tools/IDE
URL:            http://studio.zerobrane.com/
Source:         https://github.com/pkulchenko/ZeroBraneStudio/archive/%{version}.tar.gz
# PATCH-FIX-OPENSUSE use system Lua
Patch0:         zbstudio.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  lua%{lua_version_nodots}-devel
BuildRequires:  lua%{lua_version_nodots}-copas
BuildRequires:  lua%{lua_version_nodots}-lpeg
BuildRequires:  lua%{lua_version_nodots}-luafilesystem
BuildRequires:  lua%{lua_version_nodots}-luasec
%if 0%{suse_version} < 1550
BuildRequires:  lua%{lua_version_nodots}-luasocket
%else
BuildRequires:  luasocket
%endif
BuildRequires:  wxlua-devel
Requires:       libwxlua
Requires:       lua%{lua_version_nodots}-copas
Requires:       lua%{lua_version_nodots}-lpeg
Requires:       lua%{lua_version_nodots}-luafilesystem
Requires:       lua%{lua_version_nodots}-luasec
%if 0%{suse_version} < 1550
Requires:       lua%{lua_version_nodots}-luasocket
%else
Requires:       luasocket
%endif
Requires:       Lua(API) = %{lua_version}
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
%setup -q -n ZeroBraneStudio-%{version}
%patch0 -p1

# remove pre-built binaries
rm -rf bin zbstudio/ZeroBraneStudio.app zbstudio.exe

%build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DLUA_EXECUTABLE=%{_bindir}/lua%{lua_version}

make %{?_smp_mflags}

%install
%cmake_install

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
%defattr(-,root,root)
%doc CHANGELOG.md LICENSE README.md
%{_bindir}/zbstudio
%{_datadir}/zbstudio
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop
%dir %{_datadir}/appdata/
%{_datadir}/appdata/zbstudio.appdata.xml

%changelog
