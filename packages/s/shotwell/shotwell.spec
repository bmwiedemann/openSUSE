#
# spec file for package shotwell
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           shotwell
Version:        33.0
Release:        0
Summary:        Photo Manager for GNOME
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://gitlab.gnome.org/GNOME/shotwell

Source0:        https://download.gnome.org/sources/shotwell/%{version}/%{name}-%{version}.tar.xz
Source99:       shotwell-rpmlintrc
BuildSystem:    meson
BuildOption:    -D install_apport_hook=false

BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson >= 0.43.0
BuildRequires:  vala >= 0.28.0

%description
Shotwell is a digital photo organizer designed for the GNOME desktop
environment. It allows you to import photos from disk or camera,
organize them in various ways, view them in full-window or fullscreen
mode, and export them to share with others.

%lang_package

%generate_buildrequires
%meson_buildrequires

%install -a
%fdupes %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS THANKS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/shotwell
%{_datadir}/applications/org.gnome.Shotwell-Viewer.desktop
%{_datadir}/applications/org.gnome.Shotwell.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.shotwell-extras.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shotwell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.yorba.shotwell-extras.gschema.xml
%{_datadir}/glib-2.0/schemas/org.yorba.shotwell.gschema.xml
%{_datadir}/icons/hicolor/*/*/org.gnome.Shotwell*
%{_datadir}/metainfo/org.gnome.Shotwell.metainfo.xml
%{_libdir}/shotwell/
# This is not split as the only consumer is shotwell itself.
%{_libdir}/libshotwell-authenticator.so
%{_libdir}/libshotwell-authenticator.so.*
%{_libdir}/libshotwell-plugin-common.so
%{_libdir}/libshotwell-plugin-common.so.*
%{_libdir}/libshotwell-plugin-dev-1.0.so
%{_libdir}/libshotwell-plugin-dev-1.0.so.*
%dir %{_libexecdir}/shotwell
%{_libexecdir}/shotwell/shotwell-settings-migrator
%{_libexecdir}/shotwell/shotwell-video-thumbnailer
%{_mandir}/man1/shotwell.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
