#
# spec file for package gtg
#
# Copyright (c) 2022 SUSE LLC
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


# TODO 1) Report unused itstool build requirement, despite it being
#         checked by the build script.
#      2) Meson is throwing out (gtg-0.6):
#         "NOTICE: Future-deprecated features used:
#                  0.56.0: {'meson.source_root'}"
#      3) Report unneeded shebang in Python modules and executable bits
#         on networkmanager.py.

Name:           gtg
Version:        0.6
Release:        0
Summary:        Personal Organizer for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Office/Organizers
URL:            https://wiki.gnome.org/Apps/GTG
Source0:        https://github.com/getting-things-gnome/gtg/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  python-rpm-macros
BuildRequires:  python3-cairo
BuildRequires:  python3-caldav
BuildRequires:  python3-gobject
BuildRequires:  python3-liblarch
BuildRequires:  python3-lxml
BuildRequires:  update-desktop-files
BuildRequires:  typelib(GLib)
BuildRequires:  typelib(GdkPixbuf)
BuildRequires:  typelib(Gtk) = 3.0
BuildRequires:  typelib(GtkSource) = 4
BuildRequires:  typelib(Pango)
## Run-time Requirements
Requires:       python3-gobject-Gdk
Requires:       python3-liblarch
Requires:       python3-liblarch-gtk
Requires:       python3-lxml
Requires:       python3-pycairo
## For GTG's plugins
# Hamster Time Tracker Integration
Recommends:     hamster-time-tracker
BuildArch:      noarch

%description
Getting Things GNOME! (GTG) is a personal organizer for the GNOME desktop
environment inspired by the Getting Things Done (GTD) methodology. GTG is
designed with flexibility, adaptability, and ease of use in mind so it can be
used as more than just GTD software.

GTG is intended to help you track everything you need to do and need to know,
from small tasks to large projects.

%lang_package

%prep
%autosetup -p1

## Fix shebang issues
pushd GTG
sed -i -e '1s/env //' gtg.in
sed -i -r '1s,(#!/bin/sh),# \1,' \
          plugins/export/export_templates/script_pocketmod
for file in core/info.py.in core/networkmanager.py; do
    sed -i -r '1s,^(#!/usr/bin/(|env )python3),# \1,' $file
    chmod -x $file
done
popd

%build
%meson %{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file org.gnome.GTG

%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}

%files
%license LICENSE
%doc AUTHORS NEWS README.md CONTRIBUTING.md
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gtg
%{python3_sitelib}/GTG/
%{_datadir}/applications/org.gnome.GTG.desktop
%{_datadir}/icons/hicolor
%{_datadir}/dbus-1/
%{_datadir}/metainfo/org.gnome.GTG.appdata.xml
%{_mandir}/man1/gtg.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
