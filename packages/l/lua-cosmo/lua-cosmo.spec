#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
%define mod_name cosmo
%define rock_version 16.06.04-1
Version:        16.06.04
Release:        0
Summary:        A “safe templates” engine for Lua
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/mascarenhas/cosmo
Source:         cosmo-%{version}.tar.xz
Patch:          fix_test.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-lpeg
BuildRequires:  %{flavor}-luarocks
BuildRequires:  lua-macros
Requires:       %{flavor}
Requires:       %{flavor}-lpeg
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
BuildArch:      noarch

%description
Cosmo is a "safe templates" engine.  It allows you to fill nested
templates, providing many of the advantages of Turing-complete template
engines, without the downside of allowing arbitrary code in the templates.

%prep
%autosetup -p1 -n %{mod_name}-%{version}

sed -i -e '/lpeg >=/d' "rockspec/%{mod_name}-%{rock_version}.rockspec"

%build
%luarocks_build "rockspec/%{mod_name}-%{rock_version}.rockspec"

%install
%luarocks_install *.rock

%check
cd tests
lua test_cosmo.lua

%files
%license %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc/cosmo.md
%docdir %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc
%{lua_noarchdir}
%{luarocks_treedir}/%{mod_name}

%changelog
