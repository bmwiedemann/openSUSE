#
# spec file for package snapshot
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define gstreamer_version 1.20

Name:           snapshot
Version:        49.1
Release:        0
Summary:        Take pictures and videos
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/snapshot
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst

BuildRequires:  AppStream
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  liblcms2-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libxml2-tools
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.75
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer_version}
BuildRequires:  pkgconfig(gtk4) >= 4.13.6
BuildRequires:  pkgconfig(libadwaita-1) >= 1.7.alpha
## Needed for camerabin
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0) >= %{gstreamer_version}
##
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= %{gstreamer_version}
Requires:       gstreamer-plugins-rs

%description
%{summary}.

%lang_package

%prep
%autosetup -p1 -a1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
%{cargo_test}
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Snapshot.desktop
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/org.gnome.Snapshot.metainfo.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Snapshot.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Snapshot.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Snapshot.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Snapshot-symbolic.svg
%{_datadir}/metainfo/org.gnome.Snapshot.metainfo.xml
%{_datadir}/dbus-1/services/org.gnome.Snapshot.service
# resources.gresource should probably not be packaged, but never mind this early in the development
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources.gresource

%files lang -f %{name}.lang

%changelog
