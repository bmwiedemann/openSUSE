#
# spec file for package sile
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without  tests
%if 0%{?suse_version} < 1699
%define flavor lua51
%else
%define flavor luajit
%endif
Name:           sile
Version:        0.15.13
Release:        0
Summary:        Simon’s Improved Layout Engine
License:        MIT
URL:            https://sile-typesetter.org/
Source:         https://github.com/sile-typesetter/%{name}/releases/download/v%{version}/sile-%{version}.tar.zst#/%{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        sile-rpmlintrc
# PATCH-FIX-UPSTREAM no-gentium-plus.patch bsc#[0-9]+ mcepl@suse.com
# font Gentium Plus is since version 7.0.0 called only Gentium again
Patch0:         no-gentium-plus.patch

# Lua modules
# Required while lua51 is fully removed from Tumbleweed
#!BuildIgnore: lua51
BuildRequires:  luajit
BuildRequires:  %{flavor}-bit32
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luarocks
Requires:       %{flavor}-bit32
BuildRequires:  %{flavor}-cassowary
Requires:       %{flavor}-cassowary
Requires:       %{flavor}-cldr
BuildRequires:  %{flavor}-cliargs
Requires:       %{flavor}-cliargs
BuildRequires:  %{flavor}-compat-5.3
Requires:       %{flavor}-compat-5.3
BuildRequires:  %{flavor}-cosmo
Requires:       %{flavor}-cosmo
BuildRequires:  %{flavor}-luaexpat
Requires:       %{flavor}-luaexpat
BuildRequires:  %{flavor}-luafilesystem
Requires:       %{flavor}-luafilesystem
BuildRequires:  %{flavor}-fluent
Requires:       %{flavor}-fluent
BuildRequires:  %{flavor}-linenoise
Requires:       %{flavor}-linenoise
BuildRequires:  %{flavor}-loadkit
Requires:       %{flavor}-loadkit
Requires:       %{flavor}-lpeg
Requires:       %{flavor}-luaepnf
BuildRequires:  %{flavor}-luarepl
Requires:       %{flavor}-luarepl
BuildRequires:  %{flavor}-luautf8
Requires:       %{flavor}-luautf8
Requires:       %{flavor}-penlight
BuildRequires:  %{flavor}-luasec
Requires:       %{flavor}-luasec
Requires:       %{flavor}-luasocket
BuildRequires:  %{flavor}-vstruct
Requires:       %{flavor}-vstruct
BuildRequires:  %{flavor}-zlib
# Without this Requires, %{flavor}-zlib isn't counted as a dependency
Requires:       %{flavor}-zlib

# Other Dependencies
%if %{with tests}
BuildRequires:  poppler-tools
BuildRequires:  sil-gentium-fonts >= 7
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fontconfig-devel
Requires:       fontconfig
BuildRequires:  freetype2-devel
Requires:       freetype2
BuildRequires:  fdupes
BuildRequires:  gcc-objc
BuildRequires:  git-core
Requires:       git-core
BuildRequires:  glibc-devel
Requires:       glibc
# Harfbuzz's minimum version is now 6 https://github.com/sile-typesetter/sile/releases/tag/v0.14.8
BuildRequires:  harfbuzz-devel >= 6.0.0
BuildRequires:  jq
BuildRequires:  libicu-devel
Requires:       icu
BuildRequires:  libpng16-compat-devel
BuildRequires:  libtool
BuildRequires:  pkgconf-pkg-config
BuildRequires:  zlib-devel
# Default font for SILE
# Without this, you have to specify the font every time you write a new .sil
Recommends:     sil-gentium-fonts >= 7
# Default font for math package
Suggests:       libertinus-fonts
# Default font for tate enabled classes
Suggests:       noto-sans-cjk-fonts
# Default mono font
Suggests:       hack-fonts

# Rust build dependencies. We don't need cargo packaging.
# Sile has a flags we have to respect it
BuildRequires:  cargo
# For tar scm lol
BuildRequires:  zstd

%description
SILE is a typesetting system; its job is to produce beautiful printed documents.
Conceptually, SILE is similar to TeX—from which it borrows some concepts and even
syntax and algorithms—but the similarities end there. Rather than being a
derivative of the TeX family SILE is a new typesetting and layout engine written
from the ground up using modern technologies and borrowing some ideas from
graphical systems such as InDesign.

%package -n libtexpdf0
Summary:        A PDF library extracted from TeX's dvipdfmx
Group:          Productivity/Publishing
License:        GPL-2.0-or-later

%description -n libtexpdf0
A PDF library extracted from TeX's dvipdfmx. Used in software such as SILE.
This package contains the shared library for libtexpdf.

%package -n libtexpdf-devel
Summary:        Development files for libtexpdf
License:        GPL-2.0-or-later
Requires:       libtexpdf0 = %{version}

%description -n libtexpdf-devel
A PDF library extracted from TeX's dvipdfmx. Used in software such as SILE.
This package contains the development files for libtexpdf.

%package        bash-completion
Summary:        Bash Completion for %{name}
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
Requires:       sile
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%package        fish-completion
Summary:        Fish Completion for %{name}
Supplements:    (%{name} and fish)
Requires:       fish
Requires:       sile
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Supplements:    (%{name} and zsh)
Requires:       sile
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -p1 -a1

autoreconf --force --install

%build
# The macros uses this but we have to respect what upstream config.toml
# uses for the RUSTFLAGS
unset LIBSSH2_SYS_USE_PKG_CONFIG
export RUSTFLAGS=" -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2 -C incremental=false -C strip=none"
export CARGO_AUDITABLE=auditable
export CARGO_FEATURE_VENDORED=1
export LUA_INCLUDE="-I/usr/include/luajit-5_1-2.1"
export CFLAGS="%optflags $(pkg-config --cflags-only-I luajit)"
export CXXFLAGS="%optflags $(pkg-config --cflags-only-I luajit)"
%configure \
	--disable-static \
	--disable-embeded-resources \
	--with-system-lua-sources \
	--with-system-luarocks

%make_build all

%install
# The macros uses this but we have to respect what upstream config.toml
# uses for the RUSTFLAGS
unset LIBSSH2_SYS_USE_PKG_CONFIG
export RUSTFLAGS=" -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2 -C incremental=false -C strip=none"
export CARGO_AUDITABLE=auditable
export CARGO_FEATURE_VENDORED=1
export LUA_INCLUDE="$(pkg-config --cflags-only-I luajit)"
export CFLAGS="%optflags $(pkg-config --cflags-only-I luajit)"
export CXXFLAGS="%optflags $(pkg-config --cflags-only-I luajit)"
%make_install
rm %{buildroot}%{_libdir}/*.la
%fdupes %{buildroot}

%if %{with tests}
%check
make check
%endif

%ldconfig_scriptlets -n libtexpdf0
%ldconfig_scriptlets -n libtexpdf-devel

%files
%license LICENSE.md
%doc %{_datadir}/doc/sile/*
%dir %{_datadir}/doc/sile
%dir %{_datadir}/licenses/sile
%{_bindir}/sile
%{_bindir}/sile-lua
%{_datadir}/sile
%{_libdir}/sile
%{_mandir}/man1/sile.1%{?ext_man}
%{_mandir}/man1/sile-lua.1%{?ext_man}

%files -n libtexpdf0
%license %{_datadir}/licenses/libtexpdf/LICENSE
%dir %{_datadir}/licenses/libtexpdf
%{_libdir}/libtexpdf.so.0*

%files -n libtexpdf-devel
%{_includedir}/libtexpdf
%{_libdir}/libtexpdf.so

%files bash-completion
%license LICENSE.md
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%license LICENSE.md
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%license LICENSE.md
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
