#
# spec file for package lua-language-server
#
# Copyright (c) 2021 SUSE LLC
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


%define pkg_name lua-language-server

Name:           lua-language-server
Version:        2.5.6
Release:        0
Summary:        Lua Language Server coded by Lua
License:        MIT
URL:            https://github.com/sumneko/lua-language-server
# Checkout from git is required because of gh#sumneko/lua-language-server#878
Source0:        %{name}-%{version}.tar.gz
Source1:        lua-lsp-launcher.sh
Source2:        README.suse-maint.md
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja

%description
This package provides a Language Server Protocol (LSP) implementation for Lua.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

ninja -C 3rd/luamake -f compile/ninja/linux.ninja
./3rd/luamake/luamake rebuild

%install
install -d -m 0755 %{buildroot}%{_libdir}/%{name}
cp -av bin/* %{buildroot}%{_libdir}/%{name}

install -d -m 0755 %{buildroot}%{_datadir}/%{name}
cp -av \
    debugger.lua \
    main.lua \
    locale \
    script \
    meta \
    %{buildroot}%{_datadir}/%{name}/

install -d -m 0755 %{buildroot}%{_bindir}
sed -e 's#@LIBDIR@#%{_libdir}#' %{SOURCE1} > %{buildroot}%{_bindir}/%{name}
chmod 0755 %{buildroot}%{_bindir}/%{name}

%fdupes %{buildroot}%{_libdir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/

%changelog
