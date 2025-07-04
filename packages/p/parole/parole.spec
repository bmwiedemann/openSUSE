#
# spec file for package parole
#
# Copyright (c) 2025 SUSE LLC
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


Name:           parole
Version:        4.20.0
Release:        0
Summary:        Media Player for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://docs.xfce.org/apps/parole/start
Source0:        https://archive.xfce.org/src/apps/parole/4.20/%{name}-%{version}.tar.xz
BuildRequires:  appstream-glib
BuildRequires:  gettext >= 0.19.8
BuildRequires:  meson >= 0.56.0
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(clutter-1.0) >= 1.16.4
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.4.4
BuildRequires:  pkgconfig(dbus-1) >= 0.60
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.70
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.38.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libnotify) >= 0.7.8
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.16.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.16.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.16.0
BuildRequires:  pkgconfig(taglib) >= 1.4
BuildRequires:  pkgconfig(x11) >= 1.6.7
Recommends:     %{name}-lang = %{version}
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good

%description
Parole is a media player based on the GStreamer framework and written
to fit in the Xfce desktop. Parole features playback of local media
files, DVD/CD and live streams. Parole is extensible via plugins; for
a how-to document for writing a Parole plugin, see the Plugins API
documentation and the plugins directory which contains some examples.

%package devel
Summary:        Development Files for Parole
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gtk+-3.0)
Requires:       pkgconfig(libxfce4util-1.0)

%description devel
This package contains development files for developing plugins for parole.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -type f -name "*.la" -delete -print

%suse_update_desktop_file -G "Parole Media Player" org.xfce.Parole

%find_lang %{name} %{?no_lang_C}

# Validation currently fails (bxo#15751)
# appstream-util validate-relax --nonet %%{buildroot}%%{_datadir}/metainfo/*.appdata.xml

%files
%doc AUTHORS NEWS THANKS TODO README.md
%license COPYING
%{_bindir}/parole
%{_datadir}/applications/org.xfce.Parole.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/parole/
%{_libdir}/parole-0/
%{_datadir}/metainfo/%{name}.appdata.xml

%files lang -f %{name}.lang

%files devel
%{_includedir}/parole/

%changelog
