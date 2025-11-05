#
# spec file for package lua-lua-slaxml
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
%define mod_name slaxml
Version:        0.7+git20230101.756ffad
Release:        0
Summary:        SAX-like streaming XML parser for Lua 
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/Phrogz/SLAXML
Source:         lua-slaxml-%{version}.tar.xz
# PATCH-FIX-UPSTREAM fix_tests.patch gh#Phrogz/SLAXML!22 mcepl@suse.com
# unescape() function was too lenient
Patch0:         fix_tests.patch
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildArch:      noarch
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
SLAXML is a pure-Lua SAX-like streaming XML parser. It is more
robust than many (simpler) pattern-based parsers that exist
(such as mine), properly supporting code like
<expr test="5 > 7" />, CDATA nodes, comments, namespaces, and
processing instructions.

It is currently not a truly valid XML parser, however, as
it allows certain XML that is syntactically-invalid (not
well-formed) to be parsed without reporting an error.

%prep
%setup -q -n lua-slaxml-%{version}
find . -name \*.lua -exec sed -i 's/\r/\n/g; s/\n$//' '{}' +
%autopatch -p1

%build

%install
install -D -m 0644 -t %{buildroot}%{lua_noarchdir} slaxml.lua slaxdom.lua

%check
cd test
lua test.lua

%files
%license LICENSE.txt
%{lua_noarchdir}/slax*.lua

%changelog
