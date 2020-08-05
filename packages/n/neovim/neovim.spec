#
# spec file for package neovim
#
# Copyright (c) 2020 SUSE LLC
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


Name:           neovim
Version:        0.4.4
Release:        0
Summary:        Vim-fork focused on extensibility and agility
License:        Apache-2.0 AND Vim
Group:          Productivity/Text/Editors
URL:            https://neovim.io/
Source0:        https://github.com/neovim/neovim/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        sysinit.vim
Source2:        spec-template
Source3:        suse-spec-template
Source99:       neovim-rpmlintrc
# PATCH-FIX-OPENSUSE neovim.patch mcepl@cepl.eu
Patch0:         neovim.patch
# PATCH-FIX-OPENSUSE neovim-0.1.7-bitop.patch mcepl@cepl.eu build with old Lua with external bit module
Patch1:         neovim-0.1.7-bitop.patch
# PATCH-FIX-SLE libuv-compat.patch sr#793088 gh#neovim/neovim#12108 mcepl@suse.com
# works around too old version of libuv on Leap 15.*
Patch2:         libuv-compat.patch
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  filesystem
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gperf
BuildRequires:  hicolor-icon-theme
BuildRequires:  libnsl-devel
BuildRequires:  libtermkey-devel
BuildRequires:  libtool
BuildRequires:  libuv-devel
BuildRequires:  libvterm-devel >= 0.1
BuildRequires:  lua-macros
BuildRequires:  lua51-LPeg
BuildRequires:  lua51-bit32
BuildRequires:  lua51-luarocks
BuildRequires:  lua51-luv-devel
BuildRequires:  lua51-mpack
BuildRequires:  luajit-devel
BuildRequires:  make
BuildRequires:  msgpack-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  unibilium-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
Requires:       gperf
Requires:       libvterm0 >= 0.1
Requires:       lua51-bit32
Requires:       lua51-luv
Requires:       python3-neovim
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Recommends:     xsel
%if 0%{?suse_version} < 1330
BuildRequires:  hicolor-icon-theme
Requires(post): gtk3-tools
Requires(postun): gtk3-tools
%endif

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
%setup -q
%patch0 -p1
%patch1 -p1
%if 0%{?suse_version} == 1500
%patch2 -p1
%endif

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
%ifarch aarch64 ppc64
       -DPREFER_LUA=ON \
%endif
       -DCMAKE_SKIP_RPATH=ON -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DUSE_BUNDLED=OFF -DLUAJIT_USE_BUNDLED=OFF \
       -DCMAKE_COLOR_MAKEFILE=OFF \
       -DCMAKE_C_FLAGS_RELWITHDEBINFO="$opts" \
       -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
       -DLIBLUV_LIBRARY=%{lua_archdir}/luv.so \
       -DLIBLUV_INCLUDE_DIR:PATH=%{lua_incdir}
make %{?_smp_mflags} VERBOSE=1

popd

%install
%cmake_install

# system-wide configuration file
install -D -m 644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/nvim/sysinit.vim
ln -sf  %{_sysconfdir}/nvim/sysinit.vim %{buildroot}%{_datadir}/nvim/sysinit.vim

%if 0%{?suse_version}
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/nvim/template.spec
%else
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/nvim/template.spec
%endif

%suse_update_desktop_file -r nvim ConsoleOnly Application Utility TextEditor

# vim/site directories for plugins shared with vim
mkdir -p %{buildroot}%{vimplugin_dir}/{after,after/syntax,autoload,colors,doc,ftdetect,plugin,syntax}

%fdupes %{buildroot}%{_datadir}/
%find_lang nvim

# We have to have rpath
# https://en.opensuse.org/openSUSE:Packaging_checks
export NO_BRP_CHECK_RPATH=true

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post
%endif

%if 0%{?suse_version} < 1330
%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%doc BACKERS.md CONTRIBUTING.md README.md
%license LICENSE
%{_bindir}/nvim
%{_datadir}/nvim/
%{_datadir}/applications/nvim.desktop
%{_datadir}/pixmaps/nvim.png
%{_mandir}/man1/nvim.1%{?ext_man}
%dir %{_sysconfdir}/nvim
%config(noreplace) %{_sysconfdir}/nvim/sysinit.vim
%dir %{_datadir}/vim
%dir %{vimplugin_dir}/
%dir %{vimplugin_dir}/after
%dir %{vimplugin_dir}/after/syntax
%dir %{vimplugin_dir}/autoload
%dir %{vimplugin_dir}/colors
%dir %{vimplugin_dir}/doc
%dir %{vimplugin_dir}/ftdetect
%dir %{vimplugin_dir}/plugin
%dir %{vimplugin_dir}/syntax

%files lang -f nvim.lang

%changelog
