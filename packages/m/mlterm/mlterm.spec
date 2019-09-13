#
# spec file for package mlterm
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mlterm
Version:        3.8.7
Release:        0
Summary:        Multilingual Terminal Emulator for X
License:        BSD-3-Clause
Group:          System/X11/Terminals
Url:            http://mlterm.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/mlterm/01release/%{name}-%{version}/%{name}-%{version}.tar.gz
Source10:       %{name}.desktop
Patch0:         etc.patch
# PATCH-FIX-UPSTREAM: portability issues reported by rpmlint
# https://sourceforge.net/p/mlterm/bugs/78/
Patch1:         mlterm-cast.patch
BuildRequires:  canna-devel
BuildRequires:  coreutils
BuildRequires:  fwnn-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  scim-devel
BuildRequires:  uim-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fcitx)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gail)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(m17n-core)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(wordcut)
BuildRequires:  pkgconfig(x11)

Provides:       locale(xorg-x11:ja;ko;zh;ar;he)
%if 0%{?suse_version} >= 1330
Requires:       group(tty)
%endif

%description
Mlterm is a multilingual terminal emulator for the X Window System.

Multilingual features:

supported charsets: US_ASCII, ISO8859[1-11], ISO8859[13-16], TCVN5712,
VISCII, KOI8_R, KOI8_U, JISX0201, JISX0208, JISX0212, JISX0213, GB2312,
GBK, KSC5601, UHC, CNS11643-N, Big5, UCS2(4)

supported encodings: ISO-8859-[1-11], ISO-8859- [13-16], TCVN5612,
VISCII, KOI8_R, KOI8_U, EUC-JP, EUC-JISX0213, ISO-2022-JP [1, 2, 3],
Shift_JIS, Shift_JISX0213, EUC-KR, UHC, JOHAB, ISO-2022-KR,
ISO-2022-CN, GB2312(EUC-CN), GBK, GB18030, EUC-TW, Big5, Hz, UTF-8

character composition: TIS620, TCVN5712, JISX0213, UNICODE

Multiple xims are also supported and you can dynamically change various
xims.

Other features:
* scroll by wheel mouse
* antialias font (requires Xft and Xrender extensions)
* proportional font
* transparent background
* background image (requires Imlib)
* multiple pty windows
* scrollbar plug-in API (unstable)

%package canna
Summary:        Canna plugin for mlterm
Group:          System/X11/Terminals
Provides:       locale(scim:ja;ko;ar;he)

%description canna
A plugin to use the canna input methods directly from mlterm.

%package ibus
Summary:        Ibus plugin for mlterm
Group:          System/X11/Terminals
Provides:       locale(scim:ja;ko;ar;he)

%description ibus
A plugin to use the ibus input methods directly from mlterm.

%package wnn
Summary:        Wnn plugin for mlterm
Group:          System/X11/Terminals
Provides:       locale(scim:ja;ko;ar;he)

%description wnn
A plugin to use the wnn input methods directly from mlterm.

%package scim
Summary:        SCIM plugin for mlterm
Group:          System/X11/Terminals
Provides:       locale(scim:ja;ko;ar;he)

%description scim
A plugin to use the SCIM input methods directly from mlterm.

%package uim
Summary:        An uim plugin for mlterm
Group:          System/X11/Terminals
Provides:       locale(uim:ja;ko;ar;he)

%description uim
A plugin to use the uim input methods directly from mlterm.

%package m17n
Summary:        A m17n plugin for mlterm
Group:          System/X11/Terminals
Provides:       locale(m17n:ja;ko;zh;ar;he)

%description m17n
A plugin to use the m17n input methods directly from mlterm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -rf doc/{en,ja}/*win32

%build
%configure \
  --disable-static \
  --libexecdir=%{_libdir}/mlterm \
  --sysconfdir=%{_sysconfdir}/X11 \
  --disable-utmp \
  --enable-anti-alias \
  --enable-fribidi \
  --enable-ssh2 \
  --enable-vt52 \
  --enable-ind \
  --enable-m17nlib \
  --enable-ibus \
  --disable-fcitx \
  --enable-wnn \
  --enable-canna \
  --enable-scim \
  --enable-uim \
  --with-gtk=3.0 \
  --with-tools=mlclient,mlcc,mlfc,mlmenu,mlterm-zoom,mlimgloader,mlconfig \
  --with-scrollbars=sample,extra,pixmap_engine \
  --with-type-engines=xcore,cairo \
  --with-imagelib=gdk-pixbuf \
  --enable-optimize-redrawing
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -m 644 contrib/tool/mlterm-menu/menu %{buildroot}%{_sysconfdir}/X11/mlterm/
install -D -m644 "contrib/icon/%{name}-icon.svg" \
  "%{buildroot}%{_datadir}/pixmaps/%{name}.svg"
install -D -m644 "contrib/icon/%{name}-icon-trans.svg" \
  "%{buildroot}%{_datadir}/pixmaps/mlclient.svg"

mv %{buildroot}%{_libdir}/mlterm/mlterm/mlterm-zoom \
   %{buildroot}%{_bindir}/mlterm-zoom
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang mlconfig
%suse_update_desktop_file -i %{name} TerminalEmulator

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f mlconfig.lang
%doc LICENCE* README* doc/en doc/ja
%attr(555,root,tty) %{_bindir}/mlterm
%{_datadir}/applications/%{name}.desktop
%{_bindir}/mlclient
%{_bindir}/mlclientx
%{_bindir}/mlcc
%{_bindir}/mlterm-zoom
%{_bindir}/mlfc
%{_libdir}/libpobl.*
%{_libdir}/libmlterm_coreotl.so
%{_libdir}/libmef.so*
%dir %{_libdir}/mef
%{_libdir}/mef/libmef_*
%dir %{_libdir}/mlterm/
%dir %{_libdir}/mlterm/mlterm
%{_libdir}/mlterm/libathena.so
%{_libdir}/mlterm/libim-kbd.so
%{_libdir}/mlterm/libmotif.so
%{_libdir}/mlterm/libmozmodern.so
%{_libdir}/mlterm/libnext.so
%{_libdir}/mlterm/libsample.so
%{_libdir}/mlterm/libctl_bidi.so
%{_libdir}/mlterm/libctl_iscii.so
%{_libdir}/mlterm/libim-skk.so
%{_libdir}/mlterm/libind_assamese.so
%{_libdir}/mlterm/libind_bengali.so
%{_libdir}/mlterm/libind_gujarati.so
%{_libdir}/mlterm/libind_hindi.so
%{_libdir}/mlterm/libind_iitkeyb.so
%{_libdir}/mlterm/libind_inscript.so
%{_libdir}/mlterm/libind_kannada.so
%{_libdir}/mlterm/libind_malayalam.so
%{_libdir}/mlterm/libind_oriya.so
%{_libdir}/mlterm/libind_punjabi.so
%{_libdir}/mlterm/libind_tamil.so
%{_libdir}/mlterm/libind_telugu.so
%{_libdir}/mlterm/libotl.so
%{_libdir}/mlterm/libpixmap_engine.so
%{_libdir}/mlterm/libptyssh.so
%{_libdir}/mlterm/libtype_cairo.so
%{_libdir}/mlterm/mlterm/mlimgloader
%{_libdir}/mlterm/mlterm/mlconfig
%{_libdir}/mlterm/mlterm/mlmenu
%dir %{_sysconfdir}/X11/mlterm/
%config %{_sysconfdir}/X11/mlterm/*
%{_mandir}/man?/*
%{_datadir}/pixmaps/*
%dir %{_datadir}/mlterm/
%dir %{_datadir}/mlterm/scrollbars/
%dir %{_datadir}/mlterm/scrollbars/sample3/
%{_datadir}/mlterm/scrollbars/sample3/*

%files canna
%{_libdir}/mlterm/libim-canna.so

%files ibus
%{_libdir}/mlterm/libim-ibus.so

%files wnn
%{_libdir}/mlterm/libim-wnn.so

%files scim
%{_libdir}/mlterm/libim-scim.so

%files uim
%{_libdir}/mlterm/libim-uim.so

%files m17n
%{_libdir}/mlterm/libim-m17nlib.so

%changelog
