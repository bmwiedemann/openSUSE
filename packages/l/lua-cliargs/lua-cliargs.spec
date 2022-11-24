#
# spec file for package lua-cliargs
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
%define mod_name luacliargs
%define rname lua_cliargs
%define upversion 3.0-2
Version:        3.02
Release:        0
Summary:        Command-line argument parsing module for Lua
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/amireh/lua_cliargs
Source:         https://github.com/amireh/lua_cliargs/archive/v%{upversion}.tar.gz#/%{rname}-%{upversion}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-cliargs
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-cliargs
%endif

%description
This module adds support for accepting CLI arguments easily using multiple
notations and argument types.

cliargs allows you to define required, optional, and flag arguments.

%prep
%setup -q -n %{rname}-%{upversion}

%build
/bin/true

%install
install -v -D -m 0644 -p -t %{buildroot}%{lua_noarchdir} src/cliargs.lua
cp -v -r -p src/cliargs %{buildroot}%{lua_noarchdir}

%files
%dir %{lua_noarchdir}/cliargs
%{lua_noarchdir}/cliargs*

%changelog
