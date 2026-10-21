#
# spec file for package naev
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


Name:           naev
Version:        0.13.5
Release:        0
Summary:        2D action RPG space game
License:        GPL-3.0-only AND MPL-2.0
URL:            https://naev.org/
Source0:        https://codeberg.org/naev/naev/releases/download/v%{version}/%{name}-%{version}-source.tar.xz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.77.2
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 1.7.0
BuildRequires:  openblas-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-pyaml
BuildRequires:  rust >= 1.89.0
BuildRequires:  rust-bindgen >= 0.72.0
BuildRequires:  zstd
BuildRequires:  pkgconfig(AMD)
BuildRequires:  pkgconfig(BTF)
BuildRequires:  pkgconfig(CAMD)
BuildRequires:  pkgconfig(CCOLAMD)
BuildRequires:  pkgconfig(CHOLMOD)
BuildRequires:  pkgconfig(COLAMD)
BuildRequires:  pkgconfig(CXSparse)
BuildRequires:  pkgconfig(GraphBLAS)
BuildRequires:  pkgconfig(KLU)
BuildRequires:  pkgconfig(KLU_CHOLMOD)
BuildRequires:  pkgconfig(LAGraph)
BuildRequires:  pkgconfig(LDL)
BuildRequires:  pkgconfig(ParU)
BuildRequires:  pkgconfig(RBio)
BuildRequires:  pkgconfig(SPEX)
BuildRequires:  pkgconfig(SPQR)
BuildRequires:  pkgconfig(SuiteSparse_Mongoose)
BuildRequires:  pkgconfig(SuiteSparse_config)
BuildRequires:  pkgconfig(UMFPACK)
BuildRequires:  pkgconfig(dav1d) >= 1.3.0
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glpk)
BuildRequires:  pkgconfig(libcmark) >= 0.31.0
BuildRequires:  pkgconfig(libenet) >= 1.3
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libunibreak) >= 4.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(sdl3) >= 3.2.0
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
# the bindgen generated max_align_t layout check in naevc.rs fails to compile on 32-bit x86
ExcludeArch:    %{ix86}

%description
Naev is a 2D space trading and combat game, in a similar vein to Escape Velocity.

Naev is played from a top-down perspective, featuring fast-paced combat, many ships,
a large variety of equipment and a large galaxy to explore. The game is
open-ended, letting you proceed at your own pace.

%prep
%setup -q -n naev-%{version} -a1

# Remove third part libraries so we're guaranteed to use system libraries
rm -rf subprojects/packagefiles

%build
# Disable LTO: GCC LTO bytecode in static libnaev.a cannot be linked by rustc
%define _lto_cflags %{nil}
export LIBSSH2_SYS_USE_PKG_CONFIG=1
# Disabling C and LUA docs since those are only required if you're hacking on Naev
# Disabling debug because it would need BuildRequires backtrace which is only in available in repo network:cryptocurrencies
%meson \
    -Ddocs_c=disabled \
    -Ddocs_lua=disabled \
    -Ddebug=false
cp Cargo.lock %{_vpath_builddir}/Cargo.lock
%meson_build

%install
%meson_install

# Remove dummy empty Rust rlib wrapper library installed by meson
rm -f %{buildroot}%{_libdir}/libnaev_rlib.so

# Remove already handled doc files
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# Clean up some unneeded scripts and other development files
find %{buildroot}%{_datadir}/%{name} \( -name '*.sh' -o -name '*.py' -o -name '*.pyc' \) -delete
rm -rf %{buildroot}%{_datadir}/%{name}/dat/outfits/generated/__pycache__
rm -rf %{buildroot}%{_datadir}/%{name}/dat/lua-repl
rm -rf %{buildroot}%{_datadir}/%{name}/dat/.pre-commit-config.yaml
rm -f %{buildroot}%{_datadir}/%{name}/dat/.gitattributes

%fdupes %{buildroot}%{_datadir}/%{name}

# find_lang only finds one type of filename, this one all .mo files.
for dir in %{buildroot}/%{_datadir}/naev/dat/gettext/*; do
    for file in "$dir/LC_MESSAGES/"*.mo; do
        echo "%%lang($(basename "$dir")) /$(realpath --relative-to %{buildroot} "$file")" >> %{name}.lang
    done
done

%files -f %{name}.lang
%license LICENSE
%doc Readme.md Changelog.md dat/AUTHORS
%{_mandir}/man6/*
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.xml
%{_datadir}/icons/hicolor/*x*/apps/*.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
