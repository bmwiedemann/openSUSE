#
# spec file for package lua-penlight
#
# Copyright (c) 2024 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}
%define mod_name penlight
%define rname Penlight
%ifluadefault
%define with_main 1
%endif
Version:        1.14.0
Release:        0
Summary:        Generally useful modules inspired by the Python standard libraries
License:        MIT
Group:          Development/Languages/Other
URL:            https://lunarmodules.github.io/Penlight/
Source0:        https://github.com/lunarmodules/Penlight/archive/%{version}/%{rname}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-ldoc
BuildRequires:  %{flavor}-luafilesystem
BuildRequires:  %{flavor}-markdown
BuildRequires:  lua-macros
Requires:       %{flavor}
Requires:       %{flavor}-luafilesystem
Recommends:     lua-%{mod_name}-doc
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
A set of pure Lua libraries focusing on input data handling (such as
reading configuration files), functional programming (such as map,
reduce, placeholder expressions,etc), and OS path management. Much of
the functionality is inspired by the Python standard libraries.

%if 0%{?with_main}
%package -n lua-%{mod_name}-doc
Summary:        Documentation for lua-%{mod_name}
Group:          Development/Languages/Other

%description -n lua-%{mod_name}-doc
Documentation for the package lua-%{mod_name}
%endif

%prep
%autosetup -n %{rname}-%{version} -p1

%build

%install
mkdir -p %{buildroot}%{lua_noarchdir}
cp -av lua/pl %{buildroot}%{lua_noarchdir}

# fix scripts
chmod -x %{buildroot}%{lua_noarchdir}/pl/dir.lua

# build and install README etc.
lua%{lua_version} %{lua_noarchdir}/markdown.lua *.md

%check
LUA_PATH="%{buildroot}%{lua_noarchdir}/?/init.lua;%{buildroot}%{lua_noarchdir}/?.lua;;" \
lua%{lua_version} run.lua tests

%files
%license LICENSE.md
%doc README.md *.html
%{lua_noarchdir}/pl
# Add bash/zsh-completion files
# from completions/bash/penlight.bash penlight

%if 0%{?with_main}
%files -n lua-%{mod_name}-doc
%doc docs
%endif

%changelog
