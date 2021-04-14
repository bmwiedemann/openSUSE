#
# spec file for package mousepad
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


Name:           mousepad
Version:        0.5.4
Release:        0
Summary:        Simple Text Editor for Xfce
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            https://docs.xfce.org/apps/mousepad/start
Source:         https://archive.xfce.org/src/apps/mousepad/0.5/mousepad-%{version}.tar.bz2
BuildRequires:  appstream-glib
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.52.0
BuildRequires:  pkgconfig(gthread-2.0)  >= 2.52.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libxfconf-0)

%description
Mousepad is a simple text editor for Xfce.

%lang_package

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%find_lang %{name} %{?no_lang_C}

%suse_update_desktop_file %{name}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%files
%doc AUTHORS NEWS ChangeLog README.md
%license COPYING
%{_bindir}/mousepad
%{_datadir}/applications/mousepad.desktop
%{_datadir}/glib-2.0/schemas/org.xfce.mousepad.gschema.xml
%{_datadir}/polkit-1/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/org.xfce.mousepad.*

%files lang -f %{name}.lang

%changelog
