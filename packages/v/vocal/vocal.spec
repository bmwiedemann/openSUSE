#
# spec file for package vocal
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


Name:           vocal
Version:        2.4.2
Release:        0
Summary:        A podcast client for the desktop
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Other
URL:            https://vocalproject.net/
Source:         https://github.com/needle-and-thread/vocal/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM vocal-fix-build.patch -- https://github.com/needle-and-thread/vocal/issues/483
Patch0:         vocal-fix-build.patch
# PATCH-FIX-UPSTREAM vocal-2.4.2-vala-0.56.patch -- https://github.com/VocalPodcastProject/vocal/pull/503, rebased on 2.4.2
Patch1:         vocal-2.4.2-vala-0.56.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  rsvg-convert
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
%glib2_gsettings_schema_requires

%description
A podcast application designed for Elementary OS and other GTK-based
Linux desktops. Includes a built-in video player, automatic updating,
smart library management, library importing and exporting, custom
skip intervals, and more.

%lang_package

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} %{?no_lang_C}

# CONVERT SVG ICONS INSTALLED INTO NON-SCALABLE DIR TO PNG ONES
for i in 16 22 24 32 48 64 128
do
  rsvg-convert  -o %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/com.github.needleandthread.vocal.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/com.github.needleandthread.vocal.svg
  rm %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/com.github.needleandthread.vocal.svg
done

%fdupes %{buildroot}%{_datadir}/locale/

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/com.github.needleandthread.vocal
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/com.github.needleandthread.vocal.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/%{name}/

%files lang -f %{name}.lang

%changelog
