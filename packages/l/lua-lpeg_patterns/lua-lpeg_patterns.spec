#
# spec file for package lua-lpeg_patterns
#
# Copyright (c) 2020 SUSE LLC
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
%define mod_name lpeg_patterns
%define upversion 0.5
Version:        0.5
Release:        0
Summary:        Collection of LPEG patterns
License:        MIT
URL:            https://github.com/daurnimator/lpeg_patterns
Source:         https://github.com/daurnimator/lpeg_patterns/archive/v%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
BuildRequires:  %{flavor}-lpeg
BuildRequires:  %{flavor}-busted
BuildRequires:  lua-macros
Requires:       %{flavor}-lpeg
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-lpeg_patterns
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-lpeg_patterns
%endif

%description
A collection of LPEG patterns

Use cases:
 * Strict validation of user input
 * Searching free-form input


%prep
%autosetup -p1 -n %{mod_name}-%{upversion}

%build
/bin/true

%install
mkdir -p %{buildroot}%{lua_noarchdir}/lpeg_patterns
cp -v -r -p lpeg_patterns/* %{buildroot}%{lua_noarchdir}/lpeg_patterns/

%check
busted -v

%files
%license LICENSE.md
%doc README.md NEWS
%dir %{lua_noarchdir}/lpeg_patterns
%{lua_noarchdir}/lpeg_patterns*

%changelog
