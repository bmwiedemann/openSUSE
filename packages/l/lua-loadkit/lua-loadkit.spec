#
# spec file for package lua-loadkit
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
%if "%{flavor}" == "test"
%define flavor lua54
%bcond_without test
%else
%bcond_with test
%endif
%define mod_name loadkit
Version:        1.1.0
Release:        0
Summary:        Loadkit allows you to load arbitrary files within the Lua package path
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/leafo/loadkit
Source:         https://github.com/leafo/%{mod_name}/archive/v%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
# BuildRequires:  %{flavor}-moonscript
BuildRequires:  lua-macros
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if %{with test}
BuildRequires:  %{flavor}-busted
%endif
%if "%{flavor}" == ""
Name:           lua-loadkit
ExclusiveArch:  do_not_build
%else
%if %{with test}
Name:           %{flavor}-loadkit-test
%else
Name:           %{flavor}-loadkit
%endif
%endif

%description
Loadkit lets you register new file extension handlers that
can be opened with require, or you can just search for files
of any extension using the current search path.

%prep
%setup -q -n %{mod_name}-%{version}

%build
# Use prebuilt loadkit.lua to avoid build cycle.
# moonc loadkit.moon

%install
%if ! %{with test}
install -v -D -m 0644 -t %{buildroot}%{lua_noarchdir} -p loadkit.lua
%endif

%check
%if %{with test}
busted
%endif

%if ! %{with test}
%files
%doc README.md
%{lua_noarchdir}/%{mod_name}*
%endif

%changelog
