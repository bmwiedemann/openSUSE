#
# spec file for package peek
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


Name:           peek
Version:        1.4.0
Release:        0
Summary:        An animated GIF recorder
License:        GPL-3.0-or-later
URL:            https://github.com/phw/peek
Source:         https://github.com/phw/peek/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool >= 0.19
BuildRequires:  meson >= 0.37.0
BuildRequires:  pkgconfig
BuildRequires:  txt2man
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(vapigen) >= 0.22
Requires:       ImageMagick
Requires:       ffmpeg
Recommends:     %{name}-lang
%lang_package

%description
A simple tool that allows you to record short animated GIF images from your screen.
Currently, only X11 window system is supported.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.uploadedlobster.peek Utility DesktopUtility
%find_lang %{name}

%files
%license LICENSE
%{_bindir}/peek
%{_datadir}/glib-2.0/schemas/com.uploadedlobster.peek.gschema.xml
%{_datadir}/applications/com.uploadedlobster.peek.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.uploadedlobster.peek.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.uploadedlobster.peek-symbolic.svg
%{_datadir}/dbus-1/services/com.uploadedlobster.peek.service
%{_datadir}/metainfo/com.uploadedlobster.peek.appdata.xml
%{_mandir}/man1/peek.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
