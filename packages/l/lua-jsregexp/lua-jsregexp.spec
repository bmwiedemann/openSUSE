#
# spec file
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


%define flavor @BUILD_FLAVOR@
%define mod_name jsregexp
Version:        0.1.0
Release:        0
Summary:        JavaScript regular expressions for Lua
License:        MIT
URL:            https://github.com/kmarius/jsregexp
Source:         https://github.com/kmarius/jsregexp/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
Provides:       %{flavor}-jsregexp = %{version}
Obsoletes:      %{flavor}-jsregexp < %{version}
%endif

%description
Provides ECMAScript regular expressions for Lua 5.1, 5.2, 5.3,
5.4 and LuaJit. Uses libregexp from Fabrice Bellard's QuickJS.

%prep
%setup -q -n jsregexp-%{version}

# Set our cflags
sed -i \
    -e '/^INCLUDE_DIR =/s:-I.*$:-I %{lua_incdir}:' \
    -e 's: -O2: %{optflags}:g' \
    Makefile

%build
make %{?_make_output_sync}

%install

mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{lua_archdir}
mkdir -p %{buildroot}%{lua_noarchdir}

install jsregexp.so %{buildroot}%{lua_archdir}

%check
%{_bindir}/lua test.lua

%files
%license LICENSE
%doc README.md
%{lua_archdir}/jsregexp.so

%changelog
