#
# spec file for package lua-lua-ev
#
# Copyright (c) 2022 SUSE LLC
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


%define flavor @BUILD_FLAVOR@
%define mod_name lua-ev
%define lua_value  %(echo "%{flavor}" |sed -e 's:lua::')
%define upversion 1.5
%define libev_sover 1
%bcond_with public_lib
Version:        1.5
Release:        0
Summary:        Lua integration with libev
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/brimworks/lua-ev
Source:         https://github.com/brimworks/%{mod_name}/archive/v%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
# PATCH-FIX-UPSTREAM lua54.patch gh#brimworks/lua-ev#24 mcepl@suse.com
# Resolve FTBFS with Lua 5.4.
Patch0:         lua54.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  cmake
BuildRequires:  libev-devel
BuildRequires:  lua-macros
# BuildRequires:  %%{flavor}-luafilesystem
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
Lua integration with libev (http://dist.schmorp.de/libev)

%package devel
Summary:        Header files for %{flavor}-%{mod_name}
Group:          Development/Languages/Other
Requires:       %{flavor}-%{mod_name} = %{version}
%if %{with public_lib}
Requires:       %{flavor}-libev%{libev_sover}
%endif

%description devel
This subpackage contains header files for developing applications that
want to make use of %{flavor}-%{mod_name}.

%if %{with public_lib}
%package -n %{flavor}-libev%{libev_sover}
Summary:        Lua bindings for libev as a library
Group:          System/Libraries

%description -n %{flavor}-libev%{libev_sover}
This library makes libev available to lua scripts. It was made
for the luvit project but should usable from nearly any lua
project.

%post -n %{flavor}-libev%{libev_sover} -p /sbin/ldconfig
%postun -n %{flavor}-libev%{libev_sover} -p /sbin/ldconfig
%endif

%prep
%setup -q -n %{mod_name}-%{upversion}
%autopatch -p1

# Remove bundled dependencies
rm -rf deps

# Remove network sensitive tests gh#luvit/luv#340
rm -fv tests/test-dns.lua

%build
%if %{with public_lib}
# Build libev.so shared library
cmake -H. -Bbuild -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_COLOR_MAKEFILE=OFF \
    -DBUILD_SHARED_LIBS=ON
( cd build ; make )
mv build/ev.so build/libev.so.%{libev_sover}
%endif

# Build ev.so module
cmake -H. -Bbuild -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_COLOR_MAKEFILE=OFF \
    -DBUILD_SHARED_LIBS=ON
( cd build ; make )

%install
install -v -D -m 0755 -p -t %{buildroot}%{lua_archdir} build/ev.so
%if %{with public_lib}
install -v -m 0755 -p -t %{buildroot}%{lua_archdir} build/libev*
ln -sf libev.so.* %{buildroot}%{lua_archdir}/libev.so
%endif
install -v -D -m 0644 -p -t %{buildroot}%{lua_incdir}/%{mod_name} *.h

%check
cd build
# %%make_build test

%files
%doc README example.lua
%{lua_archdir}/ev.so

%files devel
%dir %{lua_incdir}
%dir %{lua_incdir}/%{mod_name}
%{lua_incdir}/%{mod_name}/*
%if %{with public_lib}
%{lua_archdir}/libev.so

%files -n %{flavor}-libev%{libev_sover}
%{lua_archdir}/libev.so.*
%endif

%changelog
