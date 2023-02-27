#
# spec file for package mlterm
#
# Copyright (c) 2023 SUSE LLC
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


%global _configure ../configure
%global flavors with-gui=wayland with-gui=sdl2 with-gtk=3.0
Name:           mlterm
Version:        3.9.2
Release:        0
Summary:        Multilingual Terminal Emulator for X and Wayland
License:        BSD-3-Clause
Group:          System/X11/Terminals
URL:            https://mlterm.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/mlterm/01release/%{name}-%{version}/%{name}-%{version}.tar.gz
Source10:       %{name}.desktop
Patch0:         etc.patch
Patch1:         CVE-2022-24130-c_sixel.c-Fix-segmentation-fault-when-the-repeat-cou.patch
Patch2:         mlterm-Fix-buffer-overflow-with-long-plugin-suffix.patch
Patch3:         mlfc-Fix-crash-with-more-than-1024-font-faces-installed.patch
Patch4:         mlterm-SDL2-UI-also-needs-math-libs.patch
Patch5:         mlterm-wayland-Detect-compiler-flags.patch
BuildRequires:  ccache
BuildRequires:  coreutils
BuildRequires:  fwnn-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  scim-devel
BuildRequires:  uim-devel
BuildRequires:  update-desktop-files
%if 0%{?sle_version} && 0%{?sle_version} <= 150400
BuildRequires:  pkgconfig(fcitx)
%else
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5GClient)
%endif
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gail)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(m17n-core)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wordcut)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       %{name}-common = %{version}-%{release}
Provides:       locale(xorg-x11:ja;ko;zh;ar;he)

%description
Mlterm is a multilingual terminal emulator for the X Window System and Wayland.

Multilingual features:

supported charsets: US_ASCII, ISO8859[1-11], ISO8859[13-16], TCVN5712,
VISCII, KOI8_R, KOI8_U, JISX0201, JISX0208, JISX0212, JISX0213, GB2312,
GBK, KSC5601, UHC, CNS11643-N, Big5, UCS2(4)

supported encodings: ISO-8859-[1-11], ISO-8859- [13-16], TCVN5612,
VISCII, KOI8_R, KOI8_U, EUC-JP, EUC-JISX0213, ISO-2022-JP [1, 2, 3],
Shift_JIS, Shift_JISX0213, EUC-KR, UHC, JOHAB, ISO-2022-KR,
ISO-2022-CN, GB2312(EUC-CN), GBK, GB18030, EUC-TW, Big5, Hz, UTF-8

character composition: TIS620, TCVN5712, JISX0213, UNICODE

Multiple IMs are also supported and you can dynamically change various
IMs.

Other features:
* scroll by wheel mouse
* antialias font (requires Xft and Xrender extensions)
* proportional font
* transparent background
* background image (requires Imlib)
* multiple pty windows
* scrollbar plug-in API (unstable)

%package common
Summary:        Multilingual Terminal Emulator common files
Group:          System/Terminals
Conflicts:      %{name} < %{version}-%{release}
%if 0%{?suse_version} >= 1330
Requires:       group(tty)
%endif

%description common
Common files for Mlterm multilingual terminal emulator

%package sdl2
Summary:        Multilingual Terminal Emulator using SDL rendering
Group:          System/Terminals
Requires:       %{name}-common = %{version}-%{release}
Provides:       locale(ja;ko;zh;ar;he)

%description sdl2
Mlterm is a multilingual terminal emulator using SDL rendering

Multilingual features:

supported charsets: US_ASCII, ISO8859[1-11], ISO8859[13-16], TCVN5712,
VISCII, KOI8_R, KOI8_U, JISX0201, JISX0208, JISX0212, JISX0213, GB2312,
GBK, KSC5601, UHC, CNS11643-N, Big5, UCS2(4)

supported encodings: ISO-8859-[1-11], ISO-8859- [13-16], TCVN5612,
VISCII, KOI8_R, KOI8_U, EUC-JP, EUC-JISX0213, ISO-2022-JP [1, 2, 3],
Shift_JIS, Shift_JISX0213, EUC-KR, UHC, JOHAB, ISO-2022-KR,
ISO-2022-CN, GB2312(EUC-CN), GBK, GB18030, EUC-TW, Big5, Hz, UTF-8

character composition: TIS620, TCVN5712, JISX0213, UNICODE

Multiple IMs are also supported and you can dynamically change various
IMs.

Other features:
* proportional font
* background image (requires Imlib)
* multiple pty windows
* scrollbar plug-in API (unstable)

%package fcitx
Summary:        A fcitx plugin for mlterm
Group:          System/X11/Terminals
Provides:       locale(fcitx:ja;ko;ar;he)

%description fcitx
A plugin to use the fcitx input methods directly from mlterm.

%package ibus
Summary:        Ibus plugin for mlterm
Group:          System/X11/Terminals
Provides:       locale(scim:ja;ko;ar;he)

%description ibus
A plugin to use the ibus input methods directly from mlterm.

%package m17n
Summary:        A m17n plugin for mlterm
Group:          System/X11/Terminals
Provides:       locale(m17n:ja;ko;zh;ar;he)

%description m17n
A plugin to use the m17n input methods directly from mlterm.

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

%package wnn
Summary:        Wnn plugin for mlterm
Group:          System/X11/Terminals
Provides:       locale(scim:ja;ko;ar;he)

%description wnn
A plugin to use the wnn input methods directly from mlterm.

%prep
%setup -q
%autopatch -p1

rm -rf doc/{en,ja}/*win32

%build
export INSTALL_OPT='-m 755'

for i in %{flavors} ; do
mkdir $i
pushd $i
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
  --enable-fcitx \
  --enable-wnn \
  --enable-scim \
  --enable-uim \
  --with-tools=mlclient,mlcc,mlfc,mlmenu,mlterm-zoom,mlimgloader,mlconfig \
  --with-scrollbars=sample,extra,pixmap_engine \
  --with-type-engines=xcore,cairo \
  --with-imagelib=gdk-pixbuf \
  --enable-optimize-redrawing \
  --$i
make -O %{?_smp_mflags}
popd
done

%install
for i in %{flavors} ; do
pushd $i
%make_install
popd
done
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -m 644 contrib/tool/mlterm-menu/menu %{buildroot}%{_sysconfdir}/X11/mlterm/
install -D -m644 "contrib/icon/%{name}-icon.svg" \
  "%{buildroot}%{_datadir}/pixmaps/%{name}.svg"
install -D -m644 "contrib/icon/%{name}-icon-trans.svg" \
  "%{buildroot}%{_datadir}/pixmaps/mlclient.svg"

ln -s %{_mandir}/man1/mlterm.1 %{buildroot}%{_mandir}/man1/mlterm-wl.1
cp -a %{buildroot}%{_mandir}/man1/mlterm.1 %{buildroot}%{_mandir}/man1/mlterm-sdl2.1

mv %{buildroot}%{_libdir}/mlterm/mlterm/mlterm-zoom \
   %{buildroot}%{_bindir}/mlterm-zoom
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang mlconfig
%suse_update_desktop_file -i %{name} TerminalEmulator

%post -n %{name}-common -p /sbin/ldconfig
%postun -n %{name}-common -p /sbin/ldconfig

%files
%attr(555,root,tty) %{_bindir}/mlterm
%attr(555,root,tty) %{_bindir}/mlterm-wl
%{_bindir}/mlterm-zoom
%{_mandir}/man?/mlterm.?.gz
%{_mandir}/man?/mlterm-wl.?.gz
%{_datadir}/applications/%{name}.desktop
%dir %{_sysconfdir}/X11/mlterm/
%config %{_sysconfdir}/X11/mlterm/*
%{_libdir}/mlterm/libim-kbd.so
%{_libdir}/mlterm/libim-kbd-wl.so
%{_libdir}/mlterm/libim-skk.so
%{_libdir}/mlterm/libim-skk-wl.so
%{_libdir}/mlterm/libathena.so
%{_libdir}/mlterm/libmotif.so
%{_libdir}/mlterm/libmozmodern.so
%{_libdir}/mlterm/libnext.so
%{_libdir}/mlterm/libsample.so
%{_libdir}/mlterm/libpixmap_engine.so
%{_libdir}/mlterm/libtype_cairo.so
%dir %{_libdir}/mlterm/mlterm
%{_libdir}/mlterm/mlterm/mlimgloader
%{_libdir}/mlterm/mlterm/mlconfig
%{_libdir}/mlterm/mlterm/mlmenu

%files common -f mlconfig.lang
%license LICENCE*
%doc README* doc/en doc/ja
%{_bindir}/mlclient
%{_bindir}/mlclientx
%{_bindir}/mlcc
%{_bindir}/mlfc
%{_libdir}/libpobl.*
%{_libdir}/libmlterm_coreotl.so
%{_libdir}/libmef.so*
%dir %{_libdir}/mef
%{_libdir}/mef/libmef_*
%dir %{_libdir}/mlterm/
%{_libdir}/mlterm/libctl_bidi.so
%{_libdir}/mlterm/libctl_iscii.so
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
%{_libdir}/mlterm/libind_telugu.so
%{_libdir}/mlterm/libotl.so
%{_libdir}/mlterm/libptyssh.so
%{_libdir}/mlterm/libzmodem.so
%{_mandir}/man?/ml[^t]*
%{_datadir}/pixmaps/*
%dir %{_datadir}/mlterm/
%dir %{_datadir}/mlterm/scrollbars/
%dir %{_datadir}/mlterm/scrollbars/sample3/
%{_datadir}/mlterm/scrollbars/sample3/*

%files sdl2
%attr(555,root,tty) %{_bindir}/mlterm-sdl2
%{_mandir}/man?/mlterm-sdl2.?.gz
%{_libdir}/mlterm/libim-kbd-sdl2.so
%{_libdir}/mlterm/libim-skk-sdl2.so

%files fcitx
%{_libdir}/mlterm/libim-fcitx*.so

%files ibus
%{_libdir}/mlterm/libim-ibus*.so

%files m17n
%{_libdir}/mlterm/libim-m17nlib*.so

%files scim
%{_libdir}/mlterm/libim-scim*.so

%files uim
%{_libdir}/mlterm/libim-uim*.so

%files wnn
%{_libdir}/mlterm/libim-wnn*.so

%changelog
