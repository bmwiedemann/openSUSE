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


%ifarch ppc64le
%bcond_with luajit
%else
%bcond_without luajit
%endif
Name:           neovim
Version:        0.10.2
Release:        0
Summary:        Vim-fork focused on extensibility and agility
License:        Apache-2.0 AND Vim AND GPL-3.0-or-later AND CC-BY-3.0
URL:            https://neovim.io/
Source0:        https://github.com/neovim/neovim/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        sysinit.vim
Source3:        suse-spec-template
Source4:        spec.vim
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
BuildRequires:  lua-macros
BuildRequires:  lua51-bit32
BuildRequires:  lua51-compat-5.3
BuildRequires:  lua51-lpeg
BuildRequires:  lua51-luarocks
BuildRequires:  lua51-luv
BuildRequires:  lua51-mpack
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  pkgconfig(libluv)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(libuv) >= 1.42.0
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(msgpack-c)
BuildRequires:  pkgconfig(termkey)
BuildRequires:  pkgconfig(tree-sitter) >= 0.20.9
BuildRequires:  pkgconfig(unibilium) >= 2.0.0
BuildRequires:  pkgconfig(vterm) >= 0.3.3
Requires:       gperf
Requires:       libvterm0 >= 0.3
Requires:       lua51-bit32
Requires:       lua51-compat-5.3
Requires:       lua51-lpeg
Requires:       lua51-luarocks
Requires:       lua51-luv
Requires:       lua51-mpack
Requires:       tree-sitter-c >= 0.21.3
Requires:       tree-sitter-lua
Requires:       tree-sitter-markdown
Requires:       tree-sitter-python
Requires:       tree-sitter-query >= 0.4.0
Requires:       tree-sitter-vim
Requires:       tree-sitter-vimdoc >= 3.0.0
Requires:       xdg-utils
Recommends:     python3-neovim
Recommends:     wl-clipboard
Recommends:     xsel
Suggests:       ripgrep
Provides:       nvim
%lang_package

%description
Neovim is a refactor - and sometimes redactor - in the tradition of
Vim, which itself derives from Stevie. It is not a rewrite, but a
continuation and extension of Vim. Many rewrites, clones, emulators
and imitators exist; some are very clever, but none are Vim. Neovim
strives to be a superset of Vim, notwithstanding some intentionally
removed misfeatures; excepting those few and carefully-considered
excisions, Neovim is Vim. It is built for users who want the good
parts of Vim, without compromise, and more.

%prep
%autosetup

# Remove __DATE__ and __TIME__.
BUILD_TIME=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%{H}:%{M}')
BUILD_DATE=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%{b} %{d} %{Y}')
sed -i "s/__TIME__/\"$BUILD_TIME\"/" $(grep -rl '__TIME__')
sed -i "s/__DATE__/\"$BUILD_DATE\"/" $(grep -rl '__DATE__')

%build
# set vars to make build reproducible in spite of config/CMakeLists.txt
HOSTNAME=OBS
USERNAME=OBS
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DPREFER_LUA=%{?with_luajit:OFF}%{!?with_luajit:ON} \
       -DLUA_PRG=%{_bindir}/%{?with_luajit:luajit}%{!?with_luajit:lua} \
%if %{with luajit}
       -DLUAJIT_INCLUDE_DIR:PATH=%(pkg-config --cflags-only-I luajit|cut -c 3-) \
%endif
       -DUSE_BUNDLED=OFF -DLUAJIT_USE_BUNDLED=OFF  \
       -DCMAKE_SKIP_RPATH=ON -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DCMAKE_COLOR_MAKEFILE=OFF -DLTO_ENABLE=ON \
       -DCMAKE_C_FLAGS_RELWITHDEBINFO="$opts" \
       -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
       -DLIBLUV_INCLUDE_DIR:PATH=%{lua_incdir}

%make_build

%install
%cmake_install

# system-wide configuration file
install -D -m 644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/nvim/sysinit.vim
ln -sf  %{_sysconfdir}/nvim/sysinit.vim %{buildroot}%{_datadir}/nvim/sysinit.vim

# install SUSE specific spec template
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/nvim/template.spec
install -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/nvim/runtime/plugin/spec.vim

desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    runtime/nvim.desktop
install -Dm0644 runtime/nvim.png %{buildroot}%{_datadir}/pixmaps/nvim.png

# Fix exec bits
find %{buildroot}%{_datadir} \( -name \*.bat -o -name \*.awk \) \
    -print -exec chmod -x '{}' \;

# vim/site directories for plugins shared with vim
mkdir -p %{buildroot}%{_datadir}/vim/site/{after,after/syntax,autoload,colors,doc,ftdetect,plugin,syntax}

%fdupes %{buildroot}
%find_lang nvim

# We have to have rpath
# https://en.opensuse.org/openSUSE:Packaging_checks
export NO_BRP_CHECK_RPATH=true

%post
if [ -d %{_datadir}/nvim/runtime/parser ]; then
if [ ! -h %{_datadir}/nvim/runtime/parser ]; then
mv %{_datadir}/nvim/runtime/parser \
   %{_datadir}/nvim/runtime/parser.rpmsave
ln -sf %{_libdir}/tree_sitter %{_datadir}/nvim/runtime/parser
fi
else
ln -sf %{_libdir}/tree_sitter %{_datadir}/nvim/runtime/parser
fi

%files
%license LICENSE.txt
%doc CONTRIBUTING.md README.md
%dir %{_sysconfdir}/nvim
%config(noreplace) %{_sysconfdir}/nvim/sysinit.vim
%{_bindir}/nvim
%{_mandir}/man?/nvim.?%{?ext_man}
%{_datadir}/nvim
%{_datadir}/applications/nvim.desktop
%{_datadir}/icons/hicolor/128x128/apps/nvim.png
%{_datadir}/pixmaps/nvim.png
%dir %{_datadir}/vim
%dir %{_datadir}/vim/site
%dir %{_datadir}/vim/site/after
%dir %{_datadir}/vim/site/after/*
%dir %{_datadir}/vim/site/autoload
%dir %{_datadir}/vim/site/colors
%dir %{_datadir}/vim/site/doc
%dir %{_datadir}/vim/site/ftdetect
%dir %{_datadir}/vim/site/plugin
%dir %{_datadir}/vim/site/syntax

%files lang -f nvim.lang

%changelog
