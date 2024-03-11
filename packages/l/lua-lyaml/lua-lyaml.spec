#
# spec file for package lua-lyaml
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


%define flavor @BUILD_FLAVOR@
%define mod_name lyaml
Version:        6.2.8
Release:        0
Summary:        LibYAML binding for Lua
License:        MIT
URL:            https://github.com/gvvaughan/lyaml
Source0:        https://github.com/gvvaughan/lyaml/archive/v%{version}.tar.gz#$/%{mod_name}-%{version}.tar.gz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
Requires:       %{flavor}
BuildRequires:  %{flavor}-luarocks
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:	pkgconfig(yaml-0.1)
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
LibYAML binding for Lua, with a fast C implementation for converting between YAML 1.1 and Lua tables,
and a low-level YAML event parser for implementing more intricate YAML document loading.

%prep
%autosetup -n %{mod_name}-%{version}

%build
                                        
export PREFIX="%{_prefix}"
luarocks make --no-install %{mod_name}-%{version}-1.rockspec

%install
mkdir -p -m 755 %{buildroot}%{lua_archdir} \
    %{buildroot}%{lua_noarchdir}/lyaml
install -m755 linux/yaml.so %{buildroot}%{lua_archdir}/
install -m644 lib/lyaml/*.lua %{buildroot}%{lua_noarchdir}/lyaml/

%files
%{lua_archdir}/yaml.so
%dir %{lua_noarchdir}/lyaml
%{lua_noarchdir}/lyaml/*.lua

%changelog

