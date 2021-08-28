# spec file for package lua-fennel
#
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
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/

Name:          lua-fennel
Version:       0.10.0
Release:       0
Summary:       Lisp dialect that compiles to Lua
License:       MIT
Group:         Development/Languages/Lua
URL:           https://fennel-lang.org/
Source0:       https://git.sr.ht/~technomancy/fennel/archive/%{version}.tar.gz
BuildRequires: lua
BuildArch:     noarch

%description
Fennel is a lisp that compiles to Lua. It aims to be easy to use,
expressive, and has almost zero overhead compared to handwritten Lua.

• Full Lua compatibility - You can use any function or library from Lua.
• Zero overhead - Compiled code should be just as or more efficient than
hand-written Lua.
• Compile-time macros - Ship compiled code with no runtime dependency
on Fennel.
• Embeddable - Fennel is a one-file library as well as an executable.
Embed it in other programs to support runtime extensibility and
interactive development.

%prep
%autosetup -p1 -n fennel-%{version}

%build
%make_build fennel

%check
make test

%install
mkdir -p %{buildroot}%{_bindir}
sed -i s:/usr/bin/env\ lua:/usr/bin/lua: fennel
install -m 755 fennel %{buildroot}%{_bindir}

%files
%doc README.md api.md changelog.md reference.md tutorial.md
%license LICENSE
%{_bindir}/fennel

%changelog
