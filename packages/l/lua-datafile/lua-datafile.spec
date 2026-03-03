#
# spec file for package lua-datafile
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
%define mod_name datafile
Version:        0.11
Release:        0
Summary:        library for handling paths when loading data files
License:        MIT
URL:            https://github.com/hishamhm/datafile
Source:         https://github.com/hishamhm/datafile/archive/refs/tags/v%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
A Lua library for handling paths when loading data files

Example usage:

    local datafile = require("datafile")

    local my_template = datafile.open("myapp/my_template.txt", "r")

This will try to find and open myapp/my_template.txt in a series of
locations, based on the "opener" plugins found at the datafile.openers
sequence, which contain opener functions loaded from the
datafile.openers.* modules (you may modify the datafile.openers sequence
in an analog fashion to the package.loaders/package.searchers sequence
from Lua).

%prep
%autosetup -p1 -n %{mod_name}-%{version}

%build
:

%install
install -v -D -m 0644 -p -t %{buildroot}%{lua_noarchdir} datafile.lua
cp -r -p datafile/ %{buildroot}%{lua_noarchdir}

%check
export LUA_PATH="%{buildroot}%{lua_noarchdir}/?.lua;test/?.lua;;"
%{lua_exec} test/test_script.lua

%files
%license LICENSE
%doc README.md
%{lua_noarchdir}/datafile.lua
%{lua_noarchdir}/datafile

%changelog
