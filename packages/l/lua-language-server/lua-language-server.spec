#
# spec file for package lua-language-server
#
# Copyright (c) 2023 SUSE LLC
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
Version:        3.6.7
Release:        0
Summary:        Lua Language Server coded by Lua
License:        MIT
URL:            https://github.com/sumneko/lua-language-server
# Checkout from git is required because of gh#sumneko/lua-language-server#878
# Source0:        %%{name}-%%{version}.tar.gz
Source0:        https://github.com/sumneko/%{name}/releases/download/%{version}/%{name}-%{version}-submodules.zip
Source1:        https://github.com/sumneko/%{name}/archive/%{version}.tar.gz
Source2:        lua-lsp-launcher.sh
Source3:        README.suse-maint.md
# PATCH-FIX-UPSTREAM time_includes.patch gh#sumneko/lua-language-server#1377 mcepl@suse.com
# Add missing #include
# Patch0:         time_includes.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  unzip
ExcludeArch:    s390x ppc64le ppc64

%description
This package provides a Language Server Protocol (LSP) implementation for Lua.

%prep
%autosetup -c

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

ninja -C 3rd/luamake -f compile/ninja/linux.ninja
./3rd/luamake/luamake all

%install
install -d -m 0755 %{buildroot}%{_libexecdir}/%{name}
cp -av bin/* %{buildroot}%{_libexecdir}/%{name}

install -d -m 0755 %{buildroot}%{_datadir}/%{name}
cp -av \
    debugger.lua \
    main.lua \
    locale \
    script \
    meta \
    %{buildroot}%{_datadir}/%{name}/

install -d -m 0755 %{buildroot}%{_bindir}
sed -e 's#@LIBEXECDIR@#%{_libexecdir}#' %{SOURCE2} > %{buildroot}%{_bindir}/%{name}
chmod 0755 %{buildroot}%{_bindir}/%{name}

%fdupes %{buildroot}%{_libexecdir}/%{name} %{buildroot}%{_datadir}/%{name}

%check
./3rd/luamake/luamake bee-test unit-test

%files
%license LICENSE
%doc README.md changelog.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/%{name}/

%changelog
