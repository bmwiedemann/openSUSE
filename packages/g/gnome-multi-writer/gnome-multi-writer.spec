#
# spec file for package gnome-multi-writer
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


Name:           gnome-multi-writer
Version:        3.32.1
Release:        0
Summary:        Program for writing an ISO file to multiple USB devices at once
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/MultiWriter
Source0:        https://download.gnome.org/sources/gnome-multi-writer/3.32/%{name}-%{version}.tar.xz
BuildRequires:  docbook-utils-minimal
BuildRequires:  gobject-introspection-devel >= 0.9.8
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.25.9
BuildRequires:  pkgconfig(glib-2.0) >= 2.45.8
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.2
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gusb) >= 0.2.7
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.10
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(udisks2)
Recommends:     %{name}-lang

%description
GNOME MultiWriter can be used to write an ISO file to multiple USB devices
at once.
Supported drive sizes are between 1Gb and 32Gb.

MultiWriter may be useful for QA testing, to create a GNOME Live image
or a code sprint or to create hundreds of LiveUSB drives for a trade show.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file org.gnome.MultiWriter Filesystem X-GNOME-Utilities

%files
%license COPYING
%{_bindir}/%{name}
%{_libexecdir}/gnome-multi-writer-probe
%{_datadir}/glib-2.0/schemas/org.gnome.MultiWriter.gschema.xml
%{_datadir}/applications/org.gnome.MultiWriter.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.MultiWriter*
%{_datadir}/metainfo/org.gnome.MultiWriter.appdata.xml
# Just own these dirs, no need to buildrequire polkit
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.gnome.MultiWriter.policy
%{_mandir}/man1/gnome-multi-writer.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
