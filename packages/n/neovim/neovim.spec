#
# spec file for package neovim
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


%{?!python3_pkgversion:%define python3_pkgversion 3}

%define vimplugin_dir %{_datadir}/vim/site
# Luajit not available on all platforms
%ifarch %{arm} %{ix86} x86_64 aarch64
%bcond_without luajit
%else
%bcond_with luajit
%endif

Name:           neovim
Version:        0.10.0
Release:        0
Summary:        Vim-fork focused on extensibility and agility
License:        Apache-2.0 AND Vim AND GPL-3.0-or-later AND CC-BY-3.0
Group:          Productivity/Text/Editors
URL:            https://neovim.io/
Source0:        https://github.com/neovim/neovim/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        sysinit.vim
Source3:        suse-spec-template
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  filesystem
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gperf
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(libuv) >= 1.42.0
BuildRequires:  pkgconfig(msgpack-c)
BuildRequires:  pkgconfig(termkey)
BuildRequires:  pkgconfig(tree-sitter) >= 0.20.9
BuildRequires:  pkgconfig(unibilium) >= 2.0.0
BuildRequires:  pkgconfig(vterm) >= 0.3.3
Requires:       gperf
Requires:       libvterm0 >= 0.3
Requires:       xdg-utils

Recommends:     wl-clipboard
Recommends:     xsel

BuildRequires:  libluv-devel
BuildRequires:  lua-macros
BuildRequires:  lua51-LPeg
BuildRequires:  lua51-bit32
BuildRequires:  lua51-luarocks
BuildRequires:  lua51-luv
BuildRequires:  lua51-mpack
%if %{with luajit}
BuildRequires:  luajit-devel
%else
BuildRequires:  lua51-BitOp
BuildRequires:  lua51-devel
%endif
Requires:       lua51-bit32
Requires:       lua51-lpeg
Requires:       lua51-luv
Recommends:     python3-neovim

Provides:       nvim

%description
Neovim is a refactor - and sometimes redactor - in the tradition of
Vim, which itself derives from Stevie. It is not a rewrite, but a
continuation and extension of Vim. Many rewrites, clones, emulators
and imitators exist; some are very clever, but none are Vim. Neovim
strives to be a superset of Vim, notwithstanding some intentionally
removed misfeatures; excepting those few and carefully-considered
excisions, Neovim is Vim. It is built for users who want the good
parts of Vim, without compromise, and more.

%lang_package

%define vimplugin_dir %{_datadir}/vim/site

%prep
%autosetup -p1

# Remove __DATE__ and __TIME__.
BUILD_TIME=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%{H}:%{M}')
BUILD_DATE=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%{b} %{d} %{Y}')
sed -i "s/__TIME__/\"$BUILD_TIME\"/" $(grep -rl '__TIME__')
sed -i "s/__DATE__/\"$BUILD_DATE\"/" $(grep -rl '__DATE__')

%build
# set vars to make build reproducible in spite of config/CMakeLists.txt
HOSTNAME=OBS
USERNAME=OBS
mkdir -p build
pushd build
export CFLAGS="%{optflags} -fcommon"
export CXXFLAGS="%{optflags} -fcommon"
%{__cmake} .. -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DPREFER_LUA=%{?with_luajit:OFF}%{!?with_luajit:ON} \
       -DLUA_PRG=%{_bindir}/%{?with_luajit:luajit}%{!?with_luajit:lua} \
%if %{with luajit}
       -DLUAJIT_INCLUDE_DIR:PATH=%(pkg-config --cflags-only-I luajit|cut -c 3-) \
%endif
       -DUSE_BUNDLED=OFF -DLUAJIT_USE_BUNDLED=ON  \
       -DCMAKE_SKIP_RPATH=ON -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DCMAKE_COLOR_MAKEFILE=OFF \
       -DCMAKE_C_FLAGS_RELWITHDEBINFO="$opts" \
       -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
       -DLIBLUV_INCLUDE_DIR:PATH=%{lua_incdir}

%make_build

popd

%install
%{?!cmake_install:%define cmake_install DESTDIR=%{buildroot} make install -C build}
%cmake_install

# system-wide configuration file
install -D -m 644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/nvim/sysinit.vim
ln -sf  %{_sysconfdir}/nvim/sysinit.vim %{buildroot}%{_datadir}/nvim/sysinit.vim

# install SUSE specific spec template
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/nvim/template.spec

desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    runtime/nvim.desktop
install -d -m0755 %{buildroot}%{_datadir}/pixmaps
install -m0644 runtime/nvim.png %{buildroot}%{_datadir}/pixmaps/nvim.png

# Fix exec bits
find %{buildroot}%{_datadir} \( -name \*.bat -o -name \*.awk \) \
    -print -exec chmod -x '{}' \;

# vim/site directories for plugins shared with vim
mkdir -p %{buildroot}%{vimplugin_dir}/{after,after/syntax,autoload,colors,doc,ftdetect,plugin,syntax}

%fdupes %{buildroot}%{_datadir}/
%find_lang nvim

# We have to have rpath
# https://en.opensuse.org/openSUSE:Packaging_checks
export NO_BRP_CHECK_RPATH=true

%files
%doc CONTRIBUTING.md README.md
%docdir %{_mandir}
%license LICENSE.txt
%{_bindir}/nvim
%{_mandir}/man1/nvim.1%{?ext_man}
%dir %{_datadir}/nvim
%{_datadir}/nvim/sysinit.vim
%{_datadir}/nvim/template.spec
%{_datadir}/nvim/runtime/
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/*
%dir %{_sysconfdir}/nvim
%config(noreplace) %{_sysconfdir}/nvim/sysinit.vim
%dir %{_datadir}/vim
%dir %{vimplugin_dir}
%dir %{vimplugin_dir}/after
%dir %{vimplugin_dir}/after/*
%dir %{vimplugin_dir}/autoload
%dir %{vimplugin_dir}/colors
%dir %{vimplugin_dir}/doc
%dir %{vimplugin_dir}/ftdetect
%dir %{vimplugin_dir}/plugin
%dir %{vimplugin_dir}/syntax

%files lang -f nvim.lang

%changelog
