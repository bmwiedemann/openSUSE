#
# spec file for package lua-fennel
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2020 Fabio Pesari
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


Name:           lua-fennel
Version:        1.6.0
Release:        0
Summary:        Lisp dialect that compiles to Lua
License:        MIT
# FIXME: use correct group or remove it, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          Development/Languages/Lua
URL:            https://fennel-lang.org/
Source0:        https://git.sr.ht/~technomancy/fennel/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  lua
BuildRequires:  lua-macros
BuildArch:      noarch

%description
Fennel is a lisp that compiles to Lua. Features include:

• Full Lua compatibility - You can use any function or library from
  Lua.
• Zero overhead - Compiled code should be just as or more efficient
  than hand-written Lua.
• Compile-time macros - Ship compiled code with no runtime
  dependency on Fennel.
• Embeddable - Fennel is a one-file library as well as an
  executable.
  Embed it in other programs to support runtime extensibility and
  interactive development.

%prep
%autosetup -p1 -n fennel-%{version}

%build
%make_build %{?_make_output_sync} PREFIX=%{_prefix} LUA="lua%{lua_version}" fennel
sed -i -e 's@#!%{_bindir}/env lua$@#!%{_bindir}/lua@' fennel

%install
%make_install %{?_make_output_sync} PREFIX=%{_prefix} install

%check
%make_build %{?_make_output_sync} test

%files
%doc README.md api.md changelog.md reference.md tutorial.md
%license LICENSE
%{_bindir}/fennel
%{lua_noarchdir}/fennel.lua
%{_mandir}/man*/fennel*%{?ext_man}

%changelog
