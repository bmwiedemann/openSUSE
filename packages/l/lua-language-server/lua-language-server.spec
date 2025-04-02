#
# spec file for package lua-language-server
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2021 Andreas Schneider <asn@cryptomilk.org>
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


Name:           lua-language-server
Version:        3.13.9
Release:        0
Summary:        Lua Language Server coded by Lua
License:        MIT
URL:            https://github.com/LuaLS/lua-language-server
Source0:        %{name}-%{version}.tar.gz
Source1:        lua-lsp-launcher.sh
Source99:       README.suse-maint.md
BuildRequires:  c++_compiler
BuildRequires:  ninja

%description
This package provides a Language Server Protocol (LSP) implementation for Lua.

%prep
%autosetup -p1
install -m 644 %{SOURCE99} .

%build
export CXXFLAGS="%{optflags}"

ninja -C 3rd/luamake -f compile/ninja/linux.ninja
./3rd/luamake/luamake all

%install
install -Dm0755 bin/%{name} %{buildroot}%{_libexecdir}/%{name}/%{name}
install -Dm0644 bin/main.lua %{buildroot}%{_libexecdir}/%{name}/main.lua

install -d %{buildroot}%{_datadir}/%{name}
cp -av \
    debugger.lua \
    main.lua \
    locale \
    script \
    meta \
    %{buildroot}%{_datadir}/%{name}/

install -d %{buildroot}%{_bindir}
sed -e 's#@LIBEXECDIR@#%{_libexecdir}#' %{SOURCE1} > %{buildroot}%{_bindir}/%{name}
chmod 0755 %{buildroot}%{_bindir}/%{name}

%ifarch x86_64
#tests are very flaky on non x86_64
%check
./3rd/luamake/luamake unit-test
%endif

%files
%license LICENSE
%doc README.md changelog.md README.suse-maint.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/%{name}

%changelog
