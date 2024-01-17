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
%define mod_name vstruct
%define rock_version 2.1.1-1

Version:        2.1.1+git2
Release:        0
Summary:        Lua library to manipulate binary data
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/ToxicFrog/vstruct
Source:         %{mod_name}-%{version}.tar.xz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-luarocks
BuildRequires:  %{flavor}-devel
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
BuildArch:      noarch

%description
A Lua library for packing and unpacking binary data, supporting arbitrary
(byte-aligned) widths, named fields, and repetition.

%prep
%autosetup -n %{mod_name}-%{version}

%build
%luarocks_build "%{mod_name}-%{rock_version}.rockspec"

%install
%luarocks_install *.rock

%files
%{lua_noarchdir}/%{mod_name}
%{luarocks_treedir}/%{mod_name}
%docdir %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc
%license %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc/COPYING

%changelog
