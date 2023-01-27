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
%define mod_name fluent
%define rock_version 0.2.0-0

Version:        0.2.0
Release:        0
Summary:        Lua implementation of Project Fluent
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/alerque/fluent-lua
Source:         %{mod_name}-lua-%{version}.tar.gz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-luarocks
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-cldr
BuildRequires:  %{flavor}-luaepnf
BuildRequires:  %{flavor}-penlight
%if %{with test}
BuildRequires:  %{flavor}-busted
%endif
Requires:       %{flavor}
Requires:       %{flavor}-cldr
Requires:       %{flavor}-luaepnf
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
A Lua implementation of Project Fluent, a localization paradigm designed
to unleash the entire expressive power of natural language translations.
Fluent is a family of localization specifications, implementations and
good practices developed by Mozilla who extracted parts of their 'l20n'
solution (used in Firefox and other apps) into a re-usable specification.

%prep
%autosetup -n %{mod_name}-lua-%{version}

%build
%luarocks_build "rockspecs/%{mod_name}-%{rock_version}.rockspec"

%install
%luarocks_install *.rock
luarocks --lua-version="%{lua_version}" --tree="%{buildroot}/usr/" \
 make --deps-mode=none --no-manifest "rockspecs/%{mod_name}-%{rock_version}.rockspec"

%if %{with test}
%check
busted
%endif

%files
%license %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc/LICENSE
%doc %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc
%{lua_noarchdir}/%{mod_name}
%{luarocks_treedir}/%{mod_name}

%changelog
