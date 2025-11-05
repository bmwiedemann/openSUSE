#
# spec file for package lua-cffi
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%define mod_name cffi-lua
Version:        0.2.3+git.1748465608.9f2acc9
Release:        0
Summary:        A portable C FFI for Lua 5.1+
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/q66/cffi-lua
Source:         %{mod_name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM 0001-Corrects-1st-example-in-introduction.md.patch gh#q66/cffi-lua!38 mcepl@suse.com
# fix one typo in introduction.md
Patch0:         0001-Corrects-1st-example-in-introduction.md.patch
# PATCH-FIX-UPSTREAM 0002-docs-fixed-the-second-example-in-introduction.md.patch mcepl@suse.com
# fix second typo in introduction.md
Patch1:         0002-docs-fixed-the-second-example-in-introduction.md.patch
# PATCH-FIX-UPSTREAM remove-bogus-luajit.patch gh#q66/cffi-lua#63 mcepl@suse.com
# fix tests for LuaJIT
Patch2:         remove-bogus-luajit.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-compat-5.3
BuildRequires:  lua-macros
BuildRequires:  meson
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libffi)
Requires:       %{flavor}
Requires: 	%{flavor}-compat-5.3
# gh#q66/cffi-lua#59
ExcludeArch:    %{ix86} armv6l armv6hl armv7l armv7hl
%lua_provides
%lua_provides -e
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
Recommends:     %{flavor}-%{mod_name}-doc
%endif

%description
This is a portable C FFI for Lua, based on `libffi` and aiming
to be mostly compatible with LuaJIT FFI, but written from
scratch. Compatibility is preserved where reasonable, but not
where not easily implementable (e.g. the parser extensions for
64-bit `cdata` and so on). Thanks to `libffi`, it works on many
operating systems and CPU architectures. The `cffi-lua` codebase
itself does not contain any non-portable code (with the exception
of things such as Windows calling convention handling on x86, and
some adjustments for big endian architectures). Some effort was
also taken to ensure compatibility with custom Lua configurations
(e.g. with changed numeric type representations), though this is
not tested or guaranteed to work (patches welcome if broken).

Unlike LuaJIT's `ffi` module or other efforts such as `luaffifb`,
it works with every common version of the reference Lua
implementation (currently 5.1, 5.2, 5.3 and 5.4, 5.0 could be
supported but wasn't considered worth it) as well as compatible
non-reference ones (like LuaJIT). Functionality from newer Lua
versions is also supported, when used with that version (e.g.
with 5.3+ you will get seamless integer and bit-op support, with
5.4 you will get metatype support for to-be-closed variables, and
so on).

Since it's written from scratch, having 1:1 bug-for-bug C parser
compatibility is a non-goal. The parser is meant to comply with
C11, plus a number of extensions from GCC, MSVC and C++ (where it
doesn't conflict with C).

The project was started because there isn't any FFI for standard
Lua that's as user friendly as LuaJIT's and doesn't have
portability issues.

%package doc
Summary:        Documentation for %{flavor}-%{mod_name}
Group:          Development/Languages/Other
BuildArch:      noarch

%description doc
This subpackage contains documentation for %{flavor}-%{mod_name}.

%prep
%autosetup -p1 -n %{mod_name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING.md
%{lua_archdir}/cffi.so

%files doc
%doc docs/*
%license COPYING.md
%doc README.md STATUS.md CHANGELOG.md

%changelog
