#
# spec file
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


%define flavor @BUILD_FLAVOR@
%define mod_name editorconfig-core-lua
Version:        0.3.0
Release:        0
Summary:        EditorConfig Core support for the Lua language
License:        BSD-2-Clause
Group:          Development/Libraries/Other
URL:            https://github.com/editorconfig/editorconfig-core-lua
Source:         https://github.com/editorconfig/%{mod_name}/archive/v%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE build-with-lua51.patch gh#editorconfig/editorconfig-core-lua!5 mcepl@suse.com
# make package building with Lua 5.1 and LuaJIT
Patch0:         build-with-lua51.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luafilesystem
BuildRequires:  %{flavor}-penlight
BuildRequires:  cmake
BuildRequires:  libeditorconfig-devel
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
Provides:       %{flavor}-LPeg = %{version}
Obsoletes:      %{flavor}-LPeg < %{version}
%endif

%description
EditorConfig makes it easy to maintain the correct coding
style when switching between different text editors
and betweendifferent projects. The EditorConfig project
maintains a file format and plugins for various text editors
which allow this file format to be read and used by those
editors. EditorConfig Lua Core provides the same functionality
as the Editorconfig C Core library.

%prep
%autosetup -p1 -n %{mod_name}-%{version}

%build
%cmake -DECL_LIBDIR:PATH=%{lua_archdir} \
    -DLUA_LIBRARY:PATH=%{lua_archdir} \
    -DLUA_INCLUDE_DIR:PATH=%{lua_incdir}

%install
%cmake_install

%check
cd build
export LUA_CPATH="./?.so;%{lua_archdir}/?.so;${LUA_CPATH}"
lua ../editorconfig.lua -v

%files
%license LICENSE
%doc README.md
%{lua_archdir}/editorconfig.so

%changelog
