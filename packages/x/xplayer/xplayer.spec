#
# spec file for package xplayer
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


%bcond_with     zeitgeist
Name:           xplayer
Version:        2.4.4
Release:        0
Summary:        Generic media player
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/linuxmint/xplayer
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM return no value in void function
Patch0:         xplayer-2.2.1-return-no-value-in-void-function.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gstreamer-plugins-good >= 0.11.93
# For gst-inspect tool
BuildRequires:  gstreamer-utils >= 0.11.93
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-pylint
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.14.1
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(%{name}-plparser)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(clutter-1.0) >= 1.10.0
BuildRequires:  pkgconfig(clutter-gst-3.0) >= 2.99.2
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.0.2
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.82
BuildRequires:  pkgconfig(glib-2.0) >= 2.33.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.93
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0) >= 1.0.2
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 0.11.93
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.1.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  pkgconfig(lirc)
BuildRequires:  pkgconfig(pygobject-3.0) >= 2.90.3
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xapp)
BuildRequires:  pkgconfig(xkbfile)
%if %{with zeitgeist}
BuildRequires:  pkgconfig(zeitgeist-2.0) >= 0.9.12
%else
Obsoletes:      %{name}-plugin-zeitgeist <= %{version}
%endif
Requires:       gstreamer-plugin-cluttergst3
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       iso-codes
Requires:       python3-gobject-Gdk
Recommends:     %{name}-plugins
Suggests:       gnome-dvb-daemon
Obsoletes:      %{name}-browser-plugin < %{version}
Obsoletes:      %{name}-browser-plugin-gmp < %{version}
Obsoletes:      %{name}-browser-plugin-vegas < %{version}

%description
xplayer is a media player based on GStreamer for the Cinnamon
desktop and others. It features a playlist, a full-screen mode,
seek and volume controls, and complete keyboard navigation.

%package plugins
Summary:        Plugins for xplayer media player
Requires:       %{name} = %{version}
Recommends:     brasero
Recommends:     python3-beautifulsoup4
Recommends:     python3-httplib2
Suggests:       gromit

%description plugins
xplayer is a media player based on GStreamer for the Cinnamon
desktop and others. It features a playlist, a full-screen mode,
seek and volume controls, and complete keyboard navigation.

This package includes plugins for xplayer, to add advanced features.

%if %{with zeitgeist}
%package plugin-zeitgeist
Summary:        Plugins for xplayer media player -- Zeitgeist Support
Requires:       %{name} = %{version}

%description plugin-zeitgeist
xplayer is a media player based on GStreamer for the Cinnamon
desktop and others. It features a playlist, a full-screen mode,
seek and volume controls, and complete keyboard navigation.

This package includes the Zeitgeist plugin for xplayer.
%endif

%package devel
Summary:        Development files for xplayer media player
Requires:       %{name} = %{version}

%description devel
xplayer is a media player based on GStreamer for the Cinnamon
desktop and others. It features a playlist, a full-screen mode,
seek and volume controls, and complete keyboard navigation.

This package contains files for development.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static \
  --disable-Werror
%make_build

%install
%make_install
%suse_update_desktop_file %{name}
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

# delete .la file
rm -f %{buildroot}%{_libdir}/lib%{name}.la

%post
%ldconfig

%postun
%ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}*
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.x.player.enums.xml
%{_datadir}/glib-2.0/schemas/org.x.player.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_datadir}/icons/hicolor/*/devices/%{name}*.*
%{_datadir}/icons/hicolor/*/actions/%{name}*.*
%dir %{_datadir}/thumbnailers/
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_datadir}/%{name}/
%{_mandir}/man?/%{name}*.?%{?ext_man}
# Own directories for plugins.
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins/
# Be careful here: libdir contains plugins while libexecdir
# contains a small utility for the main package.
%if "%{_libdir}" != "%{_libexecdir}"
%dir %{_libexecdir}/%{name}/
%endif
%{_libexecdir}/%{name}/%{name}-bugreport.py
%{_libdir}/lib%{name}.so.*
%{_libdir}/girepository-1.0/Xplayer-1.0.typelib
%{_datadir}/help/C/%{name}

%files lang -f %{name}.lang

%files plugins
%{_libdir}/%{name}/plugins/apple-trailers/
%{_libdir}/%{name}/plugins/autoload-subtitles/
%{_libdir}/%{name}/plugins/brasero-disc-recorder/
%{_libdir}/%{name}/plugins/chapters/
%{_libdir}/%{name}/plugins/dbus/
%{_libdir}/%{name}/plugins/grilo/
%{_libdir}/%{name}/plugins/gromit/
%{_libdir}/%{name}/plugins/im-status/
%{_libdir}/%{name}/plugins/lirc/
%{_libdir}/%{name}/plugins/media-player-keys/
%{_libdir}/%{name}/plugins/ontop/
%{_libdir}/%{name}/plugins/opensubtitles/
%{_libdir}/%{name}/plugins/properties/
%{_libdir}/%{name}/plugins/pythonconsole/
%{_libdir}/%{name}/plugins/recent/
%{_libdir}/%{name}/plugins/rotation/
%{_libdir}/%{name}/plugins/screensaver/
%{_libdir}/%{name}/plugins/screenshot/
%{_libdir}/%{name}/plugins/skipto/
%{_libdir}/%{name}/plugins/vimeo/
%{_datadir}/glib-2.0/schemas/org.x.player.plugins.opensubtitles.gschema.xml
%{_datadir}/glib-2.0/schemas/org.x.player.plugins.pythonconsole.gschema.xml

%if %{with zeitgeist}
%files plugin-zeitgeist
%{_libdir}/%{name}/plugins/zeitgeist-dp/
%endif

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/*.gir

%changelog
