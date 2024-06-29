#
# spec file for package sile
#
# Copyright (c) 2024 SUSE LLC
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
Name:           sile
Version:        0.15.4
Release:        0
Summary:        Simon’s Improved Layout Engine
License:        MIT
URL:            https://sile-typesetter.org/
Source0:        sile-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        sile-rpmlintrc
Source3:        LICENSE

# Lua modules
BuildRequires:  luajit
BuildRequires:  lua51-bit32
BuildRequires:  luajit-devel
Requires:       lua51-bit32
BuildRequires:  lua51-cassowary
Requires:       lua51-cassowary
Requires:       lua51-cldr
BuildRequires:  lua51-cliargs
Requires:       lua51-cliargs
BuildRequires:  lua51-compat-5.3
Requires:       lua51-compat-5.3
BuildRequires:  lua51-cosmo
Requires:       lua51-cosmo
BuildRequires:  lua51-luaexpat
Requires:       lua51-luaexpat
BuildRequires:  lua51-luafilesystem
Requires:       lua51-luafilesystem
BuildRequires:  lua51-fluent
Requires:       lua51-fluent
BuildRequires:  lua51-linenoise
Requires:       lua51-linenoise
BuildRequires:  lua51-loadkit
Requires:       lua51-loadkit
Requires:       lua51-lpeg
Requires:       lua51-luaepnf
BuildRequires:  lua51-luarepl
Requires:       lua51-luarepl
BuildRequires:  lua51-luautf8
Requires:       lua51-luautf8
Requires:       lua51-penlight
BuildRequires:  lua51-luasec
Requires:       lua51-luasec
Requires:       lua51-luasocket
BuildRequires:  lua51-vstruct
Requires:       lua51-vstruct
BuildRequires:  lua51-zlib
# Without this Requires, lua51-zlib isn't counted as a dependency
Requires:       lua51-zlib

# Other Dependencies
%if %{with tests}
BuildRequires:  poppler-tools
BuildRequires:  sil-gentium-fonts
%endif
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
Recommends:     sil-gentium-fonts
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
cp %{SOURCE3} .

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
%license LICENSE
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
