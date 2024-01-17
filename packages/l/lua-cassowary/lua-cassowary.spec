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

%bcond_without test
%define flavor @BUILD_FLAVOR@
%define mod_name cassowary
%define rock_version 2.3.2-1
Version:        2.3.2
Release:        0
Summary:        A Lua port of the cassowary constraint solver engine
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/sile-typesetter/cassowary.lua
Source:         cassowary.lua-%{version}.tar.xz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-penlight
BuildRequires:  %{flavor}-luarocks
BuildRequires:  %{flavor}-devel
%if %{with test}
BuildRequires:  %{flavor}-busted
%endif
Requires:       %{flavor}
Requires:       %{flavor}-penlight
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
BuildArch:      noarch

%description
This is a Lua port of the cassowary constraint solving toolkit.
It allows you to use Lua to solve algebraic equations and inequalities
and find the values of unknown variables which satisfy those inequalities.

%prep
%autosetup -n %{mod_name}.lua-%{version}

%build
%luarocks_build "rockspecs/%{mod_name}-%{rock_version}.rockspec"

%install
%luarocks_install *.rock


%if %{with test}
%check
busted
%endif

%files
%{lua_noarchdir}/%{mod_name}
%{luarocks_treedir}/%{mod_name}
%docdir %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc
%license %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc/LICENSE

%changelog
