#
# spec file for package vocal
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           vocal
Version:        2.4.2
Release:        0
Summary:        A podcast client for the desktop
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Other
URL:            https://launchpad.net/vocal
Source:         https://github.com/needle-and-thread/vocal/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
%if 0%{suse_version} >= 1550
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
A podcast application designed for Elementary OS and other GTK-based
Linux desktops. Includes a built-in video player, automatic updating,
smart library management, library importing and exporting, custom
skip intervals, and more.

%lang_package

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install %{?_smp_mflags}
%find_lang %{name} %{?no_lang_C}

# CONVERT SVG ICONS INSTALLED INTO NON-SCALABLE DIR TO PNG ONES
for i in 16 22 24 32 48 64 128
do
  rsvg-convert  -o %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/com.github.needleandthread.vocal.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/com.github.needleandthread.vocal.svg
  rm %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/com.github.needleandthread.vocal.svg
done

%suse_update_desktop_file com.github.needleandthread.vocal Player
%fdupes %{buildroot}%{_datadir}/locale/

%files
%license COPYING
%doc %attr(0644,root,root) AUTHORS README.md
%{_bindir}/com.github.needleandthread.vocal
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/com.github.needleandthread.vocal.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/%{name}

%files lang -f %{name}.lang

%changelog
