#
# spec file for package vim
#
# Copyright (c) 2022 SUSE LLC
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


%define pkg_version 9.0
%define patchlevel 0978
%define patchlevel_compact %{patchlevel}
%define VIM_SUBDIR vim90
%define site_runtimepath %{_datadir}/vim/site
%define make make VIMRCLOC=%{_sysconfdir} VIMRUNTIMEDIR=%{_datadir}/vim/current MAKE="make -e" %{?_smp_mflags}
%bcond_without python2

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           vim
Version:        %{pkg_version}.%{patchlevel_compact}
Release:        0
Summary:        Vi IMproved
License:        Vim
Group:          Productivity/Text/Editors
URL:            http://www.vim.org/
Source:         https://github.com/vim/vim/archive/v%{pkg_version}.%{patchlevel}.tar.gz#/vim-%{pkg_version}.%{patchlevel}.tar.gz
Source3:        suse.vimrc
Source4:        vimrc_example1
Source5:        vimrc_example2
Source8:        suse.gvimrc
Source10:       README.Japanese-XIM
Source13:       vitmp.c
Source14:       vitmp.1
Source15:       vim132
Source19:       gvim.desktop
Source20:       spec.skeleton
Source21:       spec.vim
Source23:       apparmor.vim
Source24:       gvim.svg
Source25:       gvim_24.png
Source26:       gvim_32.png
Source27:       gvim_48.png
Source28:       gvim_64.png
Source29:       gvim_96.png
Source98:       vim-changelog.sh
Source99:       %{name}-7.4-rpmlintrc
Patch3:         %{name}-7.4-disable_lang_no.patch
Patch4:         %{name}-7.3-gvimrc_fontset.patch
Patch5:         %{name}-7.4-highlight_fstab.patch
Patch6:         %{name}-7.3-sh_is_bash.patch
Patch7:         %{name}-7.3-filetype_ftl.patch
Patch8:         %{name}-7.3-help_tags.patch
Patch9:         %{name}-7.3-use_awk.patch
Patch10:        %{name}-7.3-name_vimrc.patch
Patch11:        %{name}-7.3-mktemp_tutor.patch
Patch15:        %{name}-7.4-filetype_apparmor.patch
Patch18:        %{name}-7.3-filetype_spec.patch
Patch21:        %{name}-7.3-filetype_changes.patch
Patch22:        %{name}-7.4-filetype_mine.patch
Patch23:        vim-8.0-ttytype-test.patch
Patch24:        disable-unreliable-tests.patch
Patch25:        ignore-flaky-test-failure.patch
Patch100:       vim73-no-static-libpython.patch
Patch101:       vim-8.0.1568-defaults.patch
# https://github.com/vim/vim/issues/3348 - problem more probadly in buildenv than in test
Patch102:       vim-8.1.0297-dump3.patch
Patch104:       vim-8.2.2411-globalvimrc.patch
BuildRequires:  autoconf
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  gpm-devel
BuildRequires:  libacl-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  ruby-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(xt)
Requires:       vim-data-common = %{version}-%{release}
%if %{with libalternatives}
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
Recommends:     vim-data = %{version}-%{release}
Conflicts:      vim-base < 8.2
Provides:       vi
Provides:       vim-base = %{version}-%{release}
Provides:       vim-enhanced = %{version}-%{release}
Provides:       vim-python = %{version}-%{release}
Obsoletes:      vim-base < %{version}-%{release}
Obsoletes:      vim-enhanced < %{version}-%{release}
Obsoletes:      vim-python < %{version}-%{release}
Provides:       vim_client
%{?libperl_requires}
%if %{with python2}
BuildRequires:  python2-devel
%endif

%description
Vim (Vi IMproved) is an almost compatible version of the UNIX editor
vi. Almost every possible command can be performed using only ASCII
characters. Only the 'Q' command is missing (you do not need it). Many
new features have been added: multilevel undo, command line history,
file name completion, block operations, and editing of binary data.

%package data
Summary:        Data files needed for extended vim functionality
Group:          Productivity/Text/Editors
Requires:       vim-data-common = %{version}-%{release}
# Used to be in vim-plugins package
Obsoletes:      vim-plugin-matchit <= 1.13.2
Provides:       vim-plugin-matchit = 1.13.2
# conflicts with nginx own plugin
Obsoletes:      vim-plugin-nginx < %{version}
Provides:       vim-plugin-nginx = %{version}

BuildArch:      noarch

%description data
This package contains optional runtime & syntax files for vim.

%package data-common
Summary:        Common Data files for vim & gvim
Group:          Productivity/Text/Editors
BuildArch:      noarch

%description data-common
This package contains basic runtime & syntax files for vim

%package -n gvim
Summary:        A GUI for Vi
Group:          Productivity/Text/Editors
Requires:       gvim_client
Requires:       vim-data = %{version}-%{release}
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
Conflicts:      gvim < 8.2
Provides:       gvim-base = %{version}-%{release}
Provides:       gvim-enhanced = %{version}-%{release}
Obsoletes:      gvim-base < %{version}-%{release}
Obsoletes:      gvim-enhanced < %{version}-%{release}
Provides:       gvim_client
Provides:       vi
Provides:       vim_client

%description -n gvim
Package gvim contains the largest set of features of vim, which is
graphical windows and language interpreter, like python, ruby, or perl.
You need package vim for the help and other documentation too. If you
want less features, you might want to install vim instead.

%package small
Summary:        Vim with reduced features
Group:          Productivity/Text/Editors
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
Provides:       vi
Provides:       vim_client
Requires:       vim-data-common = %{version}-%{release}

%description small
Vim compiled with reduced feature set such as no script
interpreters built in

%prep
%setup -q -n %{name}-%{pkg_version}.%{patchlevel}

%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
cp %{SOURCE23} runtime/syntax/apparmor.vim
%patch15 -p1
%patch18 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch104 -p1
cp %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE8} %{SOURCE10} .

# Unreliable tests
# See also disable-unreliable-tests.patch
rm src/testdir/test_arglist.*
rm src/testdir/test_command_count.*
rm src/testdir/test_cmdline.*
rm src/testdir/test_channel.*
rm src/testdir/test_diffmode.*
rm src/testdir/test_mksession.*
rm src/testdir/gen_opt_test.*
rm src/testdir/test_options.*
rm src/testdir/test_popupwin.*
rm src/testdir/test_startup.*
rm src/testdir/test_terminal*
rm src/testdir/test_textprop.*
rm src/testdir/test_window_cmd.*
rm src/testdir/test_writefile.*
rm runtime/indent/testdir/vim.*

%build
export CFLAGS="%{optflags} -Wall -pipe -fno-strict-aliasing"
export CFLAGS=${CFLAGS/-D_FORTIFY_SOURCE=2/-D_FORTIFY_SOURCE=1}

export COMMON_OPTIONS="\
    --with-vim-name=vim \
    --with-ex-name=ex \
    --with-view-name=view \
    --enable-cscope \
    --enable-multibyte \
    --with-compiledby='http://www.opensuse.org/' \
    --with-tlib=tinfo \
    --with-global-runtime=%{site_runtimepath} \
    "

# yeah kind of weird to call this small when we then use the
# "normal" set. Calling the package vim-normal is weird though as
# huge is our default.
export SMALL_OPTIONS="\
    $COMMON_OPTIONS \
    --with-features=small \
    --enable-luainterp=no \
    --enable-pythoninterp=no \
    --enable-perlinterp=no \
    --enable-python3interp=no \
    --enable-rubyinterp=no"

export HUGE_OPTIONS="\
    $COMMON_OPTIONS \
    --with-features=huge \
    --enable-luainterp=dynamic \
    --enable-perlinterp=yes \
    --enable-python3interp=dynamic \
    --enable-rubyinterp=dynamic
    --enable-pythoninterp=%{?with_python2:yes}%{!?with_python2:no}"

export GUI_OPTIONS="\
    --disable-icon-cache-update \
    --enable-xim \
    --enable-fontset \
    --enable-gui=gtk3"

export NOGUI_OPTIONS="\
    --disable-gui \
    --disable-gpm \
    --with-x=no \
    "

pushd src
autoconf
popd

# build smaller vim
%configure ${SMALL_OPTIONS} ${NOGUI_OPTIONS}
sed -i -e 's|define HAVE_DATE_TIME 1|undef HAVE_DATE_TIME|' src/auto/config.h
make %{?_smp_mflags}
cp src/vim vim-small

# build normal vim
make -j1 distclean
%configure ${HUGE_OPTIONS} ${NOGUI_OPTIONS}
sed -i -e 's|define HAVE_DATE_TIME 1|undef HAVE_DATE_TIME|' src/auto/config.h
make %{?_smp_mflags}
cp src/vim vim-nox11

# build gvim
make -j1 distclean
%configure ${HUGE_OPTIONS} ${GUI_OPTIONS}
sed -i -e 's|define HAVE_DATE_TIME 1|undef HAVE_DATE_TIME|' src/auto/config.h
make %{?_smp_mflags}

#
# build vitmp
gcc %{optflags} %{SOURCE13} -o vitmp

%install
%make_install STRIP=:
# create icon directories and install the icons into it
for SIZE in 24 32 48 64 96; do
  install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps
  install -m 0644 %{_sourcedir}/gvim_${SIZE}.png %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps/gvim.png
done
install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 0644 %{SOURCE24} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/gvim.svg

# the last installed binary is gvim. preserve it
mv %{buildroot}%{_bindir}/vim %{buildroot}%{_bindir}/gvim
%if %{with libalternatives}
for f in vimdiff ex view rview rvim; do
    rm %{buildroot}%{_bindir}/$f
done
%else
# fix gvim symlinks. e* was added here as it doesnt make much sense in
# console
for f in egvim egview eview evim gex gvi gview gvimdiff rgview rgvim ; do
    ln -s -vf gvim %{buildroot}%{_bindir}/$f
done
%endif

# install vim
install -D -m 0755 vim-small %{buildroot}%{_bindir}/vim-small
install -D -m 0755 vim-nox11 %{buildroot}%{_bindir}/vim-nox11
%if ! %{with libalternatives}
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/vim %{buildroot}%{_bindir}/vim
ln -s -f %{_sysconfdir}/alternatives/vi %{buildroot}%{_bindir}/vi
%else
for f in vi vim rvim evim eview egview view rview vimdiff edit ex egvim gex gvi gview gvimdiff rgview rgvim ; do
ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/$f
mkdir -p %{buildroot}%{_datadir}/libalternatives/$f
done
for f in vi vim rvim view rview vimdiff edit ex; do
cat > %{buildroot}%{_datadir}/libalternatives/$f/20.conf <<EOF
binary=%{_bindir}/vim-nox11
group=vim,vi
options=KeepArgv0
EOF
done
for f in vi vim evim rvim egview eview view rview vimdiff edit ex egvim gex gvi gview gvimdiff rgview rgvim ; do
cat > %{buildroot}%{_datadir}/libalternatives/$f/30.conf <<EOF
binary=%{_bindir}/gvim
group=vi,vim
options=KeepArgv0
EOF
done
for f in vim vi ; do
cat > %{buildroot}%{_datadir}/libalternatives/$f/19.conf <<EOF
binary=%{_bindir}/vim-small
group=vim,vi
options=KeepArgv0
EOF
done
%endif

# compat symlinks
mkdir %{buildroot}/bin
%if !0%{?usrmerged}
ln -s -f %{_bindir}/vim   %{buildroot}/bin/vi
ln -s -f %{_bindir}/vim   %{buildroot}/bin/vim
%endif
ln -s -f vim              %{buildroot}%{_bindir}/edit
%if !0%{?usrmerged}
ln -s -f %{_bindir}/vim   %{buildroot}/bin/ex
%endif

# man pages
ln -s -f vim.1.gz %{buildroot}%{_mandir}/man1/vi.1.gz
ln -s -f vim.1.gz %{buildroot}%{_mandir}/man1/ex.1.gz

# vitmp
install -m 0755 vitmp       %{buildroot}%{_bindir}/vitmp
install -m 0644 %{SOURCE14} %{buildroot}%{_mandir}/man1/vitmp.1
install -m 0755 %{SOURCE15} %{buildroot}%{_datadir}/vim/%{VIM_SUBDIR}/tools/vim132

# make the vim settings more generic
ln -s -f %{VIM_SUBDIR} %{buildroot}%{_datadir}/vim/current

# additional files
install -D -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/vim/current/suse.vimrc
#install -D -m 0644 /dev/null %{buildroot}%{_sysconfdir}/vimrc
install -D -m 0644 %{SOURCE8} %{buildroot}%{_sysconfdir}/gvimrc

# create site wide runtime directory
mkdir -p -m 0755 %{buildroot}%{site_runtimepath}/after
mkdir -m 0755 %{buildroot}%{site_runtimepath}/autoload
mkdir -m 0755 %{buildroot}%{site_runtimepath}/colors
mkdir -m 0755 %{buildroot}%{site_runtimepath}/doc
mkdir -m 0755 %{buildroot}%{site_runtimepath}/plugin
mkdir -m 0755 %{buildroot}%{site_runtimepath}/syntax
mkdir -m 0755 %{buildroot}%{site_runtimepath}/ftdetect
mkdir -m 0755 %{buildroot}%{site_runtimepath}/after/syntax
mkdir -m 0755 %{buildroot}%{_datadir}/vim/current/skeletons
mkdir -m 0755 %{buildroot}%{_sysconfdir}/skel

# install spec helper
install -m 0644 %{SOURCE20} %{buildroot}%{_datadir}/vim/current/skeletons/skeleton.spec
install -m 0644 %{SOURCE21} %{buildroot}%{_datadir}/vim/current/plugin/spec.vim

# desktop file for gvim
install -D -m 0644 %{SOURCE19} %{buildroot}%{_datadir}/applications/gvim.desktop
%suse_update_desktop_file gvim Utility TextEditor

#
# documentation
install -d -m 0755 %{buildroot}%{_docdir}/{,g}vim/
install -D -m 0644 \
    vimrc_example1 vimrc_example2 suse.vimrc \
    README.txt READMEdir/README_src.txt READMEdir/README_unix.txt \
  %{buildroot}%{_docdir}/vim/
# gvim
install -D -m 0644 \
    README.Japanese-XIM runtime/gvimrc_example.vim suse.gvimrc \
  %{buildroot}%{_docdir}/gvim/

# remove unecessary duplicate manpages
rm -rf %{buildroot}%{_mandir}/fr.ISO8859-1/
rm -rf %{buildroot}%{_mandir}/fr.UTF-8/
rm -rf %{buildroot}%{_mandir}/pl.ISO8859-2/
rm -rf %{buildroot}%{_mandir}/pl.UTF-8/
rm -rf %{buildroot}%{_mandir}/ru.KOI8-R/
rm -rf %{buildroot}%{_mandir}/it.ISO8859-1/
rm -rf %{buildroot}%{_mandir}/it.UTF-8/
rm -rf %{buildroot}%{_mandir}/da.UTF-8/
rm -rf %{buildroot}%{_mandir}/de.UTF-8/
rm -rf %{buildroot}%{_mandir}/da.ISO8859-1/
rm -rf %{buildroot}%{_mandir}/de.ISO8859-1/
rm -Rf %{buildroot}%{_mandir}/tr.ISO8859-9/
rm -Rf %{buildroot}%{_mandir}/tr.UTF-8/

# remove unnecessary files
rm -rf %{buildroot}%{_datadir}/applications/vim.desktop
rm -rf %{buildroot}%{_datadir}/icons/locolor

# and move russian manpages to a place where they can be found
mv %{buildroot}%{_mandir}/ru.UTF-8 %{buildroot}%{_mandir}/ru

# remove some c source files
rm -f %{buildroot}%{_datadir}/vim/%{VIM_SUBDIR}/tools/*.c
rm -f %{buildroot}%{_datadir}/vim/%{VIM_SUBDIR}/macros/maze/*.c

# Remove sample server to avoid python dependency
rm %{buildroot}%{_datadir}/vim/%{VIM_SUBDIR}/tools/demoserver.py

# Create ghost files (see vim.conf)
mkdir -p %{buildroot}%{_localstatedir}/run/vi.recover

%fdupes -s %{buildroot}%{_datadir}/vim/%{VIM_SUBDIR}/lang
%fdupes -s %{buildroot}%{_datadir}/vim/%{VIM_SUBDIR}/tutor
%fdupes -s %{buildroot}%{_datadir}/vim/%{VIM_SUBDIR}/ftplugin

sed -i "s@%{_bindir}/env perl@%{_bindir}/perl@" %{buildroot}%{_datadir}/vim/%{VIM_SUBDIR}/tools/*.pl
sed -i "s@%{_bindir}/env perl@%{_bindir}/perl@" %{buildroot}%{_datadir}/vim/%{VIM_SUBDIR}/doc/vim2html.pl

%check
# vim does quite an extensive test relying on a full fledged terminal
# inside OBS, stdio is redirected to a serial console (where the build log
# is being recorded/extracted. Systemd set non-local tty by default to vt220
# in upcoming versions
export TERM=xterm
# Reset the terminal scrolling region left behind by the testsuite
trap "printf '\e[r'" EXIT
TEST_IGNORE_FLAKY=1 LC_ALL=en_US.UTF-8 make -j1 test

%if %{with libalternatives}
# with libalternatives
%pre
# removing old update-alternatives entries
if [ "$1" -gt 0 ] && [ -f %{_sbindir}/update-alternatives ] && [ ! -e %{_bindir}/vim-nox11 ]; then
    %{_sbindir}/update-alternatives --remove vim %{_bindir}/vim-nox11
fi

%pre -n gvim
if [ "$1" -gt 0 ] && [ -f %{_sbindir}/update-alternatives ] && [ ! -e %{_bindir}/gvim ] ; then
    %{_sbindir}/update-alternatives --remove vim %{_bindir}/gvim
fi

%pre small
if [ "$1" -gt 0 ] && [ -f %{_sbindir}/update-alternatives ] && [ ! -e %{_bindir}/vim-small ]; then
    %{_sbindir}/update-alternatives --remove vim %{_bindir}/vim-small
fi

%if 0%{?suse_version} <= 1315
%post -n gvim
%icon_theme_cache_post

%postun -n gvim
%icon_theme_cache_postun
%endif

%else

# without libalternatives
%post
%{_sbindir}/update-alternatives \
 --install %{_bindir}/vim vim %{_bindir}/vim-nox11 20 \
 --slave %{_bindir}/vi vi %{_bindir}/vim-nox11

%postun
if [ ! -e %{_bindir}/vim-nox11 ] ; then
  %{_sbindir}/update-alternatives --remove vim %{_bindir}/vim-nox11
fi

%post -n gvim
%{_sbindir}/update-alternatives \
 --install %{_bindir}/vim vim %{_bindir}/gvim 30 \
 --slave %{_bindir}/vi vi %{_bindir}/gvim
%if 0%{?suse_version} <= 1315
%icon_theme_cache_post
%endif

%postun -n gvim
if [ ! -e %{_bindir}/gvim ] ; then
  %{_sbindir}/update-alternatives --remove vim %{_bindir}/gvim
fi
%if 0%{?suse_version} <= 1315
%icon_theme_cache_postun
%endif

%post small
%{_sbindir}/update-alternatives \
 --install %{_bindir}/vim vim %{_bindir}/vim-small 19 \
 --slave %{_bindir}/vi vi %{_bindir}/vim-small

%postun small
if [ ! -e %{_bindir}/vim-small ] ; then
  %{_sbindir}/update-alternatives --remove vim %{_bindir}/vim-small
fi
%endif

%files
%if ! %{with libalternatives}
%ghost %{_sysconfdir}/alternatives/vim
%ghost %{_sysconfdir}/alternatives/vi
%else
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/vi
%{_datadir}/libalternatives/vi/20.conf
%dir %{_datadir}/libalternatives/vim
%{_datadir}/libalternatives/vim/20.conf
%dir %{_datadir}/libalternatives/rvim
%{_datadir}/libalternatives/rvim/20.conf
%dir %{_datadir}/libalternatives/view
%{_datadir}/libalternatives/view/20.conf
%dir %{_datadir}/libalternatives/rview
%{_datadir}/libalternatives/rview/20.conf
%dir %{_datadir}/libalternatives/ex
%{_datadir}/libalternatives/ex/20.conf
%dir %{_datadir}/libalternatives/edit
%{_datadir}/libalternatives/edit/20.conf
%dir %{_datadir}/libalternatives/vimdiff
%{_datadir}/libalternatives/vimdiff/20.conf
%endif
%{_bindir}/vim-nox11
%{_bindir}/vim
# symlinks
%if !0%{?usrmerged}
/bin/vi
/bin/vim
/bin/ex
%endif
%{_bindir}/edit
%{_bindir}/ex
%{_bindir}/rview
%{_bindir}/rvim
%{_bindir}/vi
%{_bindir}/view
%{_bindir}/vimdiff
# additional binaries
%{_bindir}/vitmp
%{_bindir}/vimtutor
%{_bindir}/gvimtutor
%{_bindir}/xxd
# man pages
%{_mandir}/man1/*
%dir %{_mandir}/da
%dir %{_mandir}/da/man1/
%{_mandir}/da/man1/*
%dir %{_mandir}/de
%dir %{_mandir}/de/man1/
%{_mandir}/de/man1/*
%dir %{_mandir}/fr
%dir %{_mandir}/fr/man1/
%{_mandir}/fr/man1/*
%dir %{_mandir}/it
%dir %{_mandir}/it/man1/
%{_mandir}/it/man1/*
%dir %{_mandir}/ru
%dir %{_mandir}/ru/man1/
%{_mandir}/ru/man1/*
%dir %{_mandir}/pl
%dir %{_mandir}/pl/man1/
%{_mandir}/pl/man1/*
%dir %{_mandir}/ja
%dir %{_mandir}/ja/man1/
%{_mandir}/ja/man1/*
%dir %{_mandir}/tr
%dir %{_mandir}/tr/man1/
%{_mandir}/tr/man1/*
# docs and data file
%license LICENSE
%doc %{_docdir}/vim
#
%dir %{_datadir}/vim/%{VIM_SUBDIR}/colors/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/compiler/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/doc/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/ftplugin/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/indent/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/import/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/import/dist/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/keymap/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/lang/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/macros/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/pack/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/plugin/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/print/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/spell/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/syntax/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/tools/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/tutor/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/skeletons/
%dir %{site_runtimepath}
%dir %{site_runtimepath}/autoload/
%dir %{site_runtimepath}/colors/
%dir %{site_runtimepath}/doc/
%dir %{site_runtimepath}/plugin/
%dir %{site_runtimepath}/syntax/
%dir %{site_runtimepath}/ftdetect/
%dir %{site_runtimepath}/after/
%dir %{site_runtimepath}/after/syntax/

%files data
# exclude common files
%exclude %{_datadir}/vim/%{VIM_SUBDIR}/autoload/dist/ft.vim
%exclude %{_datadir}/vim/%{VIM_SUBDIR}/autoload/dist/script.vim
%exclude %{_datadir}/vim/%{VIM_SUBDIR}/colors/lists/default.vim
%exclude %{_datadir}/vim/%{VIM_SUBDIR}/syntax/nosyntax.vim
%exclude %{_datadir}/vim/%{VIM_SUBDIR}/syntax/resolv.vim
%exclude %{_datadir}/vim/%{VIM_SUBDIR}/syntax/sh.vim
%exclude %{_datadir}/vim/%{VIM_SUBDIR}/syntax/syncolor.vim
%exclude %{_datadir}/vim/%{VIM_SUBDIR}/syntax/synload.vim
%exclude %{_datadir}/vim/%{VIM_SUBDIR}/syntax/syntax.vim
%exclude %{_datadir}/vim/%{VIM_SUBDIR}/syntax/vim.vim
# data files
%{_datadir}/vim/%{VIM_SUBDIR}/autoload/*
%{_datadir}/vim/%{VIM_SUBDIR}/colors/*
%{_datadir}/vim/%{VIM_SUBDIR}/compiler/*
%{_datadir}/vim/%{VIM_SUBDIR}/doc/*
%{_datadir}/vim/%{VIM_SUBDIR}/ftplugin/*
%{_datadir}/vim/%{VIM_SUBDIR}/indent/*
%{_datadir}/vim/%{VIM_SUBDIR}/import/dist/*
%{_datadir}/vim/%{VIM_SUBDIR}/keymap/*
%{_datadir}/vim/%{VIM_SUBDIR}/lang/*
%{_datadir}/vim/%{VIM_SUBDIR}/macros/*
%{_datadir}/vim/%{VIM_SUBDIR}/pack/*
%{_datadir}/vim/%{VIM_SUBDIR}/plugin/*
%{_datadir}/vim/%{VIM_SUBDIR}/print/*
%{_datadir}/vim/%{VIM_SUBDIR}/skeletons/*
%{_datadir}/vim/%{VIM_SUBDIR}/spell/*
%{_datadir}/vim/%{VIM_SUBDIR}/syntax/*
%{_datadir}/vim/%{VIM_SUBDIR}/tools/*
%{_datadir}/vim/%{VIM_SUBDIR}/tutor/*

%files data-common
# we can't currently own /etc/vimrc. If we keep owning it, an
# existing, unmodified vimrc would not be removed. That results in a
# duplicated definition of SKEL_spec().
# see also https://github.com/rpm-software-management/rpm/issues/1296
#%ghost %config(noreplace) %{_sysconfdir}/vimrc
%{_datadir}/vim/current
%dir %{_datadir}/vim/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/autoload/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/autoload/dist/
%dir %{_datadir}/vim/%{VIM_SUBDIR}/syntax/
%{_datadir}/vim/%{VIM_SUBDIR}/suse.vimrc
%{_datadir}/vim/%{VIM_SUBDIR}/autoload/dist/ft.vim
%{_datadir}/vim/%{VIM_SUBDIR}/autoload/dist/script.vim
%{_datadir}/vim/%{VIM_SUBDIR}/colors/lists/default.vim
%{_datadir}/vim/%{VIM_SUBDIR}/syntax/nosyntax.vim
%{_datadir}/vim/%{VIM_SUBDIR}/syntax/resolv.vim
%{_datadir}/vim/%{VIM_SUBDIR}/syntax/sh.vim
%{_datadir}/vim/%{VIM_SUBDIR}/syntax/syncolor.vim
%{_datadir}/vim/%{VIM_SUBDIR}/syntax/synload.vim
%{_datadir}/vim/%{VIM_SUBDIR}/syntax/syntax.vim
%{_datadir}/vim/%{VIM_SUBDIR}/syntax/vim.vim
%{_datadir}/vim/%{VIM_SUBDIR}/*.vim

%files -n gvim
%doc runtime/doc/gui_x11.txt
%ghost %config(missingok) %{_sysconfdir}/gvimrc
%if ! %{with libalternatives}
%ghost %{_sysconfdir}/alternatives/vim
%ghost %{_sysconfdir}/alternatives/vi
%else
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/vi
%{_datadir}/libalternatives/vi/30.conf
%dir %{_datadir}/libalternatives/vim
%{_datadir}/libalternatives/vim/30.conf
%dir %{_datadir}/libalternatives/rvim
%{_datadir}/libalternatives/rvim/30.conf
%dir %{_datadir}/libalternatives/view
%{_datadir}/libalternatives/view/30.conf
%dir %{_datadir}/libalternatives/rview
%{_datadir}/libalternatives/rview/30.conf
%dir %{_datadir}/libalternatives/eview
%{_datadir}/libalternatives/eview/30.conf
%dir %{_datadir}/libalternatives/ex
%{_datadir}/libalternatives/ex/30.conf
%dir %{_datadir}/libalternatives/edit
%{_datadir}/libalternatives/edit/30.conf
%dir %{_datadir}/libalternatives/vimdiff
%{_datadir}/libalternatives/vimdiff/30.conf
%dir %{_datadir}/libalternatives/egvim
%{_datadir}/libalternatives/egvim/30.conf
%dir %{_datadir}/libalternatives/egview
%{_datadir}/libalternatives/egview/30.conf
%dir %{_datadir}/libalternatives/evim
%{_datadir}/libalternatives/evim/30.conf
%dir %{_datadir}/libalternatives/gex
%{_datadir}/libalternatives/gex/30.conf
%dir %{_datadir}/libalternatives/gvi
%{_datadir}/libalternatives/gvi/30.conf
%dir %{_datadir}/libalternatives/gview
%{_datadir}/libalternatives/gview/30.conf
%dir %{_datadir}/libalternatives/gvimdiff
%{_datadir}/libalternatives/gvimdiff/30.conf
%dir %{_datadir}/libalternatives/rgvim
%{_datadir}/libalternatives/rgvim/30.conf
%dir %{_datadir}/libalternatives/rgview
%{_datadir}/libalternatives/rgview/30.conf
%endif
%{_bindir}/vi
%{_bindir}/vim
%{_bindir}/egview
%{_bindir}/egvim
%{_bindir}/eview
%{_bindir}/evim
%{_bindir}/gex
%{_bindir}/gvi
%{_bindir}/gview
%{_bindir}/gvim
%{_bindir}/gvimdiff
%{_bindir}/rgview
%{_bindir}/rgvim
# menu icon
%{_datadir}/applications/gvim.desktop
%{_datadir}/icons/hicolor/*/apps/gvim.*
%doc %{_docdir}/gvim

%files small
%license LICENSE
%if ! %{with libalternatives}
%ghost %{_sysconfdir}/alternatives/vim
%ghost %{_sysconfdir}/alternatives/vi
%else
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/vi
%{_datadir}/libalternatives/vi/19.conf
%dir %{_datadir}/libalternatives/vim
%{_datadir}/libalternatives/vim/19.conf
%endif
%{_bindir}/vi
%{_bindir}/vim
%{_bindir}/vim-small

%changelog
