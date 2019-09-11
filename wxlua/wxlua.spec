#
# spec file for package wxlua
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define lua_version 5.1

Name:           wxlua
Version:        3.1.0.git.7d9d59
Release:        0
Summary:        Lua IDE with a GUI debugger and binding generator
License:        SUSE-wxWidgets-3.1
Group:          Development/Languages/Other
Url:            https://github.com/pkulchenko/wxlua
Source:         https://github.com/pkulchenko/wxlua/archive/WX_3_1_0-7d9d59.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/pkulchenko/wxlua/pull/8
Patch0:         desktop.patch
# PATCH-FIX-OPENSUSE Remoevd because webkit is exiting openSUSE:Factory
Patch1:         wx-webview.patch
BuildRequires:  cmake >= 2.8.3
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  lua51-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  wxWidgets-devel >= 3
BuildRequires:  pkgconfig(glu)
%if 0%{?suse_version} > 1320
BuildRequires:  cppcheck
%endif

%description
This package contains Integrated Development Environments (IDE, written in
wxLua) with a GUI debugger, a binding generator and wxWidgets bindings usable
as a module.

%package -n lib%{name}
Summary:        Set of Lua bindings to the C++ wxWidgets cross-platform GUI library
Group:          System/Libraries

%description -n lib%{name}
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
%setup -q -n wxlua-WX_3_1_0-7d9d59
%patch0 -p1
%patch1 -p1
cd wxLua
sed -r -i 's|LIBRARY DESTINATION .*$|LIBRARY DESTINATION %{_lib}|' CMakeLists.txt

%build
cd wxLua
%cmake \
	-DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-config \
	-DwxLua_LUA_LIBRARY_BUILD_SHARED=TRUE \
	-DwxLua_LUA_LIBRARY_USE_BUILTIN=FALSE \
	-DwxLua_LUA_LIBRARY_VERSION=%lua_version \
	-DwxLua_LUA_INCLUDE_DIR=%{lua_incdir} \
	-DwxLua_LUA_LIBRARY=%{_libdir}/liblua.so.%lua_version \
	-DBUILD_SHARED_LIBS=TRUE \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?_smp_mflags}

%install
cd wxLua
%cmake_install

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -p art/wxlualogo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
chmod -x %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wxlualogo.svg

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -p art/wxlualogo.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/

mkdir -p %{buildroot}%{_datadir}/applications/
install -p distrib/autopackage/wxlua.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -Dm644 distrib/autopackage/wxlua.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml

# packaged in separate package wxstedit
rm -rf %{buildroot}%{_datadir}/wxstedit
rm -rf %{buildroot}%{_datadir}/wxStEdit
rm -rf %{buildroot}%{_includedir}/wx/stedit/
rm -rf %{buildroot}%{_prefix}/lib/libwxstedit*.so

mkdir -p %{buildroot}%{_libdir}/lua/%lua_version/
mv %{buildroot}%{_libdir}/libwx.so %{buildroot}%{_libdir}/lua/%lua_version/wx.so

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%post -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig

%files
%{_bindir}/wxLua
%{_bindir}/wxLuaCan
%{_bindir}/wxLuaFreeze
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/%{name}.xml

%files -n lib%{name}
%{_libdir}/lua/%lua_version/wx.so
%{_libdir}/libwxlua*.so

%files devel
%{_includedir}/wxlua/
%{_datadir}/wxlua/

%changelog
