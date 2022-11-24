#
# spec file for package lua-alt-getopt
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
%define mod_name alt-getopt
%define rname lua-alt-getopt
%define upversion 0.8.0
Version:        0.8.1
Release:        0
Summary:        Process application arguments the same way as getopt_long
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/cheusov/lua-alt-getopt
Source:         https://github.com/cheusov/%{rname}/archive/%{upversion}.tar.gz#/%{rname}-%{upversion}.tar.gz
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
alt-getopt is a module for Lua programming language for
processing application's arguments the same way BSD/GNU
getopt_long(3) functions do.  The main goal is compatibility
with SUS "Utility Syntax Guidelines" guidelines 3-13.

%prep
%setup -q -n %{rname}-%{upversion}

%build
/bin/true

%install
install -v -D -m 0644 -t %{buildroot}%{lua_noarchdir} -p alt_getopt.lua

%check
ln -srf ./alt_getopt.lua ./tests
cd ./tests && ./test.sh

%files
%license LICENSE
%doc README NEWS
%{lua_noarchdir}/alt_getopt.lua

%changelog
