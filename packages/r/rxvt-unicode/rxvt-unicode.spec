#
# spec file for package rxvt-unicode
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


#
%define _terminfo      %{_datadir}/terminfo
Name:           rxvt-unicode
Version:        9.31
Release:        0
#
Summary:        Rxvt X Terminal with Unicode Support
#
License:        GPL-3.0-or-later
Group:          System/X11/Terminals
URL:            https://software.schmorp.de/pkg/rxvt-unicode.html
Source:         https://dist.schmorp.de/%{name}/%{name}-%{version}.tar.bz2
Source2:        rxvt-unicode.README.SuSE
Source3:        rxvt-unicode-256color.desktop
Source4:        rxvt-unicode.desktop
Source10:       https://dist.schmorp.de/%{name}/%{name}-%{version}.tar.bz2.sig
Patch1:         rxvt-unicode-9.20-CVE-2008-1142-DISPLAY.patch
Patch2:         rxvt-unicode-9.21-xsubpp.patch
Patch3:         rxvt-unicode-0001-Prefer-XDG_RUNTIME_DIR-over-the-HOME.patch
Patch4:         rxvt-unicode-hardening.patch
Patch5:         rxvt-unicode-secondarywheel.patch
Patch7:         handle-new-tic-and-dont-install-terminfo.patch
Patch8:         dont-set-empty-local.patch
Patch9:         confirm-paste-Change-y-p-n-to-y-f-n-to-preserve-comp.patch
Patch10:        rxvt-unicode-9.31-fix-osc-responses-with-7-bit-st.patch
# https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=785ecf0b5343348e298a5fad9c46ba58b9b303fe
Patch11:        rxvt-unicode-gcc16-compilation-fix.patch
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libptytty)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
Requires:       terminfo-base
%requires_eq    perl
Provides:       locale(xorg-x11:ja;ko;zh)

%description
rxvt-unicode is a clone of the well-known terminal emulator rxvt,
modified to store text in Unicode (either UCS-2 or UCS-4) and to use
locale-correct input and output. It also supports mixing multiple fonts
at the same time, including Xft fonts.

%prep
%autosetup -p1
install -m 0644 %{SOURCE2} README.SUSE

%build
# --enable-everything adds support for all non-multichoice options listed in ./configure --help,
# except for: --enable-assert, --enable-256-color, --enable-8bitctrls, --enable-fallback and --enable-smart-resize.
# It also sets --with-codesets to "all"
export COMMON_CONFIGURE_OPTIONS="\
        --enable-warnings \
        --enable-everything \
        --enable-8bitctrls \
        --enable-fallback \
        --enable-smart-resize \
        --with-terminfo=%{_terminfo}"

#
export CFLAGS="%{optflags} -fno-strict-aliasing -Wno-unused"
export CXXFLAGS="$CFLAGS"
#
# build the 256color version
%configure ${COMMON_CONFIGURE_OPTIONS} --enable-256-color 
#
%make_build
#
for i in rxvt rxvtd rxvtc ; do mv src/${i} u${i}-256color ; done
%make_build distclean

# build the normal 88color version
%configure ${COMMON_CONFIGURE_OPTIONS}
#
%make_build

%install
TERMINFO="%{buildroot}%{_terminfo}" %make_install
install -m 0755 u*-256color %{buildroot}%{_bindir}
for j in %{buildroot}%{_mandir}/man1/* ; do
  ln -s $(basename ${j}) ${j%%.1}-256color.1 ;
done
mkdir examples/
cp -av doc/embed* doc/rxvt-tabbed doc/pty-fd examples/
chmod 0644 examples/*
rm -rf %{buildroot}%{_libdir}/urxvt/perl/macosx-clipboard-native
install -Dd -m 0755 "%{buildroot}%{_terminfo}/r" %{buildroot}%{_datadir}/applications/
# desktop files
install -Dm644 %{SOURCE3} %{buildroot}%{_datadir}/applications/%{name}-256color.desktop
install -Dm644 %{SOURCE4} %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -f %{buildroot}/%{_terminfo}/r/%{name}

%files
%license COPYING
%doc Changes README* doc/README* doc/changes.txt
%doc doc/etc
%doc examples/
%{_bindir}/urxvt*
%{_bindir}/urclock
%{_mandir}/man1/urxvt*.1%{?ext_man}
%{_mandir}/man1/urclock*.1%{?ext_man}
%{_mandir}/man3/urxvt*.3%{?ext_man}
%{_mandir}/man7/urxvt*.7%{?ext_man}
%dir %{_libdir}/urxvt/
%dir %{_libdir}/urxvt/perl
%{_libdir}/urxvt/urxvt.pm
%{_libdir}/urxvt/perl/digital-clock
%{_libdir}/urxvt/perl/background
%{_libdir}/urxvt/perl/example-refresh-hooks
%{_libdir}/urxvt/perl/selection
%{_libdir}/urxvt/perl/block-graphics-to-ascii
%{_libdir}/urxvt/perl/clickthrough
%{_libdir}/urxvt/perl/matcher
%{_libdir}/urxvt/perl/option-popup
%{_libdir}/urxvt/perl/searchable-scrollback
%{_libdir}/urxvt/perl/selection-autotransform
%{_libdir}/urxvt/perl/selection-popup
%{_libdir}/urxvt/perl/urxvt-popup
%{_libdir}/urxvt/perl/selection-pastebin
%{_libdir}/urxvt/perl/readline
%{_libdir}/urxvt/perl/tabbed
%{_libdir}/urxvt/perl/remote-clipboard
%{_libdir}/urxvt/perl/xim-onthespot
%{_libdir}/urxvt/perl/kuake
%{_libdir}/urxvt/perl/eval
%{_libdir}/urxvt/perl/overlay-osc
%{_libdir}/urxvt/perl/clipboard-osc
%{_libdir}/urxvt/perl/confirm-paste
%{_libdir}/urxvt/perl/bell-command
%{_libdir}/urxvt/perl/keysym-list
%{_libdir}/urxvt/perl/selection-to-clipboard
%{_datadir}/applications/%{name}-256color.desktop
%{_datadir}/applications/%{name}.desktop

%changelog
