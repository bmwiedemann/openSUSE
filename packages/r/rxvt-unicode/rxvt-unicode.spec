#
# spec file for package rxvt-unicode
#
# Copyright (c) 2021 SUSE LLC
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
%if 0%{?suse_version} < 1140
%define with_265color_terminfo_files 1
%endif
Name:           rxvt-unicode
Version:        9.26
Release:        0
#
Summary:        Rxvt X Terminal with Unicode Support
#
License:        GPL-3.0-or-later
Group:          System/X11/Terminals
URL:            http://software.schmorp.de/#rxvt-unicode
Source:         http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.bz2
Source1:        rxvt-unicode-rpmlintrc
Source2:        rxvt-unicode.README.SuSE
Source3:        rxvt-unicode-256color.desktop
Source4:        rxvt-unicode.desktop
Patch1:         rxvt-unicode-9.20-CVE-2008-1142-DISPLAY.patch
Patch2:         rxvt-unicode-9.21-xsubpp.patch
Patch3:         rxvt-unicode-0001-Prefer-XDG_RUNTIME_DIR-over-the-HOME.patch
Patch4:         rxvt-unicode-hardening.patch
Patch5:         rxvt-unicode-secondarywheel.patch
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
%requires_eq    perl
Provides:       locale(xorg-x11:ja;ko;zh)
%if ! 0%{?with_265color_terminfo_files}
Requires:       terminfo-base
%endif

%description
rxvt-unicode is a clone of the well-known terminal emulator rxvt,
modified to store text in Unicode (either UCS-2 or UCS-4) and to use
locale-correct input and output. It also supports mixing multiple fonts
at the same time, including Xft fonts.

%prep
%autosetup -p1
find -type d -name CVS -print0 | xargs -r0 rm -r
install -m 0644 %{SOURCE2} README.SUSE

%build
export COMMON_CONFIGURE_OPTIONS=" --enable-warnings --enable-unicode3 \
    --enable-combining \
    --enable-xft \
    --enable-font-styles \
    --enable-pixbuf \
    --enable-transparency \
    --enable-fading \
    --enable-next-scroll \
    --enable-rxvt-scroll \
    --enable-xterm-scroll \
    --enable-perl \
    --enable-xim \
    --enable-8bitctrls \
    --enable-fallback \
    --enable-iso14755 \
    --enable-frills \
    --enable-keepscrolling \
    --enable-selectionscrolling \
    --enable-mousewheel \
    --enable-slipwheeling \
    --enable-smart-resize \
    --enable-text-blink \
    --enable-pointer-blank \
    --enable-utmp \
    --enable-wtmp \
    --enable-lastlog \
    --with-codesets=all \
    --with-terminfo=%{_terminfo}"
#
export CFLAGS="%{optflags} -fno-strict-aliasing -Wno-unused"
export CXXFLAGS="$CFLAGS"
#
# build the 256color version
%configure --enable-256-color ${COMMON_CONFIGURE_OPTIONS}
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
%suse_update_desktop_file %{name}-256color
%suse_update_desktop_file %{name}
rm %{buildroot}/%{_terminfo}/r/%{name}

%files
%license COPYING
%doc Changes README* doc/README* doc/changes.txt
%doc doc/etc
%doc examples/
%{_bindir}/urxvt*
%{_bindir}/urclock
%dir %{_terminfo}/r
%if ! 0%{?with_265color_terminfo_files}
%exclude %{_terminfo}/r/%{name}-256color
%else
%{_terminfo}/r/%{name}-256color
%endif
%{_mandir}/man1/urxvt*.1%{?ext_man}
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
