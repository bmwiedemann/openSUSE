#
# spec file for package lua-say
#
# Copyright (c) 2023 SUSE LLC
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

# The luarocks_install macro is replaced by the install-rock.sh script

%define flavor @BUILD_FLAVOR@
%if "%{flavor}" == "test"
%define flavor lua54
%bcond_without test
%else
%bcond_with test
%endif
%define mod_name say
Version:        1.4.1
Release:        0
Summary:        Lua string hashing library, useful for internationalization
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/lunarmodules/say
Source:         https://github.com/lunarmodules/say/archive/v%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luarocks
BuildRequires:  lua-macros
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-say
ExclusiveArch:  do_not_build
%else
%if %{with test}
Name:           %{flavor}-say-test
%else
Name:           %{flavor}-say
%endif
%endif
%if %{with test}
BuildRequires:  %{flavor}-say
BuildRequires:  %{flavor}-busted
%endif

%description
Useful for internationalization.

%prep
%autosetup -p1 -n %{mod_name}-%{version}

%build
%luarocks_build

%install
%if %{without test}
%luarocks_install ./%{mod_name}-*.rock
%endif

%check
%if %{with test}
busted
%endif

%if %{without test}
%files
%license LICENSE
# Nothing useful in __rocktree/
%doc README.md CONTRIBUTING.md
%{lua_noarchdir}/say
%endif

%changelog
