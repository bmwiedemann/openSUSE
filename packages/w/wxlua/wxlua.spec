#
# spec file for package wxlua
#
# Copyright (c) 2021 SUSE LLC
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

%define binds webview;gl;xrc;xml;net;media;propgrid;richtext;aui;stc;html;adv;core;base
%define sover 3_1_0_0
Name:           wxlua
Version:        3.1.0.0+27
Release:        0
Summary:        Lua bindings for wxWidgets
License:        GPL-2.0-or-later WITH WxWindows-exception-3.1
Group:          Development/Languages/Other
URL:            https://github.com/pkulchenko/wxlua
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ccache
BuildRequires:  cmake >= 2.8
BuildRequires:  cppcheck
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  lua54-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  wxGTK3-devel >= 3.1.3
BuildRequires:  pkgconfig(glu)

%description
Lua bindings for wxWidgets cross-patform GUI toolkit;
supports Lua 5.1, 5.2, 5.3, 5.4, LuaJIT and wxWidgets 3.x

%package -n lib%{name}
Summary:        Set of Lua bindings to the C++ wxWidgets cross-platform GUI library
Group:          System/Libraries
Requires:       libwxlua-wx31-%{sover} = %{version}
Requires:       libwxlua_bind-wx31-%{sover} = %{version}
Requires:       libwxlua_debug-wx31-%{sover} = %{version}
Requires:       libwxlua_debugger-wx31-%{sover} = %{version}

%description -n lib%{name}
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

%package -n libwxlua-wx31-%{sover}
Summary:        Lua bindings to the C++ wxWidgets cross-platform GUI library
Group:          System/Libraries

%description -n libwxlua-wx31-%{sover}
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

%package -n libwxlua_bind-wx31-%{sover}
Summary:        Lua bindings to the C++ wxWidgets cross-platform GUI library
Group:          System/Libraries

%description -n libwxlua_bind-wx31-%{sover}
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

%package -n libwxlua_debug-wx31-%{sover}
Summary:        Lua bindings to the C++ wxWidgets cross-platform GUI library
Group:          System/Libraries

%description -n libwxlua_debug-wx31-%{sover}
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

%package -n libwxlua_debugger-wx31-%{sover}
Summary:        Lua bindings to the C++ wxWidgets cross-platform GUI library
Group:          System/Libraries

%description -n libwxlua_debugger-wx31-%{sover}
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.


%package devel
Summary:        Development files of lib%{name}
Group:          Development/Languages/C and C++
Requires:       lib%{name} = %{version}

%description devel
This package contains files to be used in your C++ programs to embed a Lua
interpreter with the wxWidgets API.

%prep
%setup -q

cd wxLua
sed -r -i 's|LIBRARY DESTINATION .*$|LIBRARY DESTINATION %{_lib}|' CMakeLists.txt

%build
cd wxLua/build
cmake .. \
	-DCMAKE_CXX_FLAGS="-DwxLUA_USE_wxTranslations=0" \
	-DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-config \
	-DwxLua_LUA_LIBRARY_BUILD_SHARED=TRUE \
	-DwxLua_LUA_LIBRARY_USE_BUILTIN=FALSE \
	-DwxLua_LUA_LIBRARY_VERSION=%{lua_version} \
	-DwxLua_LUA_INCLUDE_DIR=%{lua_incdir} \
	-DwxLua_LUA_LIBRARY=%{_libdir}/liblua%{lua_version}.so.5 \
	-DBUILD_SHARED_LIBS=TRUE \
	-DwxWidgets_COMPONENTS="%{binds}" \
	-DwxLuaBind_COMPONENTS="%{binds}" \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_INSTALL_PREFIX=%{_prefix}

pushd modules/luamodule
make %{?_smp_mflags}
popd

make %{?_smp_mflags}

%install
cd wxLua
%cmake_install

rm -f %{buildroot}%{_bindir}/lua{,c}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -p art/wxlualogo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
chmod -x %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wxlualogo.svg

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -p art/wxlualogo.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/

mkdir -p %{buildroot}%{_datadir}/applications/
install -p distrib/autopackage/wxlua.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -Dm644 distrib/autopackage/wxlua.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml

mkdir -p %{buildroot}%{_libdir}/lua/%{lua_version}/
mv %{buildroot}%{_libdir}/libwx.so %{buildroot}%{_libdir}/lua/%{lua_version}/wx.so

sed 's-#!/usr/bin/env lua-#!/usr/bin/lua%{lua_version}-g' -i %{buildroot}%{_datadir}/wxlua/apps/wxluafreeze/*

%post -n libwxlua-wx31-%{sover} -p /sbin/ldconfig
%postun -n libwxlua-wx31-%{sover} -p /sbin/ldconfig
%post -n libwxlua_bind-wx31-%{sover} -p /sbin/ldconfig
%postun -n libwxlua_bind-wx31-%{sover} -p /sbin/ldconfig
%post -n libwxlua_debug-wx31-%{sover} -p /sbin/ldconfig
%postun -n libwxlua_debug-wx31-%{sover} -p /sbin/ldconfig
%post -n libwxlua_debugger-wx31-%{sover} -p /sbin/ldconfig
%postun -n libwxlua_debugger-wx31-%{sover} -p /sbin/ldconfig

%files
%{_bindir}/wxLua
%{_bindir}/wxLuaCan
%{_bindir}/wxLuaFreeze
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/%{name}.xml

%files -n lib%{name}
%{_libdir}/lua/%{lua_version}/wx.so

%files -n libwxlua-wx31-%{sover}
%{_libdir}/libwxlua-wx31*.so

%files -n libwxlua_bind-wx31-%{sover}
%{_libdir}/libwxlua_bind-wx31*.so

%files -n libwxlua_debug-wx31-%{sover}
%{_libdir}/libwxlua_debug-wx31*.so

%files -n libwxlua_debugger-wx31-%{sover}
%{_libdir}/libwxlua_debugger-wx31*.so

%files devel
%{_includedir}/wxlua/
%{_datadir}/wxlua/

%changelog
