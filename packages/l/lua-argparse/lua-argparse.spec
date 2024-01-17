#
# spec file for package lua-argparse
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
%define flavor lua51
%bcond_without test
%else
%bcond_with test
%endif
%define mod_name argparse
%define upversion 0.7.0
Version:        0.7.0
Release:        0
Summary:        A feature-rich command-line argument parser
License:        MIT
Group:          Development/Libraries/Other
URL:            http://argparse.org/
Source:         https://github.com/luarocks/%{mod_name}/archive/%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
BuildRequires:  %{flavor}-devel
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" != "test"
BuildRequires:  lua-macros
%endif
%if "%{flavor}" == ""
Name:           lua-argparse
ExclusiveArch:  do_not_build
%else
%if %{with test}
Name:           %{flavor}-argparse-test
%else
Name:           %{flavor}-argparse
%endif
%endif
%if %{with test}
BuildRequires:  %{flavor}-argparse
BuildRequires:  %{flavor}-busted
BuildRequires:  %{flavor}-penlight
%endif

%description
Argparse supports positional arguments, options, flags, optional
arguments, subcommands and more. Argparse automatically generates usage,
help, and error messages, and can generate shell completion scripts.

%prep
%setup -q -n %{mod_name}-%{upversion}

%build
/bin/true

%install
%if ! %{with test}
install -v -D -m 0644 -t %{buildroot}%{lua_noarchdir} -p src/argparse.lua
%endif

%check
%if %{with test}
busted
%endif

%if ! %{with test}
%files
%license LICENSE
%doc CHANGELOG.md README.md
%{lua_noarchdir}/%{mod_name}*
%endif

%changelog
