#
# spec file for package mate-media
#
# Copyright (c) 2020 SUSE LLC
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


%define _version 1.24
Name:           mate-media
Version:        1.24.1
Release:        0
Summary:        MATE Desktop multimedia stack
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  mate-common >= %{_version}
BuildRequires:  mate-control-center-devel >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libmatemixer) >= %{_version}
BuildRequires:  pkgconfig(libmatepanelapplet-4.0) >= %{_version}
BuildRequires:  pkgconfig(libxml-2.0)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
This package provides the Multimedia stack used by the MATE Desktop.

%lang_package

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static     \
  --libexecdir=%{_libexecdir}/%{name} \
  --disable-statusicon \
  --enable-profiles
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file mate-volume-control
%fdupes %{buildroot}%{_datadir}/

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/mate-volume-control
%{_libexecdir}/mate-media/
%{_datadir}/mate-media/
%{_datadir}/dbus-1/services/org.mate.panel.applet.GvcAppletFactory.service
%{_datadir}/mate-panel/
%{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/org.mate.applets.GvcApplet.mate-panel-applet
%{_datadir}/sounds/mate/
%{_datadir}/applications/*.desktop
%{_mandir}/man?/mate-volume-control-applet.?%{?ext_man}
%{_mandir}/man?/mate-volume-control.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
