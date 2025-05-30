#
# spec file for package catfish
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_with git
%define series 4.20
%define xfce_version 4.16

Name:           catfish
Version:        4.20.1
Release:        0
Summary:        Versatile File Searching Tool
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            https://docs.xfce.org/apps/catfish/start
Source:         https://archive.xfce.org/src/apps/%{name}/%{series}/%{name}-%{version}.tar.xz
%if 0%{?suse_version} < 1600
# PATCH-FIX-OPENSUSE: Force-disable Zeitgeist
Patch0:         0001-Force-disable-Zeitgeist-support.patch
# PATCH-FIX-OPENSUSE: Relax python3 requirement for Leap 15.6
Patch1:         relax-python-requirement.patch
%endif
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
%if 0%{?suse_version} >= 01550 || 0%{?sle_version} >= 150200 && 0%{?is_opensuse}
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  gobject-introspection
BuildRequires:  gtk3-devel >= 3.22
BuildRequires:  meson >= 0.54.0
BuildRequires:  python3
BuildRequires:  python3-dbus-python
BuildRequires:  python3-dbus-python-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-pexpect
BuildRequires:  python3-xml
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.42.8
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfce_version}
BuildRequires:  pkgconfig(pango) >= 1.38.0
%if 0%{?suse_version} > 1600
BuildRequires:  pkgconfig(zeitgeist-2.0) >= 1.0
%endif
# ...OK
Requires:       findutils-locate
Requires:       gdk-pixbuf-loader-rsvg
Requires:       gsettings-backend-dconf
Requires:       python3
Requires:       python3-dbus-python
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-pexpect
Requires:       python3-xml
Requires:       sudo
Recommends:     %{name}-lang
BuildArch:      noarch

%description
Catfish is a GTK+ search utility written in python. Its search is powered by
/usr/bin/find and /usr/bin/locate, with search suggestions provided by
zeitgeist.

%lang_package

%prep
%if 0%{?suse_version} > 1600
%autosetup
%else
%autosetup -p1
%endif

%build
%meson
%meson_build

%install
%meson_install
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%suse_update_desktop_file -r org.xfce.Catfish GNOME Utility Filesystem

%fdupes %{buildroot}%{python3_sitelib}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%find_lang %{name}

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/org.xfce.Catfish.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.catfish.*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}_lib
%{_mandir}/man?/%{name}.?%{ext_man}

%files lang -f %{name}.lang

%changelog
