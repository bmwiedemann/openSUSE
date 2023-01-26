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


%define flavor @BUILD_FLAVOR@
%define mod_name luaepnf
%define rock_version scm-0

Version:        0.3+git19
Release:        0
Summary:        Extended PEG Notation Format (easy grammars for LPeg)
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/siffiejoe/lua-luaepnf
Source:         lua-%{mod_name}-%{version}.tar.xz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-luarocks
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-lpeg
%lua_provides
Requires:       %{flavor}
Requires:       %{flavor}-lpeg
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
BuildArch:      noarch

%description
The LPeg library is a powerful tool to parse text and extract parts of
it using captures. It even provides grammars, which can be used to
parse non-regular languages, but the complexer the language gets, the
more difficult error handling and keeping track of captured information
becomes. luaepnf enhances usage of LPeg grammars by building an abstract
syntax tree (AST) for the input and providing tools for error reporting,
as well as offering syntax sugar and shortcuts for accessing LPeg's features.

%prep
%autosetup -n lua-%{mod_name}-%{version}

%build
%luarocks_build "%{mod_name}-%{rock_version}.rockspec"

%install
%luarocks_install *.rock

%check
cd tests
for t in *.lua; do lua $t; done

%files
%license %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc/readme.txt
%docdir %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc
%{lua_noarchdir}/epnf.lua
%{luarocks_treedir}/%{mod_name}

%changelog
