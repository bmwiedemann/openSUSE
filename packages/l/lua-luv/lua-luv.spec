#
# spec file
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2012 Togan Muftuoglu toganm@opensuse.org
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


%if %{lua_version_nodots} == 51
%define lua_default 1
%endif
%define mod_name luv
%define upver 1.51.0-1
%define fixver %(echo %{upver}|sed 's|-|+|g')
%define libluv_sover 1
%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
Version:        %{fixver}
Release:        0
Summary:        Bare libuv bindings for lua
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/luvit/luv
Source0:        https://github.com/luvit/luv/releases/download/%{upver}/luv-%{upver}.tar.gz
Patch0:         lua-link.patch
Patch1:         luv-module-install.patch
BuildRequires:  %{flavor}-compat-5.3
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luafilesystem
BuildRequires:  cmake
BuildRequires:  libuv-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == "lua"
ExclusiveArch:  do_not_build
%endif

%description
This library makes libuv available to lua scripts. It was made
for the luvit project but should usable from nearly any lua
project.

The library can be used by multiple threads at once. Each thread
is assumed to load the library from a different lua_State. Luv
will create a unique uv_loop_t for each state. You can't share uv
handles between states/loops.

The best docs currently are the libuv docs themselves. Hopfully
soon we'll have a copy locally tailored for lua.

%if 0%{?lua_default}
%package -n libluv-devel
Summary:        Header files for %{flavor}-%{mod_name}
Group:          Development/Languages/Other
Requires:       libluv%{libluv_sover} = %{version}

%description -n libluv-devel
This subpackage contains header files for developing applications that
want to make use of %{flavor}-%{mod_name}.

%package -n libluv%{libluv_sover}
Summary:        Lua bindings for libluv as a library
Group:          System/Libraries

%description -n libluv%{libluv_sover}
This library makes libuv available to lua scripts. It was made
for the luvit project but should usable from nearly any lua
project.

%post -n libluv%{libluv_sover} -p /sbin/ldconfig
%postun -n libluv%{libluv_sover} -p /sbin/ldconfig
%endif

%prep
echo "Name is %{name}, Flavor is %{flavor}"
%autosetup -p1 -n %{mod_name}-%{upver}

%build
%cmake \
    -DWITH_SHARED_LIBUV=ON \
    -DWITH_LUA_ENGINE=Lua \
    -DLUA_BUILD_TYPE=System \
    -DLUA_INCLUDE_DIR=%{lua_incdir} \
    -DMODULE_INSTALL_LIB_DIR=%{lua_archdir} \
    -DSHAREDLIBS_INSTALL_LIB_DIR=%{_libdir} \
    -DBUILD_SHARED_LIBS=OFF \
    -DLUA_COMPAT53_DIR="%{lua_incdir}" \
    %{?lua_default:-DBUILD_SHARED_LIBS=ON}
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc *.md
%{lua_archdir}/luv.so

%if 0%{?lua_default}
%files -n libluv-devel
%license LICENSE.txt
%{_includedir}/%{mod_name}
%{_libdir}/libluv.so
%{_libdir}/pkgconfig/*.pc

%files -n libluv%{libluv_sover}
%{_libdir}/libluv.so.*
%endif

%changelog
