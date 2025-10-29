#
# spec file for package neovim
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%ifarch ppc64le s390x
%bcond_with luajit
%else
%bcond_without luajit
%endif
Name:           neovim
Version:        0.11.4
Release:        0
Summary:        Vim-fork focused on extensibility and agility
License:        Apache-2.0 AND Vim AND GPL-3.0-or-later AND CC-BY-3.0
URL:            https://neovim.io/
Source0:        https://github.com/neovim/neovim/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        sysinit.vim
Source3:        suse-spec-template
Source4:        spec.vim
Source10:       https://github.com/neovim/deps/raw/06ef2b58b0876f8de1a3f5a710473dcd7afff251/opt/lua-dev-deps.tar.gz
BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  filesystem
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gperf
BuildRequires:  hicolor-icon-theme
BuildRequires:  hostname
BuildRequires:  libtool
BuildRequires:  lua51-lpeg
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(libluv)
BuildRequires:  pkgconfig(libutf8proc) >= 2.10.0
BuildRequires:  pkgconfig(libuv) >= 1.50.0
%if %{with luajit}
BuildRequires:  pkgconfig(luajit)
%else
BuildRequires:  pkgconfig(lua5.1)
%endif
BuildRequires:  pkgconfig(tree-sitter) >= 0.25.3
BuildRequires:  pkgconfig(unibilium) >= 2.1.2
BuildRequires:  pkgconfig(vterm) >= 0.3.3
BuildRequires:  treesitter_grammar(tree-sitter-vimdoc)
Requires:       gperf
Requires:       libvterm0 >= 0.3
Requires:       lua51-lpeg
Requires:       tree-sitter-c >= 0.23.4
Requires:       tree-sitter-lua >= 0.3.0
Requires:       tree-sitter-markdown >= 0.4.1
Requires:       tree-sitter-python
Requires:       tree-sitter-query >= 0.5.1
Requires:       tree-sitter-vim >= 0.5.0
Requires:       tree-sitter-vimdoc >= 3.0.1
Requires:       xdg-utils
Recommends:     inotify-tools
Recommends:     wl-clipboard
Recommends:     xsel
Suggests:       python3-neovim
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
%autosetup -p1

# Remove __DATE__ and __TIME__.
BUILD_TIME=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%{H}:%{M}')
BUILD_DATE=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%{b} %{d} %{Y}')
sed -i "s/__TIME__/\"$BUILD_TIME\"/" $(grep -rl '__TIME__')
sed -i "s/__DATE__/\"$BUILD_DATE\"/" $(grep -rl '__DATE__')

# setup unit test dependency
mkdir -p build/build/downloads/lua_dev_deps/
cp %{SOURCE10} build/build/downloads/lua_dev_deps/

%build
# Remove cmake4 error due to not setting
# min cmake version - sflees.de
export CMAKE_POLICY_VERSION_MINIMUM=3.5
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
       -DENABLE_TRANSLATIONS=ON \
       -DLIBLUV_INCLUDE_DIR:PATH=%{lua_incdir}
%cmake_build

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

# vim/site directories for plugins shared with vim
mkdir -p %{buildroot}%{_datadir}/vim/site/{after,after/syntax,autoload,colors,doc,ftdetect,plugin,syntax}

%fdupes %{buildroot}
%find_lang nvim

%ifnarch %{arm64}
%check
mkdir -p runtime/parser
ln -sf %{_libdir}/tree_sitter/vimdoc.so runtime/parser

%ifnarch %{power64} s390x
# old tests
%make_build USE_BUNDLED=OFF oldtest
%endif
# functional tests
%ifarch aarch64 x86_64
%make_build USE_BUNDLED=OFF unittest
%endif
%endif

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
