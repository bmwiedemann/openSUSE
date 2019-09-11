#
# spec file for package gnome-subtitles
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


Name:           gnome-subtitles
Version:        1.4.2
Release:        0
Summary:        Subtitle editor for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://gnomesubtitles.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  intltool >= 0.50
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(gtk-sharp-3.0) >= 2.99.3
BuildRequires:  pkgconfig(mono) >= 4.0
Requires:       gstreamer-plugins-base
Requires:       mono-core
Recommends:     %{name}-lang

%description
Gnome Subtitles is a subtitle editor for the GNOME desktop. It supports
the most common text-based subtitle formats and allows for subtitle
editing, translation and synchronization.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%configure \
	--enable-gtk-doc \
	%{nil}
# Disable parallel build - mono fails to often with it
make -j1

%install
%make_install
find %{buildroot}%{_libdir} -type f -name "*.la" -delete
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_mandir}/man1/gnome-subtitles.1%{ext_man}
%{_datadir}/pixmaps/gnome-subtitles.svg
%{_datadir}/glib-2.0/schemas/org.gnome.GnomeSubtitles.gschema.xml
%{_datadir}/applications/org.gnome.GnomeSubtitles.desktop
%{_datadir}/help/C/gnome-subtitles/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.GnomeSubtitles.appdata.xml

%files lang -f %{name}.lang

%changelog
