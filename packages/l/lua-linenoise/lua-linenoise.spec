#
# spec file for package lua-linenoise
#
# Copyright (c) 2024 SUSE LLC
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
%define mod_name linenoise
%define rock_version 0.9-1
%ifarch %{ix86}
 %define luarock_arch x86
%else
 %ifarch s390x
  %define luarock_arch s390
 %else
  %define luarock_arch %{_arch}
 %endif
%endif
Version:        0.9
Release:        0
Summary:        Lua binding for the linenoise command line library
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/hoelzro/lua-linenoise
Source:         lua-linenoise-%{version}.tar.zst
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luarocks
BuildRequires:  lua-macros
BuildRequires:  zstd
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
Linenoise (https://github.com/antirez/linenoise) is a delightfully
simple command line library. This Lua module is simply a binding for it.

The main Linenoise upstream has stagnated a bit, so this binding tracks
https://github.com/yhirose/linenoise/tree/utf8-support, which includes
things like UTF-8 support and ANSI terminal escape sequence detection.

%prep
%autosetup -n lua-linenoise-%{version}

%build
%luarocks_build "%{mod_name}-%{rock_version}.rockspec"

%install
%luarocks_install "%{mod_name}-%{rock_version}.linux-%{luarock_arch}.rock"

%check

%files
%doc README.md Changes __rocktree/*
%license COPYING
%{lua_archdir}

%changelog
