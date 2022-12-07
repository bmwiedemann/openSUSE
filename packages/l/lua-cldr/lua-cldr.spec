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
%define mod_name cldr
%define rock_version dev-0

Version:        0.3.0
Release:        0
Summary:        Unicode CLDR data and Lua interface
License:        MIT AND Unicode-TOU
Group:          Development/Languages/Other
URL:            https://github.com/alerque/cldr-lua
Source0:        %{mod_name}-lua-%{version}.tar.xz
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luarocks
BuildRequires:  %{flavor}-penlight
%lua_provides
Requires:       %{flavor}
Requires:       %{flavor}-penlight
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
BuildArch:      noarch

%description
Unicode CLDR (Common Locale Data Repository) data and Lua interface.
The Unicode CLDR provides key building blocks for software to support
the world's languages, with the largest and most extensive standard
repository of locale data available.

%prep
%autosetup -n %{mod_name}-lua-%{version}

%build
%luarocks_build "%{mod_name}-%{rock_version}.rockspec"

%install
%luarocks_install *.rock

%files
%license %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc/LICENSE
%license %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc/LICENSE-Unicode
%docdir %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc
%{lua_noarchdir}/%{mod_name}
%{luarocks_treedir}/%{mod_name}

%changelog
