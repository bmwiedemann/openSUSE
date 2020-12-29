#
# spec file for package fractal
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


Name:           fractal
Version:        4.4.0
Release:        0
Summary:        Matrix group messaging app
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://wiki.gnome.org/Apps/Fractal
Source0:        https://gitlab.gnome.org/GNOME/fractal/uploads/d4168ac40fd681240964705e000dd353/%{name}-%{version}.tar.xz
BuildRequires:  cargo
BuildRequires:  gmp-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  pkgconfig(atk) >= 2.4
BuildRequires:  pkgconfig(cairo) >= 1.10
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-3.0) >= 3.22
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gspell-1) >= 1.8
BuildRequires:  pkgconfig(gst-editing-services-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-bad-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)  >= 3.22
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0
BuildRequires:  pkgconfig(libhandy-0.0) >= 0.0.5
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango) >= 1.34
BuildRequires:  pkgconfig(pangocairo) >= 1.34

%description
Fractal is a Matrix messaging app for GNOME written in Rust. Its
interface is tuned for collaboration in large groups, such as
free software projects.

%lang_package

%prep
%autosetup -p1

%build
# bypass error https://bugzilla.opensuse.org/show_bug.cgi?id=1175502
# to avoid cargo reported error if config.guess has been changed
# by build macro.
%ifarch ppc64le
guessname='src/libbacktrace/config.guess'
cfgguess="./vendor/backtrace-sys/$guessname"
chkjson='./vendor/backtrace-sys/.cargo-checksum.json'
if [[ -f $cfgguess ]] && [[ -f $chkjson ]]; then
  chksum=`sha256sum $cfgguess |sed -e 's/ .*//'`
  grep -q $guessname $chkjson && grep -q $chksum $chkjson || sed -i -e "s#\($guessname.:.\)[0-9a-f]*#\1$chksum#" $chkjson
fi
%endif

%define _lto_cflags %{nil}
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.Fractal.metainfo.xml
%{_datadir}/applications/org.gnome.Fractal.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.Fractal*.*
%{_datadir}/glib-2.0/schemas/org.gnome.Fractal.gschema.xml

%files lang -f %{name}.lang

%changelog
