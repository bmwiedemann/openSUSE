#
# spec file for package lua-mediator_lua
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
%define mod_name mediator_lua
%define upversion 1.1.2-0
Version:        1.120
Release:        0
Summary:        Command-line argument parsing module for Lua
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/Olivine-Labs/mediator_lua
Source:         https://github.com/Olivine-Labs/mediator_lua/archive/v%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
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
This module adds support for accepting CLI arguments easily using multiple
notations and argument types.

mediator_lua allows you to define required, optional, and flag arguments.

%prep
%setup -q -n %{mod_name}-%{upversion}

%build
/bin/true

%install
install -v -D -m 0644 -p -t %{buildroot}%{lua_noarchdir} src/mediator.lua

%files
%{lua_noarchdir}/mediator*

%changelog
