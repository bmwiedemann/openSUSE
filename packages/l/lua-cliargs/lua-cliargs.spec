#
# spec file for package lua-luacliargs
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define flavor @BUILD_FLAVOR@
%define mod_name lua_cliargs
%define upversion 3.0-2
Version:        3.02
Release:        0
Summary:        Command-line argument parsing module for Lua
License:        MIT
Group:          Development/Libraries/Other
Url:            https://github.com/amireh/lua_cliargs
Source:         https://github.com/amireh/lua_cliargs/archive/v%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
BuildRequires:  %{flavor}-devel
BuildArch:      noarch
Requires:       %{flavor}
%if "%{flavor}" == "lua53"
Provides:       lua-luacliargs = %{version}
Obsoletes:      lua-luacliargs < %{version}
%endif
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
%setup -q -n %{mod_name}-%{upversion}

%build
/bin/true

%install
install -v -D -m 0644 -p -t %{buildroot}%{lua_noarchdir} src/cliargs.lua
cp -v -r -p src/cliargs %{buildroot}%{lua_noarchdir}


%files
%dir %{lua_noarchdir}/cliargs
%{lua_noarchdir}/cliargs*

%changelog
