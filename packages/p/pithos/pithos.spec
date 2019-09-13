#
# spec file for package pithos
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012-2014 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%global appid io.github.Pithos
Name:           pithos
Version:        1.4.1
Release:        0
Summary:        Native Pandora Radio client for Linux
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Other
Url:            https://pithos.github.io/
Source0:        https://github.com/pithos/pithos/releases/download/%{version}/pithos-%{version}.tar.xz
# PATCH-FIX-UPSTREAM pithos-fix-deprecated-pygobject.patch -- Fix deprecated PyGObject usage
Patch0:         pithos-fix-deprecated-pygobject.patch

BuildRequires:  gdk-pixbuf-devel
BuildRequires:  glib2-devel
BuildRequires:  meson
# Needed for automatic typelib() Requires.
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python3-devel >= 3.4
BuildRequires:  update-desktop-files
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-good
Requires:       python3-cairo
Requires:       python3-gobject-Gdk
# Implementation of secret service
Recommends:     gnome-keyring
BuildArch:      noarch

%description
Pithos is a native Pandora Radio client for Linux. It's much more
lightweight than the Pandora.com web client, and integrates with desktop
features such as media keys, notifications, and the sound menu.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name \*.pyc -delete # boo#1110032
%py3_compile %{buildroot}

# Remove unnecessary icons
rm -rf %{buildroot}%{_datadir}/icons/ubuntu-mono*

%suse_update_desktop_file %{appid}

%if 0%{?suse_version} < 1330
%post
%glib2_gsettings_schema_post
%desktop_database_post
%icon_theme_cache_post

%postun
%glib2_gsettings_schema_postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root)
%doc license README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{appid}.appdata.xml
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/io.github.Pithos.service
%{_mandir}/man1/pithos.1%{?ext_man}

%changelog
