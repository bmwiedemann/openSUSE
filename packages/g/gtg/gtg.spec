#
# spec file for package gtg
#
# Copyright (c) 2021 SUSE LLC
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

Name:           gtg
Version:        0.5
Release:        0
Summary:        Personal Organizer for GNOME
License:        GPL-3.0+
Group:          Productivity/Office/Organizers
URL:            https://wiki.gnome.org/Apps/GTG
Source0:        https://github.com/getting-things-gnome/gtg/archive/refs/tags/v0.5.tar.gz

BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  meson
Requires:       python3-pycairo
Requires:       python3-gobject-Gdk
Requires:       python3-lxml
Requires:       python3-liblarch
Requires:       python3-liblarch-gtk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
