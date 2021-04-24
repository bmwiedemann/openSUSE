#
# spec file for package lua-luv
#
# Copyright (c) 2021 SUSE LLC
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


%define mod_name luv
%define upver 1.41.0-0
%define libluv_sover 1
%if 0%{?suse_version}
%define flavor @BUILD_FLAVOR@
%else
%define flavor lua
%endif
%if 0%{?rhel}
%define __cmake cmake3
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif
%if 0%{?fedora} || 0%{?rhel}
%define flavor lua
%endif
%bcond_with public_lib
%define lua_value  %(echo "%{flavor}" |sed -e 's:lua::')
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
Version:        1.41.0
Release:        0
Summary:        Bare libuv bindings for lua
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/luvit/%{mod_name}
Source:         https://github.com/luvit/%{mod_name}/archive/%{upver}/%{mod_name}-%{upver}.tar.gz
BuildRequires:  libuv-devel
BuildRequires:  lua-macros
%lua_provides
%if 0%{?suse_version} && "%{flavor}" == "lua"
ExclusiveArch:  do_not_build
%endif
%if 0%{?suse_version}
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luafilesystem
Requires:       %{flavor}
BuildRequires:  %{flavor}-compat-5.3
# not SUSE
%else
BuildRequires:  lua-devel
BuildRequires:  lua-filesystem
%endif
%if 0%{?rhel}
BuildRequires:  lua-compat53
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

%package devel
Summary:        Header files for %{flavor}-%{mod_name}
Group:          Development/Languages/Other
Requires:       %{flavor}-%{mod_name} = %{version}
%if %{with public_lib}
Requires:       %{flavor}-libluv%{libluv_sover}
%endif

%description devel
This subpackage contains header files for developing applications that
want to make use of %{flavor}-%{mod_name}.

%if %{with public_lib}
%package -n %{flavor}-libluv%{libluv_sover}
Summary:        Lua bindings for libluv as a library
Group:          System/Libraries

%description -n %{flavor}-libluv%{libluv_sover}
This library makes libuv available to lua scripts. It was made
for the luvit project but should usable from nearly any lua
project.

%post -n %{flavor}-libluv%{libluv_sover} -p /sbin/ldconfig
%postun -n %{flavor}-libluv%{libluv_sover} -p /sbin/ldconfig
%endif

%prep
echo "Name is %{name}, Flavor is %{flavor}"
%autosetup -n %{mod_name}-%{upver}

%build
%if %{with public_lib}
# Build libluv.so shared library
%{__cmake} -H. -Bbuild -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_COLOR_MAKEFILE=OFF \
    -DBUILD_STATIC_LIBS=OFF -DCMAKE_INSTALL_DO_STRIP=OFF \
    -DBUILD_MODULE=OFF -DBUILD_SHARED_LIBS=ON \
    -DWITH_SHARED_LIBUV=ON -DWITH_LUA_ENGINE=Lua \
    -DLUA_INCLUDE_DIR:PATH="%{lua_incdir}" \
    -DLUA_BUILD_TYPE=System -DLUA_COMPAT53_DIR="%{lua_incdir}/"
( cd build ; make )
%endif

# Build luv.so module
%{__cmake} -H. -Bbuild -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_COLOR_MAKEFILE=OFF \
    -DBUILD_STATIC_LIBS=OFF -DCMAKE_INSTALL_DO_STRIP=OFF \
    -DBUILD_MODULE=ON -DBUILD_SHARED_LIBS=ON \
    -DWITH_SHARED_LIBUV=ON -DWITH_LUA_ENGINE=Lua \
    -DLUA_INCLUDE_DIR:PATH="%{lua_incdir}" \
    -DLUA_BUILD_TYPE=System -DLUA_COMPAT53_DIR="%{lua_incdir}/"
( cd build ; make )

find build -name \*.so\*

%install
install -v -D -m 0755 -p build/luv.so %{buildroot}%{lua_archdir}/luv.so
%if %{with public_lib}
mkdir -p %{buildroot}%{lua_archdir}/
install -v -m 0755 -p build/libluv* %{buildroot}%{lua_archdir}/
%endif
mkdir -p %{buildroot}%{lua_incdir}/%{mod_name}
install -v -m 0644 -p src/*.h %{buildroot}%{lua_incdir}/%{mod_name}/

%files
%license LICENSE.txt
%doc *.md
%{lua_archdir}/luv.so

%files devel
%license LICENSE.txt
%dir %{lua_incdir}/%{mod_name}
%{lua_incdir}/%{mod_name}/*
%if %{with public_lib}
%{lua_archdir}/libluv.so

%files -n %{flavor}-libluv%{libluv_sover}
%{lua_archdir}/libluv.so.*
%endif

%changelog
