#
# spec file for package lua-penlight
#
# Copyright (c) 2020 SUSE LLC
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
%define mod_name penlight
%define lua_value  %(echo "%{flavor}" |sed -e 's:lua::')
%define with_docs 1

Version:        1.6.0
Release:        0
Summary:        Generally useful modules inspired by the Python standard libraries
License:        MIT
Group:          Development/Languages/Other
URL:            http://stevedonovan.github.com/Penlight
Source:         https://github.com/stevedonovan/Penlight/archive/%{version}.tar.gz#/Penlight-%{version}.tar.gz
# PATCH-FIX-UPSTREAM lua54.patch gh#Tieske/Penlight#320 mcepl@suse.com
# workaround hardcoded version of Lua 5.3.
Patch0:         lua54.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-ldoc
BuildRequires:  %{flavor}-luafilesystem
BuildRequires:  %{flavor}-markdown
Requires:       %{flavor}
Requires:       %{flavor}-luafilesystem
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description
A set of pure Lua libraries focusing on input data handling (such as
reading configuration files), functional programming (such as map,
reduce, placeholder expressions,etc), and OS path management. Much of
the functionality is inspired by the Python standard libraries.

%if 0%{?with_docs}
%package doc
Summary:        Documentation for %{name}
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description doc
Documentation for the package %{name}
%endif

%prep
%setup -q -n Penlight-%{version}
%autopatch -p1

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

%files doc
%doc docs

%changelog
