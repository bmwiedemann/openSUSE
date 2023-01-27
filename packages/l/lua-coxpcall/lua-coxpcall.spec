#
# spec file for package lua-coxpcall
#
# Copyright (c) 2021 SUSE LLC
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
%define mod_name coxpcall
%define upversion 1_17_0
Version:        1.17.0
Release:        0
Summary:        Coroutine safe xpcall and pcall
License:        MIT
URL:            http://www.keplerproject.org/coxpcall/
Source:         https://github.com/keplerproject/%{mod_name}/archive/v%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luasocket
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-coxpcall
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-coxpcall
%endif

%description
Encapsulates the protected calls with a coroutine based loop, so errors
can be handled without the usual Lua 5.x pcall/xpcall issues with
coroutines yielding inside the call to pcall or xpcall.

%prep
%setup -q -n %{mod_name}-%{upversion}

%build
/bin/true

%install
%make_install LUA_DIR=%{lua_noarchdir}

%check
lua tests/test.lua

%files
%license doc/license.html
%doc README.md doc/{coxpcall.png,doc.css,index.html}
%{lua_noarchdir}/%{mod_name}*

%changelog
