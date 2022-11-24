#
# spec file for package lua-luassert
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
%define mod_name luassert
%define upversion 1.7.11
Version:        1.7.11
Release:        0
Summary:        Lua Assertions Extension
License:        MIT
URL:            https://github.com/Olivine-Labs/luassert
Source:         https://github.com/Olivine-Labs/luassert/archive/v%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-say
BuildRequires:  lua-macros
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-luassert
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-luassert
%endif

%description
Adds a framework that allows registering new assertions without
compromising builtin assertion functionality.

%prep
%setup -q -n %{mod_name}-%{upversion}
sed -i -e 's/\r$//' README.md

%build
/bin/true

%install
mkdir -p %{buildroot}%{lua_noarchdir}/luassert
cp -v -r -p src/* %{buildroot}%{lua_noarchdir}/luassert

%check
# requires busted
/bin/true
# spec:
# assertions_spec.lua  helper.lua     mocks_spec.lua   spies_spec.lua
# stub_spec.lua
# formatters_spec.lua  matchers_spec.lua  output_spec.lua  state_spec.lua

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%dir %{lua_noarchdir}/luassert
%{lua_noarchdir}/luassert*

%changelog
